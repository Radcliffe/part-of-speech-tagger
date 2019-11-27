# filename: happy_birthday.py
import hug
import nltk
import re

regex = r"(\w[A-Za-z']*)"

@hug.get('/happy_birthday')
def happy_birthday(name, age:hug.types.number=1):
    """Says happy birthday to a user"""
    return "Happy {age} Birthday {name}!".format(**locals())


@hug.post('/tag')
def tag(text):
    words = re.split(regex, text) [1::2]
    tags = [tag for word, tag in nltk.pos_tag(words)]
    return tags
