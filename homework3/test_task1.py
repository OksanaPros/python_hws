import pytest

from homework3.task1 import cache

def test_cache_works():
    """Testing that cache function caches function calls several times"""

    @cache(times=2)
    def f(a):
        return a

    v1, v2, v3, v4 = (f(2**123) for _ in range(4))

    assert (v1 is v2) and (v1 is v3) and not (v1 is v4)