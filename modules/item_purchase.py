from pyautogui import moveTo, click, screenshot
from keyboard import press, release
from time import sleep
from python_imagesearch.imagesearch import imagesearcharea
import threading
from modules.telegram_bot import send_purchase_notification
from win32gui import GetWindowText, GetForegroundWindow

def screen(user):
    """Функция для обработки логов и отправки уведомлений о покупке"""
    sleep(1)
    with open(f'C:/Users/{user}/AppData/Roaming/.minecraft/logs/latest.log', 'r+') as f:
        lines = f.readlines()
    lens = len(lines)
    item = ""
    while True:
        fined = lines[lens - 1]
        if "Этот товар уже купили!" in fined or "У Вас не хватает денег!" in fined:
            break
        if "Вы успешно купили" in fined:
            item = fined.split("купили")[1].replace("\n", "")[1:]
            break
        lens -= 1

    if item:
        print(f"Купил {item}")
        send_purchase_notification(item)

def purchase_items(window):
    """Функция для автоматической покупки предметов в игре"""
    i = 1132
    g = 0
    press("shift")
    while g != 6:
        if GetWindowText(GetForegroundWindow()) == window:
            moveTo(i, 538)
            pos = imagesearcharea("./1.png", 1112, 554, 1503, 731)
            if pos[0] != -1:
                global screensh
                screensh = screenshot('screenshot.png', region=(1110, 510, 500, 500))
                click()
                threading.Thread(target=screen, args=("thede",)).start()
            i += 37
            g += 1
        else:
            release("shift")
            exit()
    moveTo(1277, 716)
    release("shift")
    click()
