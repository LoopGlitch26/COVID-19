from bot import telegram_chatbot
import requests
import telebot
from bs4 import BeautifulSoup
from telebot import types
import time

bot = telegram_chatbot("config.cfg")

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    bot.send_message(msg.chat.id,'Welcome! I am LoopGlitch1 bot to get Covid 19 updates,\n Use /covid to get world Covid 19 updates, \n Use /covidIndia to get India Covid 19 updates')

@bot.message_handler(commands=['covid'])
def covid_handler(message):    
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, "retriving data...")
    a=requests.get('https://www.worldometers.info/coronavirus/')
    b=BeautifulSoup(a.text,'html.parser')
    title=b.find_all("div",class_='maincounter-number')
    c =f"Total Case : {title[0].text.strip()}\n Total Deaths : {title[1].text.strip()}\n Total Recoverd : {title[2].text.strip()}"
    bot.send_chat_action(message.chat.id,'typing')
    bot.send_message(message.chat.id,c)
	
@bot.message_handler(commands=['covidIndia'])
def covid_handler(message):    
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, "retriving data...")
    a=requests.get('https://www.worldometers.info/coronavirus/country/india/')
    b=BeautifulSoup(a.text,'html.parser')
    title=b.find_all("div",class_='maincounter-number')
    c =f"Total Case : {title[0].text.strip()}\n Total Deaths : {title[1].text.strip()}\n Total Recoverd : {title[2].text.strip()}"
    bot.send_chat_action(message.chat.id,'typing')
    bot.send_message(message.chat.id,c)
	
while True:
	try:
		bot.polling(True)
	except Exception:
		time.sleep(10)