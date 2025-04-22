from src.masks import mask_account_number, mask_card_number

"""
Тестирование функции mask_card_number:
"""


def test_mask_card_number() -> None:
    assert mask_card_number("1234567891234567") == "1234 56** **** 4567"
    assert mask_card_number("12345") == "Некорректный номер карты"


"""
Тестирование функции mask_account_number:
"""


def test_mask_account_number() -> None:
    assert mask_account_number("76666108430178874305") == "**4305"
    assert mask_account_number("234") == "Некорректный номер счета"
