# -*- coding: utf-8 -*-
"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    # stores the number of matching words per language
    counters = [count_words(language['common_words'], text) for language in languages]

    # finds the index of the largest word count
    word_count_index = counters.index(max(counters))

    return languages[word_count_index]['name']

def count_words(common_words, text):
    """checks how many words in text are in the common words given"""
    i = 0
    for word in text.split():
            
        word = word.lower().strip("?!(),.:;\n")
            
        if word in common_words:
            i += 1
    return i
