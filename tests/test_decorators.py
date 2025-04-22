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

    with open("test_log_4.txt", "r") as file:
        lines: List[str] = file.readlines()
        assert len(lines) == 1
        expected_output: str = "add_numbers ok\n"
        assert lines[0].startswith(expected_output[:8])


def test_decorator_without_file_logging(capsys: pytest.CaptureFixture) -> None:
    """
    Тестирование декоратора без логирования в файл.
    """

    @log()
    def subtract_numbers(x: int, y: int) -> int:
        return x - y

    subtract_numbers(30, 15)

    captured_out, captured_err = capsys.readouterr()
    expected_output: str = "subtract_numbers ok\n"
    assert captured_out.startswith(expected_output[:17])


def test_decorator_with_exception(capsys: pytest.CaptureFixture) -> None:
    """
    Тестирование декоратора с исключением и логированием в файл.
    """

    @log()
    def divide_numbers(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

    with open("test_log_5.txt", "r") as file:
        lines: List[str] = file.readlines()
        assert len(lines) == 1
        expected_output: str = "divide_numbers error: ZeroDivisionError. Inputs: (10, 0),\n"
        assert lines[0].startswith(expected_output[:32])
