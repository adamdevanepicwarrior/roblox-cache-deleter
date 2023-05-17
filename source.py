import psutil
import time

def watch_process(name):
    while True:
        time.sleep(1)
        try:
            process = psutil.Process(name)
        except psutil.NoSuchProcess:
            folder = os.path.join(os.environ["temp"], "Roblox")
            if os.path.exists(folder):
                print("cache deleted successfully")
                os.rmdir(folder)
            break

if __name__ == "__main__":
    name = "RobloxPlayerLauncher.exe"
    watch_process(name)
