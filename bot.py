from bot_funtions import *
import requests
import json

js = "https://api.telegram.org/bot1303637043:AAGoZGXCorjYzag_-Y_Tt_Wpo_1Cutwvcto/"


def get_updates(offset=None):
    url = js + "getupdates?timeout=100"
    if offset:
        url = url + "&offset={}".format(offset + 1)
    html = requests.get(url)
    return json.loads(html.content)


def respond(chat_id, text, first_name, lang):
    send_message_to_devolper(f"{text} from { first_name}")
    try:
        try:
            text = text.lower()
        except:
            text = "media files"
        if text == "/start":
            welcome_user(first_name, chat_id)
            helper(first_name)
            about_developer(chat_id)
            help_user(first_name, chat_id)
        elif text == "/developer":
            about_developer(chat_id)
        elif text == "/username":
            send_message_to_user("@excelyo_bot", chat_id)
        elif text == "/help":
            help_user(first_name, chat_id)
        elif isNumber(text):
            word_of_number(text, chat_id)
        elif option_of(text) == "*":
            send_flames_of_message(text.split()[0], text.split()[1], chat_id)
        elif option_of(text) == "#":
            send_expand_of_message(text, chat_id)
        else:
            send_message_of_translation(lang, text, chat_id)
        return "ok"
    except:
        send_message_to_devolper("some errors")
        pass
    


update_id = None

try:
    while True:
        updates = get_updates(offset=update_id)
        updates = updates["result"]
        if updates:
            for item in updates:
                update_id = item["update_id"]
                from_id = item["message"]["from"]["id"]
                try:
                    message = str(item["message"]["text"])
                except:
                    send_message_to_user("Don't send media files",from_id )
                    message = "Don't send media files"
                try:
                    username = item["message"]["from"]["username"]
                except:
                    username = item["message"]["from"]["first_name"]
                lang = item["message"]["from"]["language_code"]
                respond(from_id, message, username, lang)
except:
    failed_message()
