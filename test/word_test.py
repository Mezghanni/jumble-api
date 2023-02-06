from app.word import Word


def test_jumble_word():
    input_word = "test"
    word = Word.parse_obj({'word': input_word})
    assert input_word != word.jumble()


def test_jumble_word_single_character():
    input_word = "a"
    word = Word.parse_obj({'word': input_word})
    assert input_word == word.jumble()
