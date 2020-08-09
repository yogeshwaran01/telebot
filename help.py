def helper(username):
    result = """

Welcome {}, I am Excel, a Bot I have some features

Main usage:
==========
    (TRANSLATIONS)
    ENGLISH --- > TAMIL
    TAMIL --- > ENGLISH
    If you provide a single english word it gives meaning of a word as Noun,Verb,Adjective,Adverb and tamil meaning
-----------------------------------------
Some features:
=============
    ta any topic --> short passage about topic in tamil
    en any topic --> short passage about topic in english
    (Read the passage and understand the meanings)
-----------------------------------------
Some additional features:
========================
    Any number convert to words of that number
                                        (ex: 100 gives one hundread)
    * your_name ==> Gives Expand form of your name and its describe your character
                                        (ex: * dhoni)
    # name_1 name_2 ==> Gives FLAMES between name_1 and name_2
                                        (ex: # dhoni virat)
-----------------------------------------
About:
=====
    !developer ==> Gives the name of this Bot           developer
    !name ==> Gives the name of this bot
    !username ==> Gives the username of this bot
    !help ==> To see the Descriptions
    """.format(username)
    return result
