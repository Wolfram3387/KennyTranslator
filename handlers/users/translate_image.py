from aiogram import types
import pytesseract
import cv2
import os
from googletrans import Translator
from filters.all_filters import IsPrivate
from loader import dp, database


@dp.message_handler(IsPrivate(), content_types=[types.ContentType.PHOTO, types.ContentType.DOCUMENT])
async def translate(message: types.Message):
    """Распознаёт только .png .jpeg картинки и только на английском языке"""
    file_path = f'data/{message.from_user.id}.png'  # Создаём путь, по которому сохранится фото
    await message.photo.pop().download(destination_file=file_path)  # Сохраняем фото по нужному пути
    try:
        image = cv2.imread(file_path)
        text = pytesseract.image_to_string(image)
        user_language = database.select_language(id=message.from_user.id)[0]
        translated_text = Translator().translate(text=text, dest=user_language).text
        await message.answer(translated_text)
    except:
        await message.answer('Не получилось прочитать картинку. Возможно, вы отправили не .png .jpeg файл')
    os.remove(file_path)  # Удаление временного файла
