import requests
import os
import typing

from dotenv import load_dotenv
from telegram import InputMediaPhoto, InputMediaVideo


def content_type_urls() -> typing.Dict:
    """Получаем с API типы контента и соответствующие URL"""
    load_dotenv()
    return requests.get(os.getenv("API_URL"), timeout=5).json()


def get_media_raw(content_type, page):
    """возвращает файл из апи, запрашиваемый пользователем"""
    response = requests.get(url=content_type_urls()[content_type], timeout=5)
    media_url = response.json()[page][content_type[:5]]
    response = requests.get(media_url, timeout=5)
    return response.content


def get_media(content_type, page):
    """возвращает файл из апи, запрашиваемый пользователем с присвоенным типом"""
    media = get_media_raw(content_type, page)
    return (
        InputMediaPhoto(media)
        if content_type[:5] == "image"
        else InputMediaVideo(media)
    )


def get_media_list_len(content_type):
    """Для проверки на переполнение при изменении страницы"""
    response = requests.get(url=content_type_urls()[content_type], timeout=5)
    return len(response.json())


def get_media_id(content_type, page):
    """Для проверки на переполнение при изменении страницы"""
    response = requests.get(url=content_type_urls()[content_type], timeout=5)
    return response.json()[page]["id"]


def get_api_token():
    """Получаем токен api для запросов, требующих аутентификацию"""

    token_request = requests.post(
        f"{os.getenv("API_URL")}token/",
        data={"username": os.getenv("API_USER"), "password": os.getenv("API_PASSWORD")},
        timeout=5,
    )
    token_data = token_request.json()
    return token_data.get("access")


def delete_media(content_type, page):
    """Удаляем медиа по запросу"""
    headers = {"Authorization": f"Bearer {get_api_token()}"}
    requests.delete(
        f"{content_type_urls()[content_type]}{get_media_id(content_type, page)}/",
        headers=headers,
        timeout=15,
    )


def save_media(content_type, file):
    headers = {"Authorization": f"Bearer {get_api_token()}"}
    response = requests.post(
        f"{content_type_urls()[content_type]}", files=file, headers=headers, timeout=15
    )


def get_bytes(file_path):
    response = requests.get(file_path, timeout=5)
    return response.content
