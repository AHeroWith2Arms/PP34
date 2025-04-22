import datetime
import functools
from typing import Any, Callable


def log(file_path: str = None) -> Callable:
    """
    Декоратор для логирования вызова функции и результата.

    :param file_path: (опционально) Имя файла для записи логов.
                     Если не указано, логи выводятся в консоль.
    """
    # Определение функции-декоратора
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Получение текущей временной метки
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                result = func(*args, **kwargs)
                log_msg = f"{timestamp} {func.__name__} выполнено успешно"
            except Exception as e:
                result = None
                # Форматирование сообщения об ошибке
                log_msg = (
                    f"{timestamp} {func.__name__} ошибка: "
                    f"{type(e).__name__}. Входные данные: {args}, {kwargs}"
                )

            # Запись лога в файл или вывод в консоль
            if file_path:
                with open(file_path, "a") as file:
                    file.write(log_msg + "n")
            else:
                print(log_msg)

            return result

        return wrapper

    return decorator


# Примеры использования

@log(file_path="mylog.txt")
def my_function(x: int, y: int) -> int:
    """Пример простой функции для тестирования декоратора."""
    return x + y


if __name__ == "__main__":
    my_function(1, 2)  # Логирование будет выполняться в файл 'mylog.txt'