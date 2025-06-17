from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(args)
        if args not in cache.keys():
            result = func(*args, **kwargs)
            cache[args] = result
        else:
            print("Из кэша")
            return cache[args]
        return result

    return wrapper
