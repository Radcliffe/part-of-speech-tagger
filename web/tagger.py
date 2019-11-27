# filename: happy_birthday.py
import hug
import nltk
import re

regex = r"(\w[A-Za-z']*)"

@hug.post('/tag')
def tag(text):
    words = re.split(regex, text) [1::2]
    tags = [tag for word, tag in nltk.pos_tag(words)]
    return tags
