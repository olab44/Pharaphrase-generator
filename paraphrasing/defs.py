import json


def get_defs(path='config.json'):
    '''
    gets all the data from config.json
    '''
    with open(path, 'r') as file:
        data = json.load(file)
        return data


def all_urls():
    return get_defs()['urls']


def words_not_to_change():
    return get_defs()['words_not_to_change']


def saved_lyrics():
    return get_defs()['saved_lyrics']
