from functools import wraps


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                raise ValueError("Все аргументы должны быть положительными")
        result = func(*args, **kwargs)
        return result

    return wrapper
