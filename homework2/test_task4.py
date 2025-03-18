from homework2.task4 import cache


def test_cache_works():
    """Testing that cache function caches function calls"""

    def my_func(a, b):
        return (a**b) ** 2

    cached = cache(my_func)
    v1 = cached(22, 33)
    v2 = cached(22, 33)

    assert v1 is v2
