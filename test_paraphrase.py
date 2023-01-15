from paraphrase import Paraphrase


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
    qualified = ['Not', 'at', 'Home', 'to',
                 'Says', 'the', 'Naked',
                 'Tree', 'Bonnet', 'due', 'in',
                 'April', 'Wishing', 'Good',
                 'Day']
    assert parap.qualify_to_paraphrase() == qualified
