from paraphrasing.paraphrase import Paraphrase


def test_paraphrase_amount():
    text = ['Not', 'at', 'Home', 'to',
            'Callers\n', 'Says', 'the', 'Naked',
            'Tree', '--\n', 'Bonnet', 'due', 'in',
            'April', '--\n', 'Wishing', 'you', 'Good',
            'Day', '--\n']
    parap = Paraphrase(text, 40)
    assert parap.how_much_paraphrase() == 8


def test_qualify_to_parap():
    text = ['Not', 'at', 'Home', 'to',
            'Callers\n', 'Says', 'the', 'Naked',
            'Tree', '--\n', 'Bonnet', 'due', 'in',
            'April', '--\n', 'Wishing', 'you', 'Good',
            'Day', '--\n']
    parap = Paraphrase(text, 40)
    qualified = ['Home', 'Says', 'Naked',
                 'Tree', 'Bonnet', 'due',
                 'April', 'Wishing', 'Good',
                 'Day']
    assert parap.qualify_to_paraphrase() == qualified


def test_choose_to_parap():
    text = ['Not', 'at', 'Home', 'to',
            'Callers\n', 'Says', 'the', 'Naked',
            'Tree', '--\n', 'Bonnet', 'due', 'in',
            'April', '--\n', 'Wishing', 'you', 'Good',
            'Day', '--\n']
    parap = Paraphrase(text, 10)
    chosen = parap.choose_what_paraphrase()
    assert len(chosen) == 2
    for word in chosen:
        assert word in text


def test_paraphrase(monkeypatch):
    def aut_choose(a):
        return ['Bonnet', 'April', 'Tree', 'Good']
    text = ['Not', 'at', 'Home', 'to',
            'Callers\n', 'Says', 'the', 'Naked',
            'Tree', '--\n', 'Bonnet', 'due', 'in',
            'April', '--\n', 'Wishing', 'you', 'Good',
            'Day', '--\n']
    parap = Paraphrase(text, 10)
    monkeypatch.setattr('paraphrasing.paraphrase.Paraphrase.choose_what_paraphrase', aut_choose)
    expected = ['Not', 'at', 'Home', 'to', 'Callers\n',
                'Says', 'the', 'Naked', 'large Tree', '--\n',
                'hood', 'due', 'in', 'early April', '--\n',
                'Wishing', 'you', 'right', 'Day', '--\n']
    assert parap.paraphrase() == expected


