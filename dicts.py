from PyDictionary import PyDictionary
from googletrans import Translator


def translate_to_tamil(text):
    try:
        translator = Translator()
        result = translator.translate(text, dest="ta")
        return result.text
    except:
        return "Word Not Available"


def meaning_list(texts):
    text = texts.lower()
    try:
        dicts = PyDictionary()
        mean = dicts.meaning(text)
        try:
            mean_noun = mean["Noun"]
        except:
            mean_noun = ["It may be a name or not a noun"]
        try:
            mean_verb = mean["Verb"]
        except:
            mean_verb = ["It is not Verb"]
        try:
            mean_adj = mean["Adjective"]
        except:
            mean_adj = ["It is not Adjective"]
        try:
            mean_adv = mean["Adverb"]
        except:
            mean_adv = ["It is not Adverb"]
    except:
        mean_noun = ["Not Available"]
        mean_verb = ["Not Available"]
        mean_adj = ["Not Available"]
        mean_adv = ["Not Available"]

    return mean_noun, mean_verb, mean_adj, mean_adv


def meaning(text):
    tup = meaning_list(text)
    string_of_mean_noun = ""
    string_of_mean_verb = ""
    string_of_mean_adj = ""
    string_of_mean_adv = ""
    for word in tup[0]:
        string_of_mean_noun = string_of_mean_noun + word + "\n"
    for word in tup[1]:
        string_of_mean_verb = string_of_mean_verb + word + "\n"
    for word in tup[2]:
        string_of_mean_adj = string_of_mean_adj + word + "\n"
    for word in tup[3]:
        string_of_mean_adv = string_of_mean_adv + word + "\n"

    final = """
    {}

Meaning as Noun:
---------------
{}
Meaning as Verb:
---------------
{}
Meaning as Adjective:
--------------------
{}
Meaning as Adverb:
--------------------
{}
Tamil Meaning:
-------------
{}

    """.format(text.title(), string_of_mean_noun, string_of_mean_verb, string_of_mean_adj, string_of_mean_adv,
               translate_to_tamil(text))
    return final
