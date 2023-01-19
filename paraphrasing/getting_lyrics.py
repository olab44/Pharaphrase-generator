import requests
from .defs import all_urls, saved_lyrics


class NotFoundTitleError(Exception):
    pass


class NotFoundTextError(Exception):
    pass


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
            raise NotFoundTitleError('there was no title given')
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
            poem = requests.get(all_urls()['lyrics_title'].format(title=self.title())).json()
        poem = requests.get(all_urls()['lyrics_author'].format(title=self.title(), author=self.author())).json()
        if 'status' in poem:
            raise NotFoundTextError('Sorry we could not find poem')
        return poem

    def lines(self):
        return self.data()['lines']

    def length(self):
        return self.data()['linecount']


def write_to_lyrics(title, author):
    '''
    writes the text to the .txt file
    '''
    path = saved_lyrics()
    with open(path, 'w') as file_handle:
        data = Poem(title, author)
        for verse in data.lines():
            line = f'{verse}\n'
            file_handle.write(line)


def read_from_lyrics():
    '''
    returns list of words from file
    '''
    words = []
    path = saved_lyrics()
    with open(path, 'r') as file:
        for line in file:
            verse = line.split(' ')
            for word in verse:
                words.append(word)
        return words
