import random
from typing import Any, Generator, Iterator, List


def filter_by_currency(transactions: List[dict], currency: str = "USD") -> Iterator[dict]:
    """Функция,принимает список словарей и возвращает операции, в которых указана валюта"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[dict]) -> Generator[str, None, None]:
    """Генератор, принимает список словарей и возращает по очереди в нужном формате"""
    for transaction in transactions:
        yield str(transaction.get("description"))


def card_number_generator(start: int, end: int) -> Generator[str, Any, None]:
    """Генератор номеров банковских карт в нужном формате"""
    for _ in range(start, end + 1):
        card_number = "".join([str(random.randint(0, 9)) for _ in range(16)])
        yield " ".join([card_number[i : i + 4] for i in range(0, len(card_number), 4)])
