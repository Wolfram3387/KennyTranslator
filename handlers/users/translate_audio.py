import requests
import speech_recognition
import os
from os import path

from aiogram import types
from googletrans import Translator

from data.config import BOT_TOKEN
from filters.all_filters import IsPrivate
from loader import dp, bot, database


@dp.message_handler(IsPrivate(), content_types=types.ContentType.AUDIO)
async def translate_audio(message: types.Message):
    """Работает только с .wav расширением и распознаёт только английский язык"""
    # Получаем информацию о файле
    file_info = await bot.get_file(message.audio.file_id)

    # Скачиваем файл себе на компьютер
    file = requests.get(f'https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}')
    file_path = path.join(os.getcwd(), 'data', f'{message.from_user.id}.wav')
    with open(file_path, 'wb') as f:
        f.write(file.content)

    # Распознаём речь и переводим её в текст
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio, language='en-EN')

    # Отправляем текст пользователю
    user_language = database.select_language(id=message.from_user.id)[0]
    await message.answer(Translator().translate(text=text, dest=user_language).text)

    os.remove(file_path)  # Удаление временного файла
