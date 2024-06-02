from keyboard import press, release
from time import sleep

def antiafk():
    """Функция для предотвращения AFK в игре"""
    for key in ["w", "s", "a", "d", "up", "down"]:
        press(key)
        sleep(0.1)
        release(key)
