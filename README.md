# autobuy_python
---
Скрипт автопокупки с помощью машинного зрения предметов (Да, майнкрафт, и что?)  
***  
Пример(старый, в новой версии намного быстрее)  


https://user-images.githubusercontent.com/40400854/180625937-9357a3e5-080d-43da-863e-a5c03c971c7f.mp4  
____
Для работы необходим Python3.* и несколько пакетов:  
```bat
pip3 install pyautogui  
pip3 install keyboard  
pip3 install time  
pip3 install python_imagesearch  
pip3 install win32gui  
pip3 install threading
pip3 install pyscreeze
````  
____  
  
В коде есть координаты, они заданы по параметрам:  
`1. Игра в оконном режиме.`  
`2. Интерфейс игры стоит 2(средний)`  
`3. Размеры экрана 2560x1440.`  
Чтоб задать свои координаты, создайте пустой скрипт и напишите в нем:  
```python  
  import pyautogui  
  
  while True:  
    print(pyautogui.position())  
```  
И найдите местоположение ваших элементов и поставьте их вместо стандартных.

