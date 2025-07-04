from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов: {func.__name__}({', '.join(map(repr, args))})")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result

    return wrapper
