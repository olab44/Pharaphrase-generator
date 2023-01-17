from paraphrasing.getting_lyrics import Poem, read_from_lyrics, write_to_lyrics


def test_create_poem():
    poem = Poem('Not at Home to Callers', 'Emily Dickinson')
    assert poem.title() == 'Not at Home to Callers'
    assert poem.author() == 'Emily Dickinson'


def test_poem_without_author():
    poem = Poem('Ozymandias')
    assert poem.title() == 'Ozymandias'
    assert poem.author() is None


def test_get_poem():
    poem = Poem('Not at Home to Callers', 'Emily Dickinson')
    data = {'title': 'Not at Home to Callers',
            'author': 'Emily Dickinson',
            'lines': ['Not at Home to Callers',
                      'Says the Naked Tree --',
                      'Bonnet due in April --',
                      'Wishing you Good Day --'],
            'linecount': '4'}
    assert poem.data() == data


def test_poem_lines():
    poem = Poem('Not at Home to Callers', 'Emily Dickinson')
    lines = ['Not at Home to Callers',
             'Says the Naked Tree --',
             'Bonnet due in April --',
             'Wishing you Good Day --']
    assert poem.lines() == lines


def test_read_from_lyrics():
    title = 'Not at home to Callers'
    author = 'Emily Dickinson'
    write_to_lyrics(title, author, 'saved_lyrics.txt')
    supposed_lyrics = ['Not', 'at', 'Home', 'to', 'Callers\n', 'Says', 'the',
                       'Naked', 'Tree', '--\n', 'Bonnet', 'due', 'in',
                       'April', '--\n', 'Wishing', 'you', 'Good',
                       'Day', '--\n']
    assert read_from_lyrics('saved_lyrics.txt') == supposed_lyrics
