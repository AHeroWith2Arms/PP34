from src.masks import mask_account_number, mask_card_number

"""
Тестирование функции mask_card_number:
"""


def test_mask_card_number() -> None:
    assert mask_card_number("1234 5678 9101 2345") == "1234 ******** 2345"


"""
Тестирование функции mask_account_number:
"""


def test_mask_account_number() -> None:
    assert mask_account_number("76666108430178874305") == "**4305"

