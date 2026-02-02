import subprocess
import sys
import os

def main():
    # PyInstaller 解包路径
    base_dir = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    app_path = os.path.join(base_dir, "app.py")

    # 防止 PyInstaller 子进程重复执行
    if os.environ.get("STREAMLIT_LAUNCHED") == "1":
        return
    os.environ["STREAMLIT_LAUNCHED"] = "1"

    subprocess.Popen(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            app_path,

            # ======= 关键参数 =======
            "--server.headless=true",
            "--server.runOnSave=false",
            "--server.fileWatcherType=none",
            "--browser.gatherUsageStats=false",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )

if __name__ == "__main__":
    main()
