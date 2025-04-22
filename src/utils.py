import json
import os
from pathlib import Path
from typing import Any, Dict, List
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("api_key")

def read_transactions(file_path: Path) -> List[Dict[str, Any]]:
    """Считывает транзакции из JSON-файла."""
    try:
        with file_path.open(encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError):
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
        print(f"Ошибка API: {api_error}")
        return 1.0

def sum_amount(transactions: List[dict]) -> float:
    """Суммирует суммы всех транзакций"""
    total_sum = 0.0
    for transaction in transactions:
        amount_info = transaction.get("operationAmount", {})
        currency_code = amount_info.get("currency", {}).get("code")
        amount_value = float(amount_info.get("amount", 0))
        if currency_code == "RUB":
            total_sum += amount_value
        elif currency_code in ("EUR", "USD"):
            exchange_rate = get_transaction_rub(currency_code)
            total_sum += amount_value * exchange_rate
        else:
            print(f"Неизвестная валюта: {currency_code}")
    return total_sum
