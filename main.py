import requests
from getting_lyrics import read_from_lyrics
from paraphrase import read_from_new_lyrics


def asking_user():
    print('welcome to paraphrasing text.')
    title = str(input('Now enter the title: '))
    author = str(input('now enter the author: '))
    print('here is your original text:')
    percentage = int(input('enter the percentage of the text you want it to be paraphrased: '))


def print_original_text():
    text = read_from_lyrics()
    for line in text:
        print(line)


def print_paraphrased_text():
    text = read_from_new_lyrics()
    for line in text:
        print(line)

def main():
    pass


# print(asking_user())
# print_original_text()
print_paraphrased_text()
