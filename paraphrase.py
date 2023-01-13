from paraphrasing_tools import ParaphrasingTool
from getting_lyrics import read_from_lyrics, write_to_lyrics
from random import choice


words_not_to_change = ['I', 'you', 'he', 'she', 'it', 'we', ',they',
                        'my', 'your', 'his', 'her', 'its', 'our', 'their',
                    ]


def qualify_rhymes():
    lyrics = read_from_lyrics()
    new_lyrics = []
    for word in lyrics:
        if '\n' in word and word not in words_not_to_change:
            new_lyrics.append(word)
    return new_lyrics


def how_much_paraphrase(percentage):
    '''
    returns the number of words that are to paraphrase depending on percentage
    '''
    lyrics = read_from_lyrics()
    amount_to_paraphrase = int(percentage * len(lyrics) / 100)
    return amount_to_paraphrase


def choose_what_paraphrase(percentage):
    '''
    randomly choices words from those qualified to paraphrase
    '''
    words_to_change = qualify_to_paraphrase()
    amount = how_much_paraphrase(percentage)
    chosen = []
    for number in range(amount + 1):
        n_choice = choice(words_to_change)
        if n_choice not in chosen:
            chosen.append(n_choice)
    return chosen


def qualify_to_paraphrase():
    '''
    eliminates words that should not be paraphrased:
    '''
    candidates = read_from_lyrics()
    qualified = []
    for word in candidates:
        if '\n' not in word and word not in words_not_to_change:
            qualified.append(word)
    return qualified


def paraphrase(title, author, percentage):
    write_to_lyrics(title, author, 'saved_lyrics.txt')
    lyrics = read_from_lyrics()
    chosen = choose_what_paraphrase(percentage)
    paraphrased = []
    index = 0
    for word in lyrics:
        word = ParaphrasingTool(word)
        if '\n' in word.name():
            paraphrased.append(word.switch_rhyme()[:-2])
        if word.name() in chosen:
            if index % 2 == 1:
                paraphrased.append(word.switch_synonims())
                index += 1
            if index % 2 == 0:
                paraphrased.append(word.add_adj())
                index += 1
        if '\n' not in word.name() and word.name() not in chosen:
            paraphrased.append(word.name())
    return paraphrased


def write_to_new_lyrics(title, author, file, percentage):
    lyrics = paraphrase(title, author, percentage)
    with open('new_lyrics.txt', 'w') as file:
        for word in lyrics:
            # if '\n' in word:
            #     file.write(word)
            file.write(f'{word} ')


# print(how_much_paraphrase(40))
# print(qualify_to_paraphrase())
# print(choose_what_paraphrase(40))

# print(read_from_lyrics())
# print(paraphrase_rhyme())
# print(write_to_lyrics('Sonnet 2: When forty winters shall besiege thy brow', 'William Shakespeare', 'saved_lyrics.txt'))
# print(paraphrase('Sonnet 2: When forty winters shall besiege thy brow', 'William Shakespeare', 40))
print(write_to_new_lyrics('Declaiming Waters none may dread --', 'Emily Dickinson', 'new_lyrics.txt', 50))

