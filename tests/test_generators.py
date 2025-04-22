import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture()
def dict_list_with_currency() -> list[dict]:
    return [
        {"id": 432432883, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
        {"id": 123445667, "operationAmount": {"currency": {"name": "RUB", "code": "RUB"}}},
        {"id": 873234345, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
        {"id": 983243242, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
    ]


@pytest.mark.parametrize(
    "currency_code, expected_ids", [("USD", [432432883, 873234345, 983243242]), ("RUB", [123445667])]
)
def test_filter_by_currency(dict_list_with_currency: list[dict], currency_code: str, expected_ids: list[int]) -> None:
    """Проверяет правильность фильтрации по валюте"""
    result = list(filter_by_currency(dict_list_with_currency, currency_code))
    assert len(result) == len(expected_ids)
    assert all(r["id"] in expected_ids for r in result)
    assert all(r["operationAmount"]["currency"]["code"] == currency_code for r in result)


@pytest.fixture()
def dict_list_for_descriptions() -> list[dict]:
    return [
        {"id": 1, "description": "Перевод со счета на счет"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3, "description": "Перевод со счета на счет"},
        {"id": 4, "description": "Перевод со счета на счет"},
        {"id": 5, "description": "Перевод с карты на карту"},
    ]


@pytest.mark.parametrize("expected_descriptions", [["Перевод со счета на счет"] * 4 + ["Перевод организации"]])
def test_transaction_descriptions(dict_list_for_descriptions: list[dict], expected_descriptions: list[str]) -> None:
    """Проверяет правильность работы генератора"""
    result = list(transaction_descriptions(dict_list_for_descriptions))
    assert result == expected_descriptions


@pytest.mark.parametrize("count", range(100))
def test_card_number_generator(count: int) -> None:
    """Тест генератора номеров карт"""
    card_number: int = card_number_generator()

    assert 4000000000000000 <= card_number <= 4999999999999999
    assert len(str(card_number)) == 16
    assert str(card_number).isdigit()
