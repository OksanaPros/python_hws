from unittest.mock import Mock

from homework3.task1 import cache


def test_cache_works():
    """Testing that cache function caches function calls several times"""

    mock = Mock(return_value=2**123)
    cached_mock = cache(times=2)(mock)

    v1, v2, v3, v4 = (cached_mock(2**123) for _ in range(4))

    assert (v1 is v2) and (v1 is v3) and not (v1 is v4)
