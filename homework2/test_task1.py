from homework2.task1 import count_punctuation_chars, get_longest_diverse_words


def test_get_longest_diverse_words():
    answer = [
        "Insubstantialities",
        "Circumlocutionary",
        "ddddddddddddddddd",
        "Magniloquent",
        "favorite",
        "flowers",
        "hjkdjh",
        "words",
        "name",
        "love",
    ]
    assert get_longest_diverse_words("./test_data.txt") == answer


def test_count_punctuation_chars():
    assert count_punctuation_chars("./test_data.txt") == 15
