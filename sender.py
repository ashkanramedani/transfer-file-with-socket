
import socket
import os
import threading
from tqdm import tqdm

# تنظیمات
CHUNK_SIZE = 1024 * 1024  # اندازه هر بخش: 1 مگابایت
SERVER_IP = ''  # آدرس سرور
SERVER_PORT = 5000  # پورت سرور
FILE_PATH = ''  # مسیر فایل بزرگ
NUM_THREADS = 10  # تعداد تردها برای ارسال موازی

# متغیر سراسری برای پراگرس بار
progress_bar = None

def send_chunk(start, end, conn):
    global progress_bar
    with open(FILE_PATH, 'rb') as f:
        f.seek(start)
        while start < end:
            data = f.read(CHUNK_SIZE)
            if not data:
                break
            conn.sendall(data)
            start += len(data)
            progress_bar.update(len(data))  # بروزرسانی پراگرس بار

    conn.close()

def send_file():
    global progress_bar
    file_size = os.path.getsize(FILE_PATH)
    chunk_size = file_size // NUM_THREADS  # تقسیم فایل به تعداد تردها

    # ایجاد پراگرس بار
    progress_bar = tqdm(total=file_size, unit="B", unit_scale=True, desc="Sending")

    threads = []
    for i in range(NUM_THREADS):
        start = i * chunk_size
        end = start + chunk_size if i != NUM_THREADS - 1 else file_size

        # اتصال به سرور برای هر ترد
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((SERVER_IP, SERVER_PORT))
        conn.sendall(f"{os.path.basename(FILE_PATH)}:{file_size}:{start}:{end}".encode())

        # ایجاد و شروع ترد برای ارسال بخش مورد نظر
        thread = threading.Thread(target=send_chunk, args=(start, end, conn))
        threads.append(thread)
        thread.start()

    # منتظر ماندن برای اتمام همه تردها
    for thread in threads:
        thread.join()

    progress_bar.close()
    print("File sent successfully!")

if __name__ == "__main__":
    send_file()
