from hello import hello


def test_hello():
    assert hello('bob') == 'hello bob!'
