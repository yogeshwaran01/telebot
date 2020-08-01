from googletrans import Translator


def translate_to_tamil(text):
    translator = Translator()
    result = translator.translate(text, dest="ta")
    return result.text


def translate_to_english(text):
    translator = Translator()
    result = translator.translate(text, dest="en")
    return result.text
