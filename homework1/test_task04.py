import pytest

from homework1.task04 import check_sum_of_four

def test_tuples_exist():
    """Testing that the function returns the correct result"""
    assert check_sum_of_four(a = [1, 2], b = [3, 4], c = [-4, -6], d = [0, 0]) == 4

def test_zero_tuples():
    """Testing that the function returns 0 if such tuples don't exist"""
    assert check_sum_of_four(a=[1, 2], b=[3, 4], c=[5, 6], d=[7, 8]) == 0