import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.error import BadRequest
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from markup_templater import markup_media_start, markup_media_edit, markup_upload
from api_requests import get_media, get_media_raw, delete_media, save_media, get_bytes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
upload_type = {}


def generate_main_menu() -> tuple[str, InlineKeyboardMarkup]:
    """Генерация текста и клавиатуры для главного меню"""

    text = """
Здравия желаю!                     
    
Данный бот был подготовлен для удобного администрирования информационного киоска ВУЦ БФУ.
    
Для дальнейшей работы нажмите на кнопки ниже.
    """

    keyboard = [
        [
            InlineKeyboardButton(
                text="📷 Галлерея изображений", callback_data="start images"
            )
        ],
        [
            InlineKeyboardButton(
                text="📷 Изображения на главной", callback_data="start imagesMain"
            )
        ],
        [InlineKeyboardButton(text="🎥 Галлерея видео", callback_data="start videos")],
        [InlineKeyboardButton(text="🗓️ Календарь", callback_data="start calendar")],
        [
            InlineKeyboardButton(text="🔍 Информация", callback_data="info"),
            InlineKeyboardButton(text="❌ Закрыть", callback_data="close"),
        ],
    ]

    return text.strip(), InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка команды /start"""
    text, reply_markup = generate_main_menu()
    try:
        query = update.callback_query
        await query.answer()
        if query.message.chat.id in upload_type:
            upload_type.pop(query.message.chat.id)
        await query.edit_message_text(text=text, reply_markup=reply_markup)
    except AttributeError:
        if update.message.chat.id in upload_type:
            upload_type.pop(update.message.chat.id)
        await update.message.reply_text(
            text=text,
            reply_markup=reply_markup,
        )


async def media_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Главная страница по работе с галереей"""
    query = update.callback_query
    await query.answer()
    if query.message.chat.id in upload_type:
        upload_type.pop(query.message.chat.id)
    try:
        await query.edit_message_text(
            text="Выберите действие",
            reply_markup=markup_media_start(query.data.split()[1]),
        )
    except BadRequest:
        await query.message.reply_text(
            text="Выберите действие",
            reply_markup=markup_media_start(query.data.split()[1]),
        )


async def edit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Просмотр и удаление медиа файлов с бота"""
    query = update.callback_query
    await query.answer()
    data = query.data.split()
    page = 0 if len(data) == 2 else int(data[2])
    markup = markup_media_edit(data[1], page)
    if len(data) > 2:
        if len(data) == 4:
            delete_media(data[1], int(data[2]))
            await query.edit_message_media(
                media=get_media(data[1], page - 1),
                reply_markup=markup_media_edit(data[1], page - 1),
            )
        else:
            await query.edit_message_media(
                media=get_media(data[1], page),
                reply_markup=markup,
            )
    else:
        if data[1] == "videos":
            await query.message.reply_video(
                video=get_media_raw(data[1], page),
                reply_markup=markup,
            )
        else:
            await query.message.reply_photo(
                photo=get_media_raw(data[1], page),
                reply_markup=markup,
            )


async def upload(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data.split()
    if upload_type.setdefault(query.message.chat.id, query.data.split()[1]):
        upload_type[query.message.chat.id] = query.data.split()[1]
    await query.edit_message_text(
        text="""
Отправьте материал(ы).
После отправки нажмите "Назад" на этом сообщении, чтобы завершить загрузку.
        """,
        reply_markup=markup_upload(data[1]),
    )


async def handle_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Сохраняем медиа файлы"""
    if update.message.chat.id not in upload_type:
        return
    content_type = upload_type[update.message.chat.id]
    if update.message.photo:
        media = update.message.photo[-1]
        media_type = "image"
    elif update.message.video:
        media = update.message.video
        media_type = "video"
    else:
        return
    extension = "jpg" if media_type == "image" else "mp4"
    file = await context.bot.get_file(media.file_id)
    file = {
        media_type: (
            f"{media.file_id}.{extension}",
            get_bytes(file.file_path),
            f"{media_type}/{extension}",
        )
    }
    save_media(content_type, file)


def main() -> None:
    """Run the bot."""
    application = Application.builder().token(os.getenv("BOT_TOKEN")).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(start, pattern=r"^start$"))
    application.add_handler(CallbackQueryHandler(media_start, pattern=r"^start .*$"))
    # функция media_start вызывается любой кнопкой с callbackdata,
    # что начинается на "start " (пробел важен, по нему будем сплитить наш диплинк)
    application.add_handler(CallbackQueryHandler(edit, pattern=r"^edit .*$"))
    application.add_handler(CallbackQueryHandler(upload, pattern=r"^upload .*$"))

    application.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO, handle_media))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
