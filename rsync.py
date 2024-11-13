import subprocess
import os

# تنظیمات
SERVER_IP = ''  # آدرس سرور
SERVER_USERNAME = ''  # نام کاربری در سرور
SERVER_PATH = './save'  # مسیر مقصد در سرور
FILE_PATH = ''  # مسیر فایل اصلی

def transfer_with_rsync():
    # اطمینان از وجود فایل
    if not os.path.isfile(FILE_PATH):
        print("File does not exist.")
        return

    # دستور rsync برای انتقال فایل
    command = [
        "rsync",
        "-avP",  # 'a' برای آرشیو کردن و 'P' برای نمایش پیشرفت و از سرگیری
        FILE_PATH,
        f"{SERVER_USERNAME}@{SERVER_IP}:{SERVER_PATH}"
    ]

    # اجرای دستور rsync
    try:
        subprocess.run(command, check=True)
        print("File transferred successfully!")
    except subprocess.CalledProcessError as e:
        print("An error occurred while transferring the file:", e)

if __name__ == "__main__":
    transfer_with_rsync()
