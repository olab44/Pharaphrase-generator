from getting_lyrics import Poem, write_to_lyrics, read_from_lyrics
from paraphrase import Paraphrase


def asking_user():
    print('Welcome to paraphrasing text.')
    print('Here you can paraphrase any poem that can be found on the internet')
    print('What would you like to paraphrase?')
    title = str(input('Enter the title: '))
    author = str(input('now enter the author: '))
    percent = int(input('what percent of the text do you want to change?: '))
    return title, author, percent


def print_original_text(title, author):
    '''
    prints original text
    '''
    text = Poem(title, author)
    print('Here is your original text:')
    print('-'*40)
    for line in text.lines():
        print(line)


def print_paraphrased_text(text):
    '''
    prints paraphrased text
    '''
    print('Here is your paraphrased text:')
    print('-'*40)
    print(text)
    print(' ')


def main():
    title, author, percentage = asking_user()
    print(' ')
    print_original_text(title, author)
    write_to_lyrics(title, author)
    lyrics = read_from_lyrics()
    parap = Paraphrase(lyrics, percentage)
    text = ' '.join(parap.paraphrase())
    print_paraphrased_text(text)


if __name__ == '__main__':
    main()
