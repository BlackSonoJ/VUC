from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from api_requests import get_media_list_len

_BACK_BUTTON_TEXT = "≪ Назад"

_text_templates = {
    "images": [
        "Добавить в галерею",
        "Удалить из галереи",
        _BACK_BUTTON_TEXT,
    ],
    "imagesMain": [
        "Добавить на главную",
        "Удалить с главной",
        _BACK_BUTTON_TEXT,
    ],
    "videos": [
        "Добавить видеоматериал",
        "Удалить видеоматериал",
        _BACK_BUTTON_TEXT,
    ],
}


def markup_media_start(content_type) -> InlineKeyboardMarkup:
    """Передаем на кнопки диплинк с данными, откуда пришли,
    чтобы понимать, откуда потом брать или куда выгружать медиа файлы
    content_data - наш диплинк, определяет в какую таблицу бд мы потом будем обращаться
    """
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    _text_templates[content_type][0],
                    callback_data=f"upload {content_type}",
                )
            ],
            [
                InlineKeyboardButton(
                    _text_templates[content_type][1],
                    callback_data=f"edit {content_type}",
                )
            ],
            [
                InlineKeyboardButton(
                    _text_templates[content_type][2], callback_data="start"
                )
            ],
        ]
    )


def markup_media_edit(content_type, page) -> InlineKeyboardMarkup:
    """В диплинк добавляем страницу, чтобы удобно переключаться по медиа"""
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "≪",
                    callback_data=f"edit {content_type} {page-1 if page > 0 else get_media_list_len(content_type)-1}",
                ),
                InlineKeyboardButton(
                    "≫",
                    callback_data=f"edit {content_type} {page+1 if page+1 < get_media_list_len(content_type) else 0}",
                ),
            ],
            [
                InlineKeyboardButton(
                    "Удалить",
                    callback_data=f"edit {content_type} {page} delete",
                )
            ],
            [
                InlineKeyboardButton(
                    _BACK_BUTTON_TEXT, callback_data=f"start {content_type}"
                )
            ],
        ]
    )


def markup_upload(content_type):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    _BACK_BUTTON_TEXT, callback_data=f"start {content_type}"
                )
            ],
        ]
    )
