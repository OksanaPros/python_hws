"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
from string import punctuation, ascii_letters

def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path) as file:
        text = file.read().splitlines()

    only_words = list()
    for item in text:
        item = "".join([char for char in item if char in ascii_letters + " "])
        only_words.extend(item.split(" "))

    only_words.sort(key=lambda item: (-len(item), -len(set(item))))
    return only_words[:10]

def count_punctuation_chars(file_path: str) -> int:
    with open(file_path) as file:
        text = " ".join(file.read().splitlines())

    res = 0

    for char in text:
        if char in punctuation:
            res += 1

    return res