"""
Телеграм бот для удобного администрирования инфокиоска
Общение с бд идет через api
С фронтенда идут только get запросы для отрисовки
С бота запросы get, post, put, delete
Подготовил студент ЛН-23, возможность правок после запуска не предусмотрена
Реализация удаления сообщений требует правок, старый формат закомментирован,
новый пока не реализован
Клонируешь реп https://github.com/BlackSonoJ/VUC.git и потом жестко кайфуешь
Ищи помощи, нас тут было двое, один на backend и бота, второй на front
Ну или ты слишлом крутой для этого?
версия после рефакторинга
"""

import os
import requests


import telebot
from dotenv import load_dotenv

from uploader import Uploader
from paginator import Paginator


load_dotenv()


def content_type_urls():
    """Получаем с API типы контента и соответствующие URL"""
    return requests.get(os.getenv("API_URL"), timeout=5).json()


API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
API_URLS = content_type_urls()
uploader = Uploader(API_URLS)
paginator = Paginator(API_URLS)


@bot.message_handler(commands=["start"])
def start(message):
    """Обработка /start, главное меню"""

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(
            "📷 Галлерея изображений", callback_data="images_start"
        )
    )
    markup.add(
        telebot.types.InlineKeyboardButton(
            "📷 Изображения на главной", callback_data="imagesMain_start"
        )
    )
    markup.add(
        telebot.types.InlineKeyboardButton(
            "🎥 Галлерея видео", callback_data="videos_start"
        )
    )
    markup.add(
        telebot.types.InlineKeyboardButton(
            "🗓️ Календарь", callback_data="calendar_start"
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


@bot.callback_query_handler(func=lambda call: call.data == "back_to_start")
def start_button(call: telebot.types.CallbackQuery):
    """Возврат на стартовую страницу"""
    start(call.message)


@bot.callback_query_handler(func=lambda call: call.data == "images_start")
@uploader.close_upload
@uploader.add_content_type("images")
@paginator.add_content_type("images")
def image_start_button(call: telebot.types.CallbackQuery):
    """Главная страница по работе с галереей"""

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Добавить в галерею", callback_data="upload"
        ),
    )
    markup.add(
        telebot.types.InlineKeyboardButton("Удалить из галереи", callback_data="edit"),
    )
    markup.add(
        telebot.types.InlineKeyboardButton("≪ Назад", callback_data="back_to_start")
    )
    bot.send_message(
        chat_id=call.message.chat.id, text="""Выберите действие""", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "imagesMain_start")
@uploader.close_upload
@uploader.add_content_type("imagesMain")
@paginator.add_content_type("imagesMain")
def images_main_start_button(call: telebot.types.CallbackQuery):
    """Главная страница по работе с изображениями на главной"""

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Добавить на главную", callback_data="upload"
        ),
    )
    markup.add(
        telebot.types.InlineKeyboardButton("Удалить c главной", callback_data="edit"),
    )
    markup.add(
        telebot.types.InlineKeyboardButton("≪ Назад", callback_data="back_to_start")
    )
    bot.send_message(
        chat_id=call.message.chat.id, text="""Выберите действие""", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "videos_start")
@uploader.close_upload
@uploader.add_content_type("videos")
@paginator.add_content_type("videos")
def videos_start_button(call: telebot.types.CallbackQuery):
    """Главная страница по работе с изображениями на главной"""

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Добавить в видеоматериалы", callback_data="upload"
        ),
    )
    markup.add(
        telebot.types.InlineKeyboardButton(
            "Удалить из видеоматериалов", callback_data="edit"
        ),
    )
    markup.add(
        telebot.types.InlineKeyboardButton("≪ Назад", callback_data="back_to_start")
    )
    bot.send_message(
        chat_id=call.message.chat.id, text="""Выберите действие""", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "edit")
@paginator.paginator("create")
def image_edit_main_button(call: telebot.types.CallbackQuery):
    """Отрисовка первой страницы"""
    bot.send_photo(  # почему-то оно отправляет и видео, очень удобно
        call.message.chat.id,
        paginator.get_media_raw(call.message.chat.id),
        reply_markup=paginator.markup(call.message.chat.id, "start"),
    )


@bot.callback_query_handler(func=lambda call: call.data == "previous")
@paginator.paginator("previous")
def previous_button(call: telebot.types.CallbackQuery):
    """Отрисовка предыдущей страницы"""

    bot.edit_message_media(
        media=paginator.get_media(call.message.chat.id),
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=paginator.markup(
            call.message.chat.id,
            "start",
        ),
    )


@bot.callback_query_handler(func=lambda call: call.data == "next")
@paginator.paginator("next")
def next_button(call: telebot.types.CallbackQuery):
    """Отрисовка следующей страницы"""
    bot.edit_message_media(
        media=paginator.get_media(call.message.chat.id),
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=paginator.markup(
            call.message.chat.id,
            "start",
        ),
    )


@bot.callback_query_handler(func=lambda call: call.data == "upload")
@uploader.open_upload
def upload(call: telebot.types.CallbackQuery):
    """Загрузка видео/фото, открываем поток"""
    bot.send_message(
        chat_id=call.message.chat.id,
        text="""
Отправьте материал(ы).
После отправки нажмите "Назад" на этом сообщении, чтобы завершить загрузку.
        """,
        reply_markup=uploader.markup(call.message.chat.id, "start"),
    )


@bot.message_handler(content_types=["video", "photo"])
def save_media(message):
    """Сохраняем видео и фото как боженьки"""
    if not uploader.status[message.chat.id]:
        return
    if uploader.content_type[message.chat.id][:5] == "image":
        file_id = message.photo[-1].file_id
        file_path = bot.get_file(file_id).file_path
        response = requests.get(
            f"https://api.telegram.org/file/bot{API_TOKEN}/{file_path}", timeout=5
        )
        img_data = response.content
        files = {"image": (f"{file_id}.jpg", img_data, "image/jpeg")}
    else:
        file_id = message.video.file_id
        file_path = bot.get_file(file_id).file_path
        response = requests.get(
            f"https://api.telegram.org/file/bot{API_TOKEN}/{file_path}", timeout=5
        )
        video_data = response.content
        files = {"video": (f"{file_id}.mp4", video_data, "video/mp4")}
    url = uploader.urls_api[uploader.content_type[message.chat.id]]
    headers = {"Authorization": f"Bearer {get_api_token()}"}
    response = requests.post(url, files=files, headers=headers, timeout=15)


def get_api_token():
    """Получаем токен api для запросов, требующих аутентификацию"""

    token_request = requests.post(
        f"{os.getenv("API_URL")}token/",
        data={"username": os.getenv("API_USER"), "password": os.getenv("API_PASSWORD")},
        timeout=5,
    )
    token_data = token_request.json()
    return token_data.get("access")


def start_bot():
    """Запускаем бота, по хорошему нужно добавить threads, но в данной реализации нет необходимости"""

    bot.infinity_polling(skip_pending=True)


if __name__ == "__main__":
    start_bot()
