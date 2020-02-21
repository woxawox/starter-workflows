# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')

@bot.message_handler(content_types=["text"])
def start_message(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, "Assalomu alaykum, \"ARMO\" botiga xush kelibsiz!")
    bot.send_message(message.chat.id, "Sizga nima yordam berishim mumkin?", reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)
    bot.infinity_polling(none_stop = True, interval=0)
