from pyautogui import moveTo,click,screenshot # Подключения из библиотеки функций движения мыши, клика, и создания скриншота
from keyboard import press,release #Подключения функций зажатия и отпускания клавиши клавиатуры
from sys import exit #функция выхода
from time import sleep #функция задержки
from python_imagesearch.imagesearch import imagesearcharea #Поиск в определенной области
from win32gui import GetWindowText, GetForegroundWindow #Получение названия окна
import threading #Многопоточность
import telebot #Bot API Telegram

window = "MatHax v1.7.6 - modified/Fabric 1.18.1" #Название окна игры

bot = telebot.TeleBot("token") #Вместо token ваш токен от бота
chat_id = "@chatid" #ID чата куда кидать покупки
user = "thede" #Имя вашего пользователя 

def screen():
	sleep(1) #Ожидание 1 сек.
	f = open(f'C:/Users/{user}/AppData/Roaming/.minecraft/logs/latest.log','r+') #Открытие логов
	lines = f.readlines() #Чтение логов
	f.close() #Закрытие логов
	lens = len(lines) #Получения количества строк
	item = "" #Создания переменной для предмета который купили
	while True: #Бесконечный цикл
		fined = lines[lens-1] #Получение с последней до первой строки логов 
		if "Этот товар уже купили!" in fined or "У Вас не хватает денег!" in fined: #Проверка 
			break #Окончить цикл
		if "Вы успешно купили" in fined: #Если есть уведомление о покупке
			item = fined.split("купили")[1].replace("\n","")[1:] #Получить название того, что купили
			break #Окончание цикла
		lens -= 1 #переход к предыдущей строке 
 
	if item != "": #Если предмет есть то
		print(f"Купил {item}") #Отладка
		bot.send_photo(chat_id,screensh,f"Купил {item}") #Отправка скриншота в чат с названием того что купили


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

#Бесконечный цикл 
while True:
	try:
		#Проверка на текущее окно
		if GetWindowText(GetForegroundWindow()) == window:
			i = 1132 #Начальная координата клетки по горизонтали
			g = 0 #Номер ячейки
			press("shift") #Зажимание шифта, так быстрее покупает, не нужно подтверджать
			while g != 6:
				#Проверка какое сейчас окно и если оно игра, то запускаем
				if GetWindowText(GetForegroundWindow()) == window:
					#передвижение на клетку
					moveTo(i,538)
					#Ищем в области по координатам совпадение с шаблоном
					pos = imagesearcharea("./1.png",1112,554,1503,731)
					#если совпадения есть
					if pos[0] != -1:
						#Создаем глобальную переменную со скриншотом инвентаря
						global screensh
						screensh = screenshot('screenshot.png',region=(1110,510,500,500))
						#Кликаем по предмету
						click()
						#Запускаем поток с отправкой уведомления
						threading.Thread(target = screen).start()
					#Добавляем координату по горизонтали, и меняем номер клетки
					i += 37
					g += 1
				else:
					#Если окно не игра, отпускаем на всякий случай шифт(Были случаи зажима) и выходим из скрипта
					release("shift")
					exit()

			moveTo(1277,716)#Передвигаемся на кнопку обновления
			release("shift")#Отжимаем шифт(Так надо, в ином случае создаст проблемы)
			click()#Кликаем

		else:
			#Та же проверка на текущее окна, с шифтом и выходом
			release("shift")
			exit()
	#Если нажато CTRL+C			
	except KeyboardInterrupt:
		#Та же проверка на текущее окна, с шифтом и выходом
		release("shift")
		exit()


