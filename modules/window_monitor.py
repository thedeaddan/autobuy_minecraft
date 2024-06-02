from time import sleep
from win32gui import GetWindowText, GetForegroundWindow

def monitor_window(window_name):
    """Мониторинг окна игры"""
    while True:
        if GetWindowText(GetForegroundWindow()) != window_name:
            sleep(1)
        else:
            break
