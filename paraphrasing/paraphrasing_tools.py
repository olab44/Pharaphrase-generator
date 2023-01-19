import requests
from .defs import all_urls


def get_paraphrasing_tool(word, tool):
    '''
    with an API gets the paraphrasing tool
    (synonyms, related adjectives or rhymes)
    for a given word
    words are sorted by the score amount
    '''
    urls = all_urls()
    return requests.get(urls[tool].format(word=word)).json()


class ParaphrasingTool:
    '''
    class ParaphrasingTool. contains attribute
    :param representation: word
    :param type: str
    '''
    def __init__(self, word):
        self._word = word

    def name(self):
        return self._word

    def switch_synonyms(self):
        '''
        1. gets the list of synonims for given word by API
        2. returns the one with the biggest score
        '''
        synonyms = get_paraphrasing_tool(self.name(), 'synonims')
        if len(synonyms) == 0:
            return self.name()
        return synonyms[0]['word']

    def switch_rhyme(self):
        '''
        1. gets the list of rhyming words
        2. returns the one with the most points
        '''
        word = self.name()[:-1]
        rhymes = get_paraphrasing_tool(word, 'rhymes')
        if len(rhymes) == 0:
            return f'{self.name()}'
        else:
            best_rhyme = rhymes[0]['word']
            return f'{best_rhyme}\n'

    def add_adj(self):
        '''
        1. gets the list of related adjectives
        2. returns the pair: 'adjective word'
        '''
        adjs = get_paraphrasing_tool(self.name(), 'related_adjectives')
        if len(adjs) == 0:
            return self.name()
        best_adj = adjs[0]['word']
        return f'{best_adj} {self.name()}'
