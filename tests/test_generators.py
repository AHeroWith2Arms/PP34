import pytest
import random
from typing import List, Iterator, Generator
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

sample_transactions = [
    {"operationAmount": {"currency": {"code": "USD"}}, "description": "Purchase 1"},
    {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Purchase 2"},
    {"operationAmount": {"currency": {"code": "USD"}}, "description": "Purchase 3"},
]

def test_filter_by_currency() -> None:
    filtered_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(filtered_transactions) == 2
    assert filtered_transactions[0]["operationAmount"]["currency"]["code"] == "USD"
    assert filtered_transactions[1]["operationAmount"]["currency"]["code"] == "USD"

def test_transaction_descriptions() -> None:
    descriptions = list(transaction_descriptions(sample_transactions))
    assert len(descriptions) == 3
    assert "Purchase 1" in descriptions
    assert "Purchase 2" in descriptions
    assert "Purchase 3" in descriptions

def test_card_number_generator() -> None:
    card_gen = card_number_generator(1, 5)
    generated_cards = [next(card_gen) for _ in range(5)]
    assert len(generated_cards) == 5
    assert all(len(card) == 19 for card in generated_cards)