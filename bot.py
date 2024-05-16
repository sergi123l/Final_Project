import config
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import sqlite3
import datetime
import time
que = []

bot = telebot.TeleBot(config.API_TOKEN)

# def gen_markup():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 2
#     markup.add(InlineKeyboardButton("Получить на вопрос ответ", callback_data="cb_yes"))
#     return markup

# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     if call.data == "cb_yes":
#         con = sqlite3.connect("dvd.db") # соединение с базой данных, если бд нет, то файл создастся
#         cur = con.cursor()
#         cur.executemany("""
#             SELECT ques from quest""")
#         res = cur.fetchall()
#         bot.send_message(call.message.chat.id , "вот вопросы напишите один из них и получите ответ")


#reply_markup=gen_markup()



@bot.message_handler(commands = ['help'])
def moai(message):
    bot.send_message(message.chat.id ,"Здравстуйте администратор! Что бы найти вас интересующий ответ на ваш вопрос заданный пользователем напишите что нибудь в чат")





@bot.message_handler(func=lambda message: True)
def echo_message(message):

    # if message.text.lower() == "что нибудь":
    #     bot.send_message(message.chat.id, 'Оригинално -_-... Так вот, чтобы найти ответ на вопрос нажмите на кнопку "Показать вопросы". Вам вышлется все вопросы и ответы в моей базе данных',reply_markup=gen_markup())
    # else:
    #     bot.send_message(message.chat.id, 'Так вот, чтобы найти ответ на вопрос нажмите на кнопку "Показать вопросы". Вам вышлется все вопросы и ответы в моей базе данных',reply_markup=gen_markup())
    con = sqlite3.connect("dvd.db") # соединение с базой данных, если бд нет, то файл создастся
    cur = con.cursor()
    cur.execute("""
    SELECT answ from quest WHERE ques = ?""",(message.text.lower(),))
    res = cur.fetchone()
    if res :
        bot.send_message(message.chat.id,res[0])
    else :
        bot.send_message(message.chat.id,"Такого вопроса нет в базе:( примите наши извинения спишитесь с создателем базы данным и выдайте ему трески жареной и скажите чтоб добавил вопрос")
    con.close()

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        time.sleep(15)