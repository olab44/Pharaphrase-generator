import json

# urls = {
#     'lyrics_title': 'https://poetrydb.org/title/{title}',
#     'lyrics_author': 'https://poetrydb.org/author,title/{author};{title}',
#     'related_adjectives': 'https://api.datamuse.com/words?rel_jjb={word}',
#     'synonims': 'https://api.datamuse.com/words?rel_syn={word}',
#     'rhymes': 'https://api.datamuse.com/words?ml={word}&rel_rhy={word}'
# }


def read_from_urls_json(file_handle):
    data = json.load(file_handle)
    return data
    # all_urls = {}
    # for key in data:
    #     url = all_urls[key]
    # return all_urls


def get_urls(key, file_handle):
    all_urls = read_from_urls_json(file_handle)
    return all_urls[key]


print(read_from_urls_json('urls.json'))
