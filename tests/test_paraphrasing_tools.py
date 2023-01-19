from paraphrasing.paraphrasing_tools import ParaphrasingTool
from paraphrasing.paraphrasing_tools import get_paraphrasing_tool


def test_get_paraphrasing_tool():
    list_syn_top_5 = [
        {"word": "route", "score": 2820},
        {"word": "itinerant", "score": 1338},
        {"word": "moving", "score": 774},
        {"word": "traveling", "score": 725},
        {"word": "touring", "score": 287}
    ]
    get_all = get_paraphrasing_tool('road', 'synonims')
    assert get_all[:6] == list_syn_top_5


def test_paraphrasing_tool_switch_syn():
    word = ParaphrasingTool('road')
    assert word.switch_synonyms() == 'route'


def test_paraphrasing_tool_switch_syn_fail():
    word = ParaphrasingTool('wneionwon')
    assert word.switch_synonyms() == 'wneionwon'


def test_paraphrasing_tool_switch_rhy():
    word = ParaphrasingTool('road')
    assert word.switch_rhyme() == 'railroad\n'


def test_paraphrasing_tool_switch_rhy_with_n():
    word = ParaphrasingTool('road\n')
    assert word.switch_rhyme() == 'railroad\n'


def test_paraphrasing_tool_switch_rhy_fail():
    word = ParaphrasingTool('egoenwonvi\n')
    assert word.switch_rhyme() == 'egoenwonvi\n'


def test_paraphrasing_tool_add_adj():
    word = ParaphrasingTool('mountain')
    assert word.add_adj() == 'high mountain'


def test_paraphrasing_tool_add_adj_fail():
    word = ParaphrasingTool('niogenoio')
    assert word.add_adj() == 'niogenoio'
