from time import sleep
from sys import exit
from win32gui import GetWindowText, GetForegroundWindow
from item_purchase import purchase_items
from window_monitor import monitor_window

window = "MatHax v1.7.6 - modified/Fabric 1.18.1"

# Цикл, ожидающий открытия игры
monitor_window(window)

try:
    # Основной цикл выполнения
    while True:
        if GetWindowText(GetForegroundWindow()) == window:
            purchase_items(window)
        else:
            exit()
except KeyboardInterrupt:
    exit()
