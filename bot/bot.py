"""
Телеграм бот для удобного администрирования инфокиоска
Общение с бд идет через api
С фронтенда идут только get запросы для отрисовки
С бота запросы get, post, put, delete
Подготовил студент ЛН-23, возможность правок после запуска не предусмотрена
Реализация удаления сообщений требует правок, старый формат закомментирован, новый пока не реализован
"""

import os
import requests


import telebot
from dotenv import load_dotenv
import psycopg2


waiting_for_upload = {}
where_to_upload = {}
URLS_API = {  # переписать, чтобы считывалось с http://127.0.0.1:8000/api/
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


@bot.message_handler(commands=["start"])
def start(message):
    """Обработка /start, главное меню"""

    close_upload(message)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Галлерея изображений", callback_data="images_start"
        )
    )
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Галлерея видео", callback_data="videos_start"
        )
    )
    markup.add(
        telebot.types.InlineKeyboardButton("Календарь", callback_data="calendar_start")
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
    """Кнопка закрытия, возможно не требуется"""

    bot.delete_message(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "info")
def info_button(call: telebot.types.CallbackQuery):
    """Информация о приложении и контакты для внесения правок, возможно не требуется"""

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
    """Возврат на стартовую страницу"""
    start(call.message)
    # bot.delete_message(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "images_start")
def image_start_button(call: telebot.types.CallbackQuery):
    """Главная страница по работе с изображениями"""

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
    """Указываем, что следующий поток входных изображений будет сохранен в дб для изображения на главном экране инфокиоска"""

    where_to_upload[call.message.chat.id] = URLS_API["imagesMain"]
    image_upload_button(call)


@bot.callback_query_handler(func=lambda call: call.data == "image_upload_gallery")
def image_upload_gallery_button(call: telebot.types.CallbackQuery):
    """Указываем, что следующий поток входных изображений будет сохранен в дб для изображения в галлереи инфокиоска"""

    where_to_upload[call.message.chat.id] = URLS_API["images"]
    image_upload_button(call)


def image_upload_button(call: telebot.types.CallbackQuery):
    """Открываем поток для обработки изображений, кнопка назад вернет в меню выбора местоположения входящий изображений и закроет поток до следующего запроса"""

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
    waiting_for_upload[call.message.chat.id] = True
    # bot.delete_message(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "videos_start")
def videos_start_button(call: telebot.types.CallbackQuery):
    """Главная страница по работе с видео"""

    close_upload(call.message)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Добавить в видеоматериалов", callback_data="video_upload"
        ),
        telebot.types.InlineKeyboardButton(
            "Удалить из видеоматериалов", callback_data="video_delete"
        ),
    )
    markup.add(
        telebot.types.InlineKeyboardButton("≪ Назад", callback_data="back_to_start")
    )
    bot.send_message(
        chat_id=call.message.chat.id, text="""Выберите действие""", reply_markup=markup
    )
    # bot.delete_message(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "video_upload")
def videos_upload_button(call: telebot.types.CallbackQuery):
    """Открытие потока загрузки видео, по хорошему объединить с открытием потока на видео, но лениво"""

    where_to_upload[call.message.chat.id] = URLS_API["videos"]
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("≪ Назад", callback_data="videos_start")
    )
    bot.send_message(
        chat_id=call.message.chat.id,
        text="""
Отправьте видеоматериалы.
После отправки нажмите "Назад" на этом сообщении, чтобы завершить загрузку.
        """,
        reply_markup=markup,
    )
    waiting_for_upload[call.message.chat.id] = True


@bot.message_handler(content_types=["photo"])
def save_photo(message):
    """Обработка потока входящих изображений в случае открытого потока, иначе не обрабатываем, проверить timeout в requests"""
    if not waiting_for_upload[message.chat.id]:
        return
    file_id = message.photo[-1].file_id
    file_path = bot.get_file(file_id).file_path
    response = requests.get(
        f"https://api.telegram.org/file/bot{API_TOKEN}/{file_path}", timeout=5
    )
    img_data = response.content
    files = {"image": (f"{file_id}.jpg", img_data, "image/jpeg")}
    url = where_to_upload[message.chat.id]
    headers = {"Authorization": f"Bearer {get_api_token()}"}
    response = requests.post(url, files=files, headers=headers, timeout=15)


@bot.message_handler(content_types=["video"])
def save_video(message):
    """Обработка потока входящих видео в случае открытого потока, иначе не обрабатываем, проверить timeout в requests"""
    if not waiting_for_upload[message.chat.id]:
        return
    file_id = message.video.file_id
    file_path = bot.get_file(file_id).file_path
    response = requests.get(
        f"https://api.telegram.org/file/bot{API_TOKEN}/{file_path}", timeout=5
    )
    img_data = response.content
    files = {"video": (f"{file_id}.mp4", img_data, "video/mp4")}
    url = where_to_upload[message.chat.id]
    headers = {"Authorization": f"Bearer {get_api_token()}"}
    response = requests.post(url, files=files, headers=headers, timeout=15)


def close_upload(message):
    """Закрываем поток загрузки"""

    where_to_upload.setdefault(message.chat.id, "")
    if waiting_for_upload.setdefault(message.chat.id, False):
        waiting_for_upload[message.chat.id] = False


def get_api_token():
    """Получаем токен api для запросов, требующих аутентификацию"""

    username = os.getenv("API_USER")
    password = os.getenv("API_PASSWORD")
    token_request = requests.post(
        "http://127.0.0.1:8000/api/token/",
        data={"username": username, "password": password},
        timeout=5,
    )
    token_data = token_request.json()
    return token_data.get("access")


def start_bot():
    """Запускаем бота, по хорошему нужно добавить threads, но в данной реализации нет необходимости"""

    bot.infinity_polling(skip_pending=True)


if __name__ == "__main__":
    start_bot()
