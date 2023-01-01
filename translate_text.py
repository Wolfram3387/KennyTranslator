from googletrans import Translator

from loader import database


def translate(text, user_id=None, to_lang=None):  # TODO применить везде
    if user_id:
        to_lang = database.select_language(id=user_id)
    translator = Translator()
    translated = translator.translate(text=text, dest=to_lang)
    return translated.text
