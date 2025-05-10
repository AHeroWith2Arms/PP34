import os
from typing import List, Tuple, Generator
import pytest
from src.decorators import log


@pytest.fixture(autouse=True)
def cleanup() -> Generator:
    """
    Фикстура для очистки файлов после каждого теста.
    """
    yield
    filenames: List[str] = ["test_log_4.txt", "test_log_5.txt", "test_log_6.txt"]
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)


def test_decorator_with_file_logging() -> None:
    """
    Тестирование декоратора с логированием в файл.
    """
    @log()
    def add_numbers(x: int, y: int) -> int:
        return x + y

    add_numbers(10, 20)

