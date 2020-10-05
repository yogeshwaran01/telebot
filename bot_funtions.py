import telegram
from config import TOKEN, URL
from flames import flames
from expand import expand
from translate import translate_to_english, translate_to_tamil
from dicts import meaning
from help import helper
import num2word as digit

bot = telegram.Bot(token=TOKEN)


def send_message_to_user(msg, chat_id):
    try:
        bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)
    except:
        bot.send_message(
            chat_id=chat_id, text="Sorry try again", parse_mode=telegram.ParseMode.HTML
        )


def send_message_to_devolper(msg):
    bot.send_message(chat_id=1071607407, text=msg, parse_mode=telegram.ParseMode.HTML)


def send_flames_of_message(p1, p2, chat_id):
    send_message_to_user(flames(p1, p2), chat_id)


def send_expand_of_message(word, chat_id):
    send_message_to_user(expand(word), chat_id)


def send_message_of_translation(lang, msg, chat_id):
    if lang == "en":
        if len(msg.split()) == 1:
            send_message_to_user(meaning(msg), chat_id)
        else:
            send_message_to_user(translate_to_tamil(msg), chat_id)
    else:
        send_message_to_user(translate_to_english(msg), chat_id)


def format_user_name(first, last):
    try:
        return first + last
    except:
        return first


def welcome_user(first, chat_id):
    msg = f"""
    
    Hi! {first} 
    My name is Excel
    """
    send_message_to_user(msg, chat_id)


def help_user(first, chat_id):
    send_message_to_user(helper(first), chat_id)


def word_of_number(msg, chat_id):
    send_message_to_user(digit.word(msg), chat_id)


def failed_message():
    send_message_to_devolper("Bot is Failed")


def isNumber(s):
    for i in range(len(s)):
        if not s[i].isdigit():
            return False

    return True


def about_developer(chat_id):
    msg = """
    
    Name: YOGESHWARAN R
    Lang: Python 3.8
    GitHub: https://github.com/yogeshwaran01

    """
    send_message_to_user("Developer", chat_id)
    send_message_to_user(msg, chat_id)


def option_of(msg):
    return msg[0]
