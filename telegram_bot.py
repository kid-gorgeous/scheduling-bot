import telebot
from config import telegram_token as T_TOKEN

telegram_bot = telebot.TeleBot(T_TOKEN)

@telegram_bot.message_handler(commands=['start'])
def start_bot(message):
    telegram_bot.send_message(message.chat.id,"Welcome to the Halo-Chat bot! 🤖\n\nThis bot will help organize your week!\n\nType /help to see all the commands.")
    print("User connected")

telegram_bot.polling()