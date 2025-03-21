"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    def cache_func(*args, cache_dict=dict()):
        if args in cache_dict.keys():
            return cache_dict[args]
        res = func(*args)
        cache_dict[args] = res
        return res

    return cache_func
