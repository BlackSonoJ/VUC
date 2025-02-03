import os


import telebot
from dotenv import load_dotenv


load_dotenv()
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
"""
Обработка старового сообщения + несколько маленьких кнопок
"""

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Галлерея изображений", callback_data="images_start"))
    markup.add(telebot.types.InlineKeyboardButton("Галлерея видео", callback_data="video_start"))
    markup.add(telebot.types.InlineKeyboardButton("🔍 Информация", callback_data="info"), telebot.types.InlineKeyboardButton("❌ Закрыть", callback_data="close"))
    bot.send_message(chat_id=message.chat.id, text='''
Здравия желаю!                     
                     
Данный бот был подготовлен для удобного администрирования информационного киоска ВУЦ БФУ.
                     
Для дальнейшей работы нажмите на кнопки ниже.
                    ''',
                    reply_markup=markup)
    bot.delete_message(message.chat.id, message.message_id)
    

@bot.callback_query_handler(func=lambda call: call.data == "close")
def close_button(call: telebot.types.CallbackQuery):
    bot.delete_message(call.message.chat.id, call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data == "info")
def info_button(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("≪ Назад", callback_data="back_to_start"))
    bot.send_message(chat_id=call.message.chat.id, text="""
Контакты разработчика:
Лигатюк Владимир Дмитривич (ЛН-23)
мобильный телефон: +79052812421
Телеграм: @VLigatiuk
    """, reply_markup=markup)
    bot.delete_message(call.message.chat.id, call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data == "back_to_start")
def start_button(call: telebot.types.CallbackQuery):
    start(call.message)
    bot.delete_message(call.message.chat.id, call.message.message_id)


"""
Обработка запросов на просмотр и редактирование галереи изображений
"""


@bot.callback_query_handler(func=lambda call: call.data == "images_start")
def image_start_button(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Добавить", callback_data="image_upload"), telebot.types.InlineKeyboardButton("Удалить", callback_data="image_delete"))
    markup.add(telebot.types.InlineKeyboardButton("≪ Назад", callback_data="back_to_start"))
    bot.send_message(chat_id=call.message.chat.id, text="""Выберите действие""", reply_markup=markup)
    bot.delete_message(call.message.chat.id, call.message.message_id)


"""
Обработка запросов на просмотр и редактирование галереи видео
"""


@bot.callback_query_handler(func=lambda call: call.data == "videos_start")
def videos_start_button(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Добавить", callback_data="video_upload"), telebot.types.InlineKeyboardButton("Удалить", callback_data="image_delete"))
    markup.add(telebot.types.InlineKeyboardButton("≪ Назад", callback_data="back_to_start"))
    bot.send_message(chat_id=call.message.chat.id, text="""Выберите действие""", reply_markup=markup)
    bot.delete_message(call.message.chat.id, call.message.message_id)



@bot.message_handler(content_types=['photo'])
def photo_id(message):
    for i in range (3, len(message.photo), 4):
        file_id = message.photo[i].file_id
        bot.send_photo(chat_id=message.chat.id, photo=file_id)


def start_bot():
    bot.infinity_polling(skip_pending=True)

if __name__ == '__main__':
    start_bot()