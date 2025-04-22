import json
import os
from pathlib import Path
from typing import Any, Dict, List
import requests
from dotenv import load_dotenv
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

load_dotenv()
API_KEY = os.getenv("api_key")


def read_transactions(file_path: Path) -> List[Dict[str, Any]]:
    """Считывает транзакции из JSON-файла."""
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        else:
            logger.warning("Файл %s содержит неверный формат данных.", file_path)
            return []
    except FileNotFoundError:
        logger.error("Файл %s не найден.", file_path)
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования файла %s.", file_path)
        return []


def get_transaction_rub(currency: str) -> Any:
    """Получает курс валюты от API и возвращает его в виде float"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
    try:
        response = requests.get(url, headers={"apikey": API_KEY}, timeout=5)
        response.raise_for_status()
        response_data = response.json()
        rate = response_data["rates"]["RUB"]
        return rate
    except requests.exceptions.RequestException as api_error:
        logger.error("Ошибка API при получении курса валюты (%s): %s", currency, api_error)
        return 1.0


def sum_amount(transaction: dict) -> None or float:
    """Сумма транзакции"""
    amount_info = transaction.get("operationAmount", {})
    currency_code = amount_info.get("currency", {}).get("code")
    amount_value = float(amount_info.get("amount", 0))

    if currency_code == "RUB":
        return amount_value

    elif currency_code in ("EUR", "USD"):
        exchange_rate = get_transaction_rub(currency_code)
        return exchange_rate
    else:
        logger.warning("Обнаружена неизвестная валюта: %s", currency_code)
    return None