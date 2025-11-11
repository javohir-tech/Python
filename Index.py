from transliterate import to_cyrillic , to_latin;
from dotenv import load_dotenv

import telebot
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN , parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message , "Assalom Aleykum")
    
@bot.message_handler(func = lambda m : True )
def echo_all(message):
    msg = message.text
    javob = lambda x : to_cyrillic(x) if msg.isascii() else to_latin(x)
    bot.reply_to(message , javob(msg))
    


bot.polling()
