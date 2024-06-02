import telebot

bot = telebot.TeleBot("your_token_here")
chat_id = "@your_chat_id_here"

def send_purchase_notification(item):
    """Отправка уведомления о покупке в Telegram"""
    global screensh
    bot.send_photo(chat_id, screensh, f"Купил {item}")
