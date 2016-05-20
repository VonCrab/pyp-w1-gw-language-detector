# -*- coding: utf-8 -*-
"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    # stores the number of matching words per language
    counters = []
    
    for language in languages:
        i = 0
        
        for word in text.split():
            
            word = word.lower()
            
            if word in language['common_words']:
                i += 1
                
        counters.append(i)
  
    # finds the index of the largest word count
    word_count_index = counters.index(max(counters))

    return languages[word_count_index]['name']
