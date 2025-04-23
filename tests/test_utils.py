import os
from unittest.mock import Mock, patch
from pathlib import Path
from src.utils import read_transactions, get_transaction_rub


def test_json_transactions() -> None:
    test_wrong_way = Path("C:/Users/user1/PycharmProjects/PP34/tests/test_operations.json")


    assert read_transactions(test_wrong_way) == []
