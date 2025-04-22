import os

import pytest

from src.decorators import log


@pytest.fixture(autouse=True)
def cleanup():
    """
    Фикстура для очистки файлов после каждого теста.
    """
    yield
    for filename in ["test_log_4.txt", "test_log_5.txt", "test_log_6.txt"]:
        if os.path.exists(filename):
            os.remove(filename)


def test_decorator_with_file_logging():
    """
    Тестирование декоратора с логированием в файл.
    """

    @log(filename="test_log_4.txt")
    def add_numbers(x, y):
        return x + y

    add_numbers(10, 20)

    with open("test_log_4.txt", "r") as f:
        lines = f.readlines()
        assert len(lines) == 1
        expected_output = f"add_numbers okn"
        assert lines[0].startswith(expected_output[:8])


def test_decorator_without_file_logging(capsys):
    """
    Тестирование декоратора без логирования в файл.
    """

    @log()
    def subtract_numbers(x, y):
        return x - y

    subtract_numbers(30, 15)

    captured = capsys.readouterr()
    expected_output = f"subtract_numbers okn"
    assert captured.out.startswith(expected_output[:17])


def test_decorator_with_exception(capsys):
    """
    Тестирование декоратора с исключением и логированием в файл.
    """

    @log(filename="test_log_5.txt")
    def divide_numbers(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

    with open("test_log_5.txt", "r") as f:
        lines = f.readlines()
        assert len(lines) == 1
        expected_output = f"divide_numbers error: ZeroDivisionError. Inputs: (10, 0), {1}n"
        assert lines[0].startswith(expected_output[:32])


# Дополнительные тесты

def test_decorator_with_no_arguments(capsys):
    """
    Дополнительный тест: декоратор без аргументов.
    """

    @log()
    def greet():
        print("Hello, World!")

    greet()

    captured = capsys.readouterr()
    expected_output = f"greet okn"
    assert captured.out.startswith(expected_output[:9])


def test_decorator_with_keyword_arguments(capsys):
    """
    Дополнительный тест: декоратор с ключевыми аргументами.
    """

    @log()
    def calculate_area(width=10, height=20):
        return width * height

    calculate_area(height=30, width=40)

    captured = capsys.readouterr()
    expected_output = f"calculate_area okn"
    assert captured.out.startswith(expected_output[:15])


def test_decorator_with_nested_calls(capsys):
    """
    Дополнительный тест: вложенные вызовы функций с декоратором.
    """

    @log()
    def inner_function():
        pass

    @log()
    def outer_function():
        inner_function()

    outer_function()

    captured = capsys.readouterr()
    expected_output_inner = f"inner_function okn"
    expected_output_outer = f"outer_function okn"
    assert expected_output_inner in captured.out
    assert expected_output_outer in captured.out


def test_decorator_with_multiple_args_and_kwargs(capsys):
    """
    Дополнительный тест: декоратор с несколькими аргументами и ключевыми аргументами.
    """

    @log()
    def complex_operation(a, b, c=3, d=4):
        return a + b + c + d

    complex_operation(1, 2, d=6)

    captured = capsys.readouterr()
    expected_output = f"complex_operation okn"
    assert captured.out.startswith(expected_output[:18])