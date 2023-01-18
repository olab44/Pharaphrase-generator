import requests
from urls import urls


class Poem:
    '''
    class Poem. contains attributes:
    :param representation: title
    :param type: str
    :param representation: author
    :param type: str (default None)
    '''
    def __init__(self, title, author=None):
        if not title:
            raise ValueError('there was no title given')
        self._title = title
        self._author = author

    def title(self):
        return self._title

    def author(self):
        return self._author

    def data(self):
        return self.get_poem()[0]

    def get_poem(self):
        '''
        gets the text of the poem by API,
        raises ValueError, when API does not find anything
        '''
        if not self.author():
            return requests.get(urls['lyrics_title'].format(title=self._title)).json()
        poem = requests.get(urls['lyrics_author'].format(title=self.title(), author=self.author())).json()
        if 'status' in poem:
            raise ValueError('Sorry we could not find poem with this title')
        return poem

    def lines(self):
        return self.data()['lines']

    def length(self):
        return self.data()['linecount']


def write_to_lyrics(title, author, file_handle):
    with open('saved_lyrics.txt', 'w') as file_handle:
        data = Poem(title, author)
        for verse in data.lines():
            line = f'{verse}\n'
            file_handle.write(line)


def read_from_lyrics(file_handle):
    '''
    returns list of words from file
    '''
    words = []
    with open('saved_lyrics.txt', 'r') as file_handle:
        for line in file_handle:
            verse = line.split(' ')
            for word in verse:
                words.append(word)
        return words