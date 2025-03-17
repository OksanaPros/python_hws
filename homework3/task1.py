from typing import Callable

def cache(times: int):
    def cache_decorator(func: Callable) -> Callable:
        counter = times
        def cache_func(*args, cache_dict = dict()):
            nonlocal times, counter
            if args in cache_dict.keys():
                while counter:
                    counter -= 1
                    return cache_dict[args]
            res = func(*args)
            counter = times
            cache_dict[args] = res
            return res
        return cache_func
    return cache_decorator