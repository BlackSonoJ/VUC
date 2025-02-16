"""
Файл появился после рефакторинга
по хорошему поля хранить в бд, а не в оперативке, но это дольше и мне поебать
"""

import functools
import requests

import telebot


class Paginator:
    """Просмотр галлереи файлов"""

    def __init__(self, urls_api):
        self.content_type = {}
        self.page = {}
        self.urls_api = urls_api

    def paginator(self, arg):
        """Декоратор c аргументами"""

        def _decorator(func):

            @functools.wraps(func)
            def _wrapper(*args, **kwargs):
                chat_id = None
                if isinstance(args[0], telebot.types.CallbackQuery):
                    chat_id = args[0].message.chat.id
                elif isinstance(args[0], telebot.types.Message):
                    chat_id = args[0].chat.id

                if arg == "create":
                    if self.page.setdefault(chat_id, 0):
                        self.page[chat_id] = 0
                elif arg == "previous":
                    if self.page[chat_id] > 0:
                        self.page[chat_id] -= 1
                    else:
                        self.page[chat_id] = self.get_media_array_len(chat_id) - 1

                elif arg == "next":
                    if self.page[chat_id] < self.get_media_array_len(chat_id) - 1:
                        self.page[chat_id] += 1
                    else:
                        self.page[chat_id] = 0

                return func(*args, **kwargs)

            return _wrapper

        return _decorator

    def get_media_raw(self, chat_id):
        """возвращает файл из апи, запрашиваемый пользователем, тип не присвоен, поэтому и raw"""
        response = requests.get(
            url=self.urls_api[self.content_type[chat_id]], timeout=5
        )
        media_url = response.json()[self.page[chat_id]][self.content_type[chat_id][:5]]
        response = requests.get(media_url, timeout=5)
        return response.content

    def get_media(self, chat_id):
        """возвращает файл из апи, запрашиваемый пользователем, теперь с типом"""
        content = self.get_media_raw(chat_id)
        if self.content_type[chat_id][:5] == "image":
            return telebot.types.InputMediaPhoto(media=content)
        else:
            return telebot.types.InputMediaVideo(media=content)

    def get_media_id(self, chat_id):
        """возвращает айди файла из апи, запрашиваемого пользователем"""
        response = requests.get(
            url=self.urls_api[self.content_type[chat_id]], timeout=5
        )
        return response.json()[self.page[chat_id]]["id"]

    def get_media_array_len(self, chat_id):
        """возвращает длину массива файлов из апи, запрашиваемого пользователем"""
        response = requests.get(
            url=self.urls_api[self.content_type[chat_id]], timeout=5
        )
        return len(response.json())

    def markup(self, chat_id, formatter):
        """Универсально возвращаем маркап (кнопочки под сообщением)"""
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(
            telebot.types.InlineKeyboardButton("≪", callback_data="previous"),
            telebot.types.InlineKeyboardButton("≫", callback_data="next"),
        )
        markup.add(
            telebot.types.InlineKeyboardButton(
                "Удалить", callback_data="delete_current"
            )
        )
        markup.add(
            telebot.types.InlineKeyboardButton(
                "≪ Назад", callback_data=f"{self.content_type[chat_id]}_{formatter}"
            )
        )
        return markup

    def add_content_type(self, content_type):
        """Объявляем тип контента для загрузки"""

        def _decorator(func):
            @functools.wraps(func)
            def _wrapper(*args, **kwargs):
                if isinstance(args[0], telebot.types.CallbackQuery):
                    chat_id = args[0].message.chat.id
                elif isinstance(args[0], telebot.types.Message):
                    chat_id = args[0].chat.id
                else:
                    chat_id = None
                if self.content_type.setdefault(chat_id, content_type):
                    self.content_type[chat_id] = content_type
                return func(*args, **kwargs)

            return _wrapper

        return _decorator
