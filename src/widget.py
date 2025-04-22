def mask_card_and_account_info(info: str) -> str:
    """
    Возвращает маскированные данные, как номер карты и счета.
    Если информация содержит слово "Счет" или "Счёт", маскирует счет,
    иначе - маскирует номер карты.
    """
    card_number = ""
    name_card = ""
    if "Счёт" in info or "Счет" in info:
        score_number = info[5:]
        number_mask = f"{info[:4]} **{score_number[-4:]}"
        return number_mask
    else:
        for i in range(len(info)):
            if info[i].isalpha() or info[i] == " ":
                name_card += info[i]
            else:
                card_number += info[i]

        correct_number = card_number[0:7] + card_number[7:14] + card_number[14:19]
        number_mask = (
            f"{name_card} {correct_number[:4]} {correct_number[4:6]}** **** {correct_number[12:16]}"
        )

        return number_mask


def format_date(input_date: str) -> str:
    """
    Преобразует дату из формата YYYY-MM-DD в формат DD.MM.YYYY.
    """
    correct_date = f"{input_date[8:10]}.{input_date[5:7]}.{input_date[0:4]}"
    return correct_date


user_input = input("Введите информацию о карте или счете: ")
print(mask_card_and_account_info(user_input))
