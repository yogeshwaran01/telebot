from googletrans import Translator


def translate_to_tamil(text):
    try:
        translator = Translator()
        result = translator.translate(text, dest="ta")
        return result.text
    except:
        return "Word Not Available"


def translate_to_english(text):
    try:
        translator = Translator()
        result = translator.translate(text, dest="en")
        return result.text
    except:
        return "Word Not Available"
