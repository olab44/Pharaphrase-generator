from getting_lyrics import Poem, write_to_lyrics, read_from_lyrics
from paraphrase import Paraphrase, write_to_new_lyrics


def print_original_text(title, author):
    '''
    prints original text
    '''
    text = Poem(title, author)
    print('here is your original text:')
    print('-'*40)
    for line in text.lines():
        print(line)


def print_paraphrased_text(text):
    '''
    prints paraphrased text
    '''
    print('here is your paraphrased text:')
    print('-'*40)
    print(text)


def main(title, author, percentage):
    print('Welcome to paraphrasing text.')
    print(' ')
    print_original_text(title, author)
    write_to_lyrics(title, author, 'saved_lyrics.txt')
    lyrics = read_from_lyrics('saved_lyrics.txt')
    parap = Paraphrase(lyrics, percentage)
    # write_to_new_lyrics('new_lyrics.txt', lyrics, percentage)
    text = ' '.join(parap.paraphrase())
    print(' ')
    print_paraphrased_text(text)


if __name__ == '__main__':
    main('Ozymandias', 'Percy Bysshe Shelley', 30)
