import socket
import os
import threading
from tqdm import tqdm

# تنظیمات
CHUNK_SIZE = 1024 * 1024  # اندازه هر بخش
SERVER_IP = ''  # آی‌پی سرور
SERVER_PORT = 5000  # پورت سرور
SAVE_PATH = 'save'  # مسیر ذخیره فایل نهایی
NUM_THREADS = 10  # تعداد تردها برای دریافت موازی

# متغیر سراسری برای پراگرس بار
progress_bar = None

def receive_chunk(conn, filename, start, end):
    global progress_bar
    with open(filename, 'rb+') as f:
        f.seek(start)
        received_data = start
        while received_data < end:
            data = conn.recv(CHUNK_SIZE)
            if not data:
                break
            f.write(data)
            received_data += len(data)
            progress_bar.update(len(data))  # بروزرسانی پراگرس بار

    conn.close()

def receive_file():
    global progress_bar
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((SERVER_IP, SERVER_PORT))
        server_sock.listen(NUM_THREADS)
        print("Waiting for connections...")

        conn, addr = server_sock.accept()
        with conn:
            print(f"Connected by {addr}")

            # دریافت اطلاعات فایل
            file_info = conn.recv(1024).decode()
            filename, file_size, start, end = file_info.split(":")
            file_size, start, end = int(file_size), int(start), int(end)

            # باز کردن فایل برای نوشتن
            save_file_path = os.path.join(SAVE_PATH, filename)
            with open(save_file_path, 'wb') as f:
                f.truncate(file_size)

            # ایجاد پراگرس بار
            progress_bar = tqdm(total=file_size, unit="B", unit_scale=True, desc="Receiving")

            # شروع ترد برای دریافت بخش
            threads = []
            for _ in range(NUM_THREADS):
                thread = threading.Thread(target=receive_chunk, args=(conn, save_file_path, start, end))
                threads.append(thread)
                thread.start()

            # منتظر ماندن برای اتمام همه تردها
            for thread in threads:
                thread.join()

            progress_bar.close()
            print("File received and assembled successfully!")

if __name__ == "__main__":
    receive_file()
