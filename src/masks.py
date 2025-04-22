import logging

# Настраиваем логгер
logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8",
                                   mode="a")  # режим 'a' означает append (добавление записей)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def mask_card_number(card_number: str) -> str:
    """
    Возвращает маскированную версию номера банковской карты.
    Формат маски: ХХХХ XX** **** ХХХХ
    """
    cleaned_number = ''.join(char for char in card_number if char.isdigit())  # удаляем лишние символы
    masked_number = '{} {}'.format(cleaned_number[:4], '*' * len(cleaned_number[4:-4])) + ' {}'.format(
        cleaned_number[-4:])
    logger.info('Маска карты создана успешно')
    return masked_number


def mask_account_number(account_number: str) -> str:
    """
    Возвращает маскированную версию банковского счёта.
    Формат маски: **XXXX
    """
    masked_account = '**{}'.format(account_number[-4:])
    logger.info('Маска счёта создана успешно')
    return masked_account


def main():
    while True:
        user_input = input("Введите номер карты или счёт (или введите 'exit', чтобы выйти): ").strip()
        if user_input.lower() == 'exit':
            break
        elif len(user_input.strip()) > 0:
            masked_card_or_account = ''
            if any(c.isalpha() for c in user_input):
                logger.warning('Номер карты/счета содержит буквы! Проверяйте ввод.')
                continue
            elif len(user_input) >= 16:
                masked_card_or_account = mask_card_number(user_input)
            else:
                masked_card_or_account = mask_account_number(user_input)

            print("Маскированная карта/счёт:", masked_card_or_account)
        else:
            logger.warning('Пользователь ничего не ввёл!')


if __name__ == "__main__":
    main()
