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
    name_info = code.get_name(message.text)
    if not name_info:
        bot.send_message(message.chat.id, messages.msg['not_enough_info'])
    name, surname = name_info['name'], name_info['surname']
    id_output(message, name, surname)


def id_output(message, name, surname):
    chgk_id = code.get_id(name, surname)
    if not chgk_id:
        bot.send_message(message.chat.id, messages.msg['unfound'])
    elif len(chgk_id) > 1:
        bot.send_message(message.chat.id, messages.msg['more_than_one'])
        for i in chgk_id:
            bot.send_message(message.chat.id, i)
        bot.send_message(message.chat.id, messages.msg['next'])
    else:
        bot.send_message(message.chat.id, chgk_id[0])
        bot.send_message(message.chat.id, messages.msg['next'])


bot.polling(non_stop=True)
