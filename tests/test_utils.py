from unittest.mock import Mock

from src.utils import read_transactions


def test_json_transactions(test_json):

    test_by_mock_way = Mock(return_value=r"../PP34/data/operations.jso")
    test_way = r"../PP34/data/operations.json"
    test_wrong_way = r"../PP34/tests/test_operations.json"

    assert read_transactions(test_by_mock_way) == []
    assert read_transactions(test_way) == test_json
    assert read_transactions(test_wrong_way) == []