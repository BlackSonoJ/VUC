import os
import datetime
import requests
from io import BytesIO


import telebot
from dotenv import load_dotenv
import psycopg2
from PIL import Image

waiting_for_image_upload = {}
where_to_upload = {}
URLS_API = {
    "images": "http://127.0.0.1:8000/api/images/",
    "imagesMain": "http://127.0.0.1:8000/api/imagesMain/",
    "videos": "http://127.0.0.1:8000/api/videos/",
    "events": "http://127.0.0.1:8000/api/events/",
}
load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

db = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

"""
Обработка старового сообщения + несколько маленьких кнопок
"""


@bot.message_handler(commands=["start"])
def start(message):
    close_upload(message)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Галлерея изображений", callback_data="images_start"
        )
    )
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Галлерея видео", callback_data="video_start"
        )
    )
    markup.add(
        telebot.types.InlineKeyboardButton("🔍 Информация", callback_data="info"),
        telebot.types.InlineKeyboardButton("❌ Закрыть", callback_data="close"),
    )
    bot.send_message(
        chat_id=message.chat.id,
        text="""
Здравия желаю!                     
                     
Данный бот был подготовлен для удобного администрирования информационного киоска ВУЦ БФУ.
                     
Для дальнейшей работы нажмите на кнопки ниже.
                    """,
        reply_markup=markup,
    )
    # bot.delete_message(message.chat.id, message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "close")
def close_button(call: telebot.types.CallbackQuery):
    bot.delete_message(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "info")
def info_button(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("≪ Назад", callback_data="back_to_start")
    )
    bot.send_message(
        chat_id=call.message.chat.id,
        text="""
Контакты разработчика:
Лигатюк Владимир Дмитривич (ЛН-23)
мобильный телефон: +79052812421
Телеграм: @VLigatiuk
    """,
        reply_markup=markup,
    )
    # bot.delete_message(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "back_to_start")
def start_button(call: telebot.types.CallbackQuery):
    start(call.message)
    # bot.delete_message(call.message.chat.id, call.message.message_id)


"""
Обработка запросов на просмотр и редактирование галереи изображений
"""


@bot.callback_query_handler(func=lambda call: call.data == "images_start")
def image_start_button(call: telebot.types.CallbackQuery):
    close_upload(call.message)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Добавить на главный экран", callback_data="image_upload_main"
        ),
    )
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Добавить в галерею", callback_data="image_upload_gallery"
        ),
    )
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Удалить c главного экрана", callback_data="image_delete_main"
        ),
    )
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Удалить из галереи", callback_data="image_delete_gallery"
        ),
    )
    markup.add(
        telebot.types.InlineKeyboardButton("≪ Назад", callback_data="back_to_start")
    )
    bot.send_message(
        chat_id=call.message.chat.id, text="""Выберите действие""", reply_markup=markup
    )
    # bot.delete_message(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "image_upload_main")
def image_upload_main_button(call: telebot.types.CallbackQuery):
    where_to_upload[call.message.chat.id] = URLS_API["imagesMain"]
    image_upload_button(call)


@bot.callback_query_handler(func=lambda call: call.data == "image_upload_gallery")
def image_upload_gallery_button(call: telebot.types.CallbackQuery):
    where_to_upload[call.message.chat.id] = URLS_API["images"]
    image_upload_button(call)


def image_upload_button(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("≪ Назад", callback_data="images_start")
    )
    bot.send_message(
        chat_id=call.message.chat.id,
        text="""
Отправьте изображения.
После отправки нажмите "Назад" на этом сообщении, чтобы завершить загрузку.
        """,
        reply_markup=markup,
    )
    waiting_for_image_upload[call.message.chat.id] = True
    # bot.delete_message(call.message.chat.id, call.message.message_id)


"""
Обработка запросов на просмотр и редактирование галереи видео
"""


@bot.callback_query_handler(func=lambda call: call.data == "videos_start")
def videos_start_button(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Добавить на главный экран", callback_data="video_upload_main"
        ),
        telebot.types.InlineKeyboardButton(
            "Добавить в галерею", callback_data="video_upload"
        ),
        telebot.types.InlineKeyboardButton(
            "Удалить из галереи", callback_data="video_delete"
        ),
    )
    markup.add(
        telebot.types.InlineKeyboardButton("≪ Назад", callback_data="back_to_start")
    )
    bot.send_message(
        chat_id=call.message.chat.id, text="""Выберите действие""", reply_markup=markup
    )
    # bot.delete_message(call.message.chat.id, call.message.message_id)


@bot.message_handler(content_types=["photo"])
def save_photo(message):
    if not waiting_for_image_upload[message.chat.id]:
        return
    file_id = message.photo[-1].file_id
    file_path = bot.get_file(file_id).file_path
    response = requests.get(f"https://api.telegram.org/file/bot{API_TOKEN}/{file_path}")
    img_data = response.content
    files = {"image": ("{0}.jpg".format(file_id), img_data, "image/jpeg")}
    url = where_to_upload[message.chat.id]
    username = os.getenv("API_USER")
    password = os.getenv("API_PASSWORD")
    requests.post(url, files=files, auth=(username, password))


def close_upload(message):
    where_to_upload.setdefault(message.chat.id, "")
    if waiting_for_image_upload.setdefault(message.chat.id, False):
        waiting_for_image_upload[message.chat.id] = False


def start_bot():
    bot.infinity_polling(skip_pending=True)


if __name__ == "__main__":
    start_bot()
