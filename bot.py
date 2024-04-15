import telebot
import config
import messages, code
from telebot import types


bot = telebot.TeleBot(config.tg_token, parse_mode='html')


@bot.message_handler(commands=['start'])
def func_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    bot.send_message(message.chat.id, messages.msg['start'], reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def func_text(message):
    if code.get_name(message.text) == {}:
        bot.send_message(message.chat.id, 'Введите и имя, и фамилию.')
    else:
        name = code.get_name(message.text)['name']
        surname = code.get_name(message.text)['surname']
        id_output(message, name, surname)


def id_output(message, name, surname):
    chgk_id = code.get_id(name, surname)
    if chgk_id == 0:
        bot.send_message(message.chat.id, 'Игрок не найден')
    else:
        output = f'''Ваш ID: {chgk_id}'''
        bot.send_message(message.chat.id, output)
        bot.send_message(message.chat.id, messages.msg['next'])


bot.polling(non_stop=True)
