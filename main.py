from pyautogui import moveTo,click #Импортируем из библиотеки мыши функцию клика и движения
from keyboard import press,release #Из библиотеки управления клавиатурой импортируем нажатие и отпускание клавиши
from sys import exit #Импортируем системную либу для функции выхода
from time import sleep #Из библиотеки времени импортируем функию ожидания
from python_imagesearch.imagesearch import imagesearch #Из библиотеки машинного зрения импортируем функцию поиска по шаблону
from win32gui import GetWindowText, GetForegroundWindow #Из библиотеки UI Windows импортируем функции имени окна

#Задаем название окна
window = "MatHax v1.7.6 - modified/Fabric 1.18.1"

#Цикл, ожидающий открытия игры
while True:
	if GetWindowText(GetForegroundWindow()) != window:
		sleep(1)
	else:
		break
#Функция АнтиАФК, мне она не пригодилась, но всё равно оставил
def antiafk():
	#Перебираем массив с клавишами движения
	for i in ["w","s","a","d","up","down"]:
		#Нажимаем кнопку
		press(i)
		#Ждём
		sleep(0.1)
		#Отпускаем
		release(i)
#Главный цикл
while True:
	try:	#Проверка окна 
		if GetWindowText(GetForegroundWindow()) == window:
			i = 821 #Начальная координата клетки по горизонтали
			g = 0 #Номер клетки
			press("shift") #Зажимание шифта, так быстрее покупает, не нужно подтверджать
			# 7 - Количество проверяемых ячеек
			while g != 7:
				#Проверка какое сейчас окно и если оно игра, то запускаем
				if GetWindowText(GetForegroundWindow()) == window:
					#передвижение на клетку
					moveTo(i,352)
					#Ищем на экране совпадение с шаблоном
					pos = imagesearch("./1.png")
					#если совпадения есть
					if pos[0] != -1:
						#Уведомляем и покупаем
						print("Вижу предмет за 10$ : ", pos[0], pos[1])
						click()
					#Добавляем координату по горизонтали, и меняем номер клетки
					i += 35
					g += 1
				else:
					#Если окно не игра, отпускаем на всякий случай шифт(Были случаи зажима) и выходим из скрипта
					release("shift")
					exit()
			#Передвигаемся на кнопку обновления
			moveTo(963,535)
			#Отжимаем шифт(Так надо, в ином случае созда			
			release("shift")
			#Кликаем
			click()
		else:
			#Та же проверка на текущее окна, с шифтом и выходом
			release("shift")
			exit()
	#Если нажато CTRL+C
	except KeyboardInterrupt:
		#Отжимаем шифт и выходим
		release("shift")
		exit()


