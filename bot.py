import config
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import sqlite3
import datetime
que = []
answ = []
bot = telebot.TeleBot(config.API_TOKEN)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Получить на вопрос ответ", callback_data="cb_yes"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        con = sqlite3.connect("dvd.db") # соединение с базой данных, если бд нет, то файл создастся
        cur = con.cursor()
        cur.executemany("""
            SELECT ques from dvd AND SELECT answ from dvd """)


#reply_markup=gen_markup()



@bot.message_handler(commands = ['help'])
def moai(message):
    
    bot.send_message(message.chat.id ,"Здравстуйте администратор! Что бы найти вас интересующий ответ на ваш вопрос заданный пользователем напишите что нибудь в чат")
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text.lower() == "что нибудь":
        bot.send_message(message.chat.id, 'Оригинално -_-... Так вот, чтобы найти ответ на вопрос нажмите на кнопку "Показать вопросы". Вам вышлется все вопросы и ответы в моей базе данных',reply_markup=gen_markup())
    else:
        bot.send_message(message.chat.id, 'Так вот, чтобы найти ответ на вопрос нажмите на кнопку "Показать вопросы". Вам вышлется все вопросы и ответы в моей базе данных',reply_markup=gen_markup())
bot.infinity_polling()