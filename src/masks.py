def mask_card_number(card_number: str) -> str:
    """Возвращает маску номера карты."""
    cleaned_number = "".join(char for char in card_number if char.isdigit())
    masked_number = "{} {}** **** {}".format(cleaned_number[:4], cleaned_number[6:8], cleaned_number[-4:])
    return masked_number


def mask_account_number(account_number: str) -> str:
    """Возвращает маску номера счета."""
    masked_account = "**{}".format(account_number[-4:])
    return masked_account


def main() -> None:
    n = input("Введите номер карты или номер счета: ")
    masked_card = mask_card_number(n)

    print("Маскированный номер карты:", masked_card)


if __name__ == "__main__":
    main()
