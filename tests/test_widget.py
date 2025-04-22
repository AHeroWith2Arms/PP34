from src.widget import format_date, mask_card_and_account_info

"""
тестирование функции mask_card_and_account_info
"""


def test_mask_card_and_account_info() -> None:
    assert mask_card_and_account_info("Счет 12345678901234567890") == "1234 **567890"
    assert mask_card_and_account_info("Card Visa 4111 1111 1111 1111") == "Card Visa 4111 11** **** 1111"


"""
Тест функции format_date
"""


def test_format_date() -> None:
    assert format_date("2023-10-05") == "05.10.2023"
