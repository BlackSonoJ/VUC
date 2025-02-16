import functools

import telebot


class Uploader:
    """Удобно храним всё, что связанно с загрузкой в бд"""

    def __init__(self, urls_api):
        self.content_type = {}
        self.status = {}
        self.urls_api = urls_api

    def close_upload(self, func):
        """Декоратор, заткрывает поток загрузки"""

        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            if isinstance(args[0], telebot.types.CallbackQuery):
                chat_id = args[0].message.chat.id
            elif isinstance(args[0], telebot.types.Message):
                chat_id = args[0].chat.id
            else:
                chat_id = None

            if self.status.setdefault(chat_id, False):
                self.status[chat_id] = False
            return func(*args, **kwargs)

        return _wrapper

    def open_upload(self, func):
        """Декоратор, открывает поток загрузки"""

        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            if isinstance(args[0], telebot.types.CallbackQuery):
                chat_id = args[0].message.chat.id
            elif isinstance(args[0], telebot.types.Message):
                chat_id = args[0].chat.id
            else:
                chat_id = None

            self.status[chat_id] = True
            return func(*args, **kwargs)

        return _wrapper

    def add_content_type(self, content_type):
        """Объявляем тип контента для выгрузки"""

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

    def markup(self, chat_id, formatter):
        """Универсально возвращаем маркап (кнопочки под сообщением)"""
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(
            telebot.types.InlineKeyboardButton(
                "≪ Назад", callback_data=f"{self.content_type[chat_id]}_{formatter}"
            )
        )
        return markup
