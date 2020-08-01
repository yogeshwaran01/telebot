import telegram
import requests
import json
from config import token
from expand import expand
from datetime import datetime
from flames import flames
from wiki import wiki, langs
from help import helper
from translate import translate_to_tamil

api = "https://api.telegram.org/bot{}/".format(token)
bot = telegram.Bot(token=token)


def format_user_name(first, last):
    try:
        return first + last
    except:
        return first


def get_updates(offset=None):
    url = api + "getupdates?timeout=100"
    if offset:
        url = url + "&offset={}".format(offset + 1)
    html = requests.get(url)
    return json.loads(html.content)


def send_message(msg, chat_id):
    bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)


def output_personal(input_message, user_name):
    input_message = input_message.lower()
    input_message_splitted = input_message.split()
    output_message = "Type help for Usage"
    if input_message is not None:
        if input_message == "name":
            output_message = "My name is Excel (The Robot)"
        elif "hai" in input_message:
            output_message = "hai {}".format(user_name)
        elif input_message[0] == "*":
            select = input_message[1:]
            output_message = expand(select)
        elif input_message[0] == "#":
            input_message_list = input_message.split()
            output_message = flames(input_message_list[1], input_message_list[2])
        elif input_message_splitted[0] in langs:
            output_message = wiki(input_message_splitted[0], input_message_splitted[1])
        elif input_message == "author":
            output_message = "YOGESHWARAN R"
        elif input_message == "/start":
            output_message = helper()
        elif input_message == "help":
            output_message = helper()
        elif input_message == "username":
            output_message = "@excelyo_bot"
        else:
            output_message = translate_to_tamil(input_message)
        return output_message


update_id = None

while True:
    print("...")
    updates = get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None

            from_id = item["message"]["from"]["id"]
            first_name = item["message"]["from"]["first_name"]
            last_name = item["message"]["from"]["last_name"]
            name = format_user_name(first_name, last_name)
            date = datetime.fromtimestamp(item["message"]["date"])
            print("{} from {} at {}".format(message, name, date))
            send_message(output_personal(message, name), from_id)
