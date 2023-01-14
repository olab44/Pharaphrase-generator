from getting_lyrics import Poem
from paraphrase import read_from_new_lyrics, paraphrase


def print_original_text(title, author):
    text = Poem(title, author)
    print('here is your original text:')
    print('-'*40)
    for line in text.lines():
        print(line)


def print_paraphrased_text():
    text = read_from_new_lyrics()
    print('here is your paraphrased text')
    print('-'*40)
    for line in text:
        print(line)


def main(title, author, percentage):
    print('Welcome to paraphrasing text.')
    print(' ')
    print_original_text(title, author)
    paraphrase(title, author, percentage)
    print(' ')
    print_paraphrased_text()


if __name__ == '__main__':
    main('Not at Home to Callers', 'Emily Dickinson', 40)
