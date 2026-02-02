import subprocess
import threading
import time
import webview
import socket
import sys
import os

def is_port_open(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(("127.0.0.1", port))
        s.close()
        return True
    except:
        return False

def run_streamlit():
    app_path = os.path.join(os.path.dirname(sys.executable), "app.py")
    subprocess.Popen([
        sys.executable,
        "-m", "streamlit",
        "run",
        app_path,
        "--server.headless=true",
        "--server.port=8501"
    ])

if __name__ == "__main__":
    if not is_port_open(8501):
        t = threading.Thread(target=run_streamlit, daemon=True)
        t.start()
        time.sleep(2)

    webview.create_window(
        "多品种交易风控与研究系统",
        "http://localhost:8501",
        width=1280,
        height=800
    )
    webview.start()