from .getting_lyrics import Poem, write_to_lyrics, read_from_lyrics
from .getting_lyrics import NotFoundTextError, NotFoundTitleError
from .paraphrase import Paraphrase, WrongPercentageError, NoPercentageError


def print_greeting():
    print('Welcome to paraphrasing text.')
    print('Here you can paraphrase any poem that can be found on the internet')


def asking_user():
    print('What would you like to paraphrase?')
    title = str(input('Enter the title: '))
    author = str(input('now enter the author: '))
    percent = (input('what percent of the text do you want to change?: '))
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
    print(' ')


def print_paraphrased_text(text):
    '''
    prints paraphrased text
    '''
    print('And here is your paraphrased text:')
    print('-'*40)
    print(text)
    print(' ')


def generate():
    title, author, percentage = asking_user()
    print(' ')
    try:
        print_original_text(title, author)
        write_to_lyrics(title, author)
        lyrics = read_from_lyrics()
        parap = Paraphrase(lyrics, percentage)
        text = ' '.join(parap.paraphrase())
        print_paraphrased_text(text)
    except NotFoundTitleError:
        print('Sorry, You have to type the title')
    except NotFoundTextError:
        print('Sorry, we could not find such text, try again')
    except NoPercentageError:
        print('Sorry, No percentage was given')
    except WrongPercentageError:
        print('Sorry, The percentage has to be between 0 and 100')


def main():
    print_greeting()
    while True:
        print('')
        generate()
        print(' ')
        print('Would you like to continue? ')
        action = str(input('Press c to continue or q to quit '))
        if action == 'c':
            generate()
        if action == 'q':
            exit()


if __name__ == '__main__':
    main()
