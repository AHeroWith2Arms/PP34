import pandas as pd


def csv_reader(filename: str) -> list:
    """Читает csv файл по заданному пути"""
    if filename.endswith(".csv"):
        try:
            data = pd.read_csv(filename, sep=";")
            return data.to_dict("records")
        except FileNotFoundError:
            return []
    else:
        return []


def excel_reader(filename: str) -> list:
    """Читает xlsx файл по переданному пути"""
    if filename.endswith(".xlsx") or filename.endswith(".xls"):
        try:
            data = pd.read_excel(filename)
            return data.to_dict("records")
        except FileNotFoundError:
            return []
    else:
        return []