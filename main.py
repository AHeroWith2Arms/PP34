import os

from src import files_reader, generators, proccesing, utils, widget, collection


def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print(
        """1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )

    while True:
        try:
            file_type = int(input())
            break
        except Exception:
            print("Введите корректное число")

    while True:
        if file_type == 1:
            print("Для обработки выбран JSON-файл.")
            break
        elif file_type == 2:
            print("Для обработки выбран CSV-файл.")
            break
        elif file_type == 3:
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Введите корректное число")
            file_type = int(input())

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.",
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING",
        )
        state = str(input())
        statuses = ["EXECUTED", "CANCELED", "PENDING"]
        if state.upper() not in statuses:
            print(f'Статус операции "{state}" недоступен')
        else:
            break

    print(f'Операции отфильтрованы по статусу "{state.upper()}"')

    print("Отсортировать операции по дате? Да/Нет")
    while True:
        data_sort = str(input())
        if data_sort.lower() not in ["да", "нет"]:
            print("Напиши да или нет")
        else:
            break
    if data_sort.lower() == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        while True:
            inc_sort = str(input())
            if inc_sort.lower() not in ["по возрастанию", "по убыванию"]:
                print("Напиши по возрастанию или по убыванию")
            else:
                break

    print("Выводить только рублевые транзакции? Да/Нет")
    while True:
        rub_sort = str(input())
        if rub_sort.lower() not in ["да", "нет"]:
            print("Напиши да или нет")
        else:
            break

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    while True:
        word_sort = str(input())
        if word_sort.lower() not in ["да", "нет"]:
            print("Напиши да или нет")
        else:
            if word_sort.lower() in ["да"]:
                print("Напиши слово для фильтрации")
                word = str(input())
            break

    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")

    if file_type == 1:
        file_path = os.path.join(data_dir, "operations.json")
        file = utils.get_transaction(file_path)
    elif file_type == 2:
        file_path = os.path.join(data_dir, "transactions.csv")
        file = files_reader.CSV_file_read(file_path)
        print(file)
    elif file_type == 3:
        file_path = os.path.join(data_dir, "transactions_excel.xlsx")
        file = files_reader.XLSX_file_read(file_path)

    file = proccesing.filter_by_state(file, state)

    if data_sort.lower() in ["да"]:
        if inc_sort in ["по убыванию"]:
            file = proccesing.sort_by_date(file, True)
        else:
            file = proccesing.sort_by_date(file, False)

    if rub_sort.lower() in ["да"]:
        if file_type == 1:
            file = generators.filter_by_currency_json(file, "RUB")
        else:
            file = generators.filter_by_currency_csvxlsx(file, "RUB")

    if word_sort.lower() in ["да"]:
        file = collection.description_filter(file, word)

    print("Распечатываю итоговый список транзакций... \n")

    if file is not None:
        print(f"Всего банковских операций в выборке: {len(file)} \n")
        if file_type == 1:
            for i in file:
                print(widget.get_date(i["date"]), i["description"])
                if i["description"] == "Открытие вклада":
                    print(widget.mask_account_card(i["to"]))
                else:
                    print(widget.mask_account_card(i["from"]), "->", widget.mask_account_card(i["to"]))
                print(
                    "Сумма:",
                    round(float(i["operationAmount"]["amount"])),
                    i["operationAmount"]["currency"]["name"] + "\n",
                )
        else:
            for i in file:
                print(widget.get_date(i["date"]), i["description"])
                if i["description"] == "Открытие вклада":
                    print(widget.mask_account_card(i["to"]))
                else:
                    print(widget.mask_account_card(i["from"]), "->", widget.mask_account_card(i["to"]))
                print("Сумма:", round(float(i["amount"])), i["currency_name"] + "\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


main()
