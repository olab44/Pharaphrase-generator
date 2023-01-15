from paraphrasing_tools import ParaphrasingTool
from getting_lyrics import read_from_lyrics
from random import choice
from words_not_to_change import words_not_to_change


class Paraphrase:
    ''''
    Class Paraphrase. Contains attributes:
    :param name: text
    :param type: list
    :param representation: percentage
    :param type: int
    '''
    def __init__(self, text, percentage):
        text = read_from_lyrics('saved_lyrics.txt')
        if percentage > 100:
            raise ValueError('percentage must be between 0 and 100')
        self._percentage = percentage
        self._text = text

    def text(self):
        return self._text

    def percentage(self):
        return self._percentage

    def how_much_paraphrase(self):
        '''
        returns the number of words that are to paraphrase
        '''
        return int(self.percentage() * len(self.text()) / 100)

    def qualify_to_paraphrase(self):
        '''
        eliminates words that should not be paraphrased:
        '''
        qualified = []
        for word in self.text():
            if '\n' not in word and word not in words_not_to_change and len(word) > 2:
                qualified.append(word)
        return qualified

    def choose_what_paraphrase(self):
        '''
        randomly choices words from those qualified to paraphrase
        '''
        words_to_change = self.qualify_to_paraphrase()
        amount = self.how_much_paraphrase()
        chosen = []
        for number in range(amount + 1):
            n_choice = choice(words_to_change)
            if n_choice not in chosen:
                chosen.append(n_choice)
        return chosen

    def paraphrase(self):
        '''
        paraphrases the text depending on the percentage
        '''
        if self.percentage() == 0:
            return self.text()
        chosen = self.choose_what_paraphrase()
        paraphrased = []
        index = 0
        for word in self.text():
            word = ParaphrasingTool(word)
            if '\n' in word.name():
                # switches rhymes, only for words at the end of the line
                paraphrased.append(word.switch_rhyme())
            if word.name() in chosen:
                # half of the chosen words get related adjectives
                # half gets switched with synonims
                if index % 2 == 1:
                    paraphrased.append(word.switch_synonims())
                    index += 1
                if index % 2 == 0:
                    paraphrased.append(word.add_adj())
                    index += 1
            if '\n' not in word.name() and word.name() not in chosen:
                paraphrased.append(word.name())
        return paraphrased


def write_to_new_lyrics(file_handle, text, percentage):
    with open('new_lyrics.txt', 'w') as file_handle:
        parap = Paraphrase(text, percentage)
        text_2 = parap.paraphrase()
        for word in text_2:
            if '\n' in word:
                file_handle.write(word)
            to_add = f'{word} '
            file_handle.write(to_add)
