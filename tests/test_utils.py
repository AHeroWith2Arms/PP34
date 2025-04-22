from unittest.mock import Mock, patch
from pathlib import Path
from src.utils import read_transactions, get_transaction_rub


def test_json_transactions(test_json: list) -> None:
    test_by_mock_way = Mock(return_value=Path("../PP34/data/operations.json"))
    test_way = Path("../PP34/data/operations.json")
    test_wrong_way = Path("../PP34/tests/test_operations.json")

    assert read_transactions(test_by_mock_way()) == []
    assert read_transactions(test_way) == test_json
    assert read_transactions(test_wrong_way) == []


@patch("requests.get")
def test_get_transaction_rub(mock_get) -> None:
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75.8}}
    assert get_transaction_rub("USD") == 75.8

    mock_get.side_effect = Exception("API Error")
    assert get_transaction_rub("EUR") == 1.0