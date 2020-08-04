import wikipedia


def wiki_english(topic):
    try:
        wikipedia.set_lang('en')
        result = str(wikipedia.summary(topic))
    except:
        result = "NOT FOUND! Try another topic"
    return result


def wiki_tamil(topic):
    try:
        wikipedia.set_lang('ta')
        result = str(wikipedia.summary(topic))
    except:
        result = "NOT FOUND! Try another topic"
    return result



