from transliterate import to_cyrillic , to_latin
from dotenv import load_dotenv
import os
import telebot

load_dotenv()



TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalom Aleykum")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    xabar = message.text;
    javob = lambda x : to_cyrillic(x) if x.isascii() else to_latin(x)
    bot.reply_to(message , javob(xabar))

bot.polling()