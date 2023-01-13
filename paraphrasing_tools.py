import requests
from urls import urls


def get_paraphrasing_tool(word, tool):
    return requests.get(urls[tool].format(word=word)).json()


class ParaphrasingTool:
    def __init__(self, word):
        self._word = word

    def name(self):
        return self._word

    def switch_synonims(self):
        synonims = get_paraphrasing_tool(self.name(), 'synonims')
        if len(synonims) == 0:
            return self.name()
        return synonims[0]['word']

    def switch_rhyme(self):
        rhymes = get_paraphrasing_tool(self.name(), 'rhymes')
        if len(rhymes) == 0:
            return f'{self.name()}\n'
        best_rhyme = rhymes[0]['word']
        return f'{best_rhyme}\n'

    def add_adj(self):
        adjs = get_paraphrasing_tool(self.name(), 'related_adjectives')
        if len(adjs) == 0:
            return self.name()
        best_adj = adjs[0]['word']
        return f'{best_adj} {self.name()}'


parap = ParaphrasingTool('mountain')
# print(parap.switch_synonims())
# print(parap.switch_rhyme())
print(parap.add_adj())
