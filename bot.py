import telegram
import num2word as digit
import requests
import json
from datetime import datetime
from langdetect import detect
from config import token
from expand import expand
from flames import flames
from wiki import wiki_english, wiki_tamil
from help import helper
from translate import translate_to_tamil, translate_to_english
from dicts import meaning

api = "https://api.telegram.org/bot{}/".format(token)
bot = telegram.Bot(token=token)

def isNumber(s) :

    for i in range(len(s)) :
        if s[i].isdigit() != True :
            return False

    return True

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
    try:
        bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)
    except:
        bot.send_message(chat_id=chat_id, text="Sorry try again", parse_mode=telegram.ParseMode.HTML)


def output_personal(input_message, user_name):
    try:
        input_message = input_message.lower()
    except:
        input_message = "media files"
    input_message_splitted = input_message.split()
    if input_message is not None:
        if input_message == "!name":
            output_message = "My name is Excel (The Robot)\n I am used to learn English from Tamil"
        elif input_message == "hai":
            output_message = "hai {}".format(user_name)
        elif input_message[0] == "*":
            try:
                select = input_message[1:]
                output_message = expand(select)
            except:
                output_message = "Try another word"
        elif input_message[0] == "#":
            try:
                input_message_list = input_message.split()
                output_message = flames(input_message_list[1], input_message_list[2])
            except:
                output_message = "Please use two words for flames!"
        elif input_message_splitted[0] == "en":
            try:
                output_message = wiki_english("{} {}".format(input_message_splitted[1], input_message_splitted[2]))
            except IndexError:
                output_message = wiki_english(input_message_splitted[1])
        elif input_message_splitted[0] == "ta":
            try:
                output_message = wiki_tamil("{} {}".format(input_message_splitted[1], input_message_splitted[2]))
            except IndexError:
                output_message = wiki_tamil(input_message_splitted[1])
        elif input_message == "!developer":
            output_message = "YOGESHWARAN R"
        elif input_message == "/start":
            output_message = helper(user_name)
        elif input_message == "!help":
            output_message = helper(user_name)
        elif input_message == "!username":
            output_message = "@excelyo_bot"
        elif isNumber(input_message):
            output_message = digit.word(input_message)

        else:
            try:
                a = detect(input_message)
                if a == "en":
                    if len(input_message_splitted) == 1:
                        output_message = meaning(input_message)
                    else:
                        output_message = translate_to_tamil(input_message)
                elif a == "ta":
                    output_message = translate_to_english(input_message)
                else:
                    if len(input_message_splitted) == 1:
                        output_message = meaning(input_message)
                    else:
                        output_message = translate_to_tamil(input_message)
            except:
                output_message = "Not Available!"
        return output_message


update_id = None

while True:
    try:
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
                try:
                    last_name = item["message"]["from"]["last_name"]
                except:
                    last_name = ""
                name = format_user_name(first_name, last_name)
                date = datetime.fromtimestamp(item["message"]["date"])
                details = "{} from {} at {}".format(message, name, date)
                send_message(output_personal(message, name), from_id)
                bot.send_message(chat_id=1071607407, text=details, parse_mode=telegram.ParseMode.HTML)
    except:
        bot.send_message(chat_id=1071607407, text="Bot is failed!", parse_mode=telegram.ParseMode.HTML)
