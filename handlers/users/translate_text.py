from aiogram import types

from filters.all_filters import IsPrivate
from loader import dp, database
from googletrans import Translator


@dp.message_handler(IsPrivate())
async def translate(message: types.Message):
    translator = Translator()
    user_language = database.select_language(id=message.from_user.id)[0]
    translated = translator.translate(text=message.text, dest=user_language)
    await message.answer(translated.text)
