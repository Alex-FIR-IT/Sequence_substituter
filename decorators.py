from functools import wraps


def retry(func):
    @wraps(wrapped=func)
    def wrapper(*args, **kwargs):
        result = None

        while not result:
            try:
                result = func(*args, **kwargs)
            except FileNotFoundError:
                print("Файл не найден!")
                continue
            except Exception as error:
                print(f"Неизвестная ошибка - {error}")

        return result

    return wrapper
