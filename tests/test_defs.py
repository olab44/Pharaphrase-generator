from paraphrasing.defs import all_urls, get_defs
from paraphrasing.defs import words_not_to_change, saved_lyrics


def test_get_defs():
    assert get_defs() == {
        'urls':
        {'lyrics_title': 'https://poetrydb.org/title/{title}',
         'lyrics_author': 'https://poetrydb.org/author,title/{author};{title}',
         'synonims': 'https://api.datamuse.com/words?rel_syn={word}',
         'rhymes': 'https://api.datamuse.com/words?ml={word}&rel_rhy={word}',
         'related_adjectives': 'https://api.datamuse.com/words?rel_jjb={word}'
         },
        'saved_lyrics': 'paraphrasing/saved_lyrics.txt',
        'words_not_to_change': [
                'I', 'you', 'he', 'she', 'it', 'we', 'they', 'my', 'your',
                'his', 'her', 'its', 'our', 'their', 'me', 'him', 'hers',
                'them', 'Not', 'no', 'not', 'yes', 'Yes', 'the', 'The',
                'and', 'And', 'From', 'from', 'with', 'for']}


def test_all_urls():
    assert all_urls() == {
        'lyrics_title': 'https://poetrydb.org/title/{title}',
        'lyrics_author': 'https://poetrydb.org/author,title/{author};{title}',
        'synonims': 'https://api.datamuse.com/words?rel_syn={word}',
        'rhymes': 'https://api.datamuse.com/words?ml={word}&rel_rhy={word}',
        'related_adjectives': 'https://api.datamuse.com/words?rel_jjb={word}'
        }


def test_saved_lyrics():
    assert saved_lyrics() == 'paraphrasing/saved_lyrics.txt'


def test_words_not_to_change():
    assert words_not_to_change() == [
                'I', 'you', 'he', 'she', 'it', 'we', 'they', 'my', 'your',
                'his', 'her', 'its', 'our', 'their', 'me', 'him', 'hers',
                'them', 'Not', 'no', 'not', 'yes', 'Yes', 'the', 'The',
                'and', 'And', 'From', 'from', 'with', 'for']
