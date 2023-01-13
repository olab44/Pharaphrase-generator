import requests
from urls import urls
from word import Word


def get_poetry(title, author):
    if not author:
        return requests.get(urls['lyrics_title'].format(title=title)).json()
    return requests.get(urls['lyrics_author'].format(title=title, author=author)).json()


class Lyrics:
    def __init__(self, title, author):
        data = get_poetry(title, author)[0]
        self._data = data

    def title(self):
        return self._data['title']

    def author(self):
        return self._data['author']

    def lines(self):
        return self._data['lines']

    def length(self):
        return self._data['linecount']


def read_from_lyrics():
    words = []
    with open('saved_lyrics.txt', 'r') as file:
        for line in file:
            verse = line.split(' ')
            for word in verse:
                word = Word(word)
                words.append(word._name)
        return words


def write_to_lyrics(title, author, file_handle):
    with open('saved_lyrics.txt', 'w') as file_handle:
        data = Lyrics(title, author)
        for verse in data.lines():
            line = f'{verse}\n'
            file_handle.write(line)
