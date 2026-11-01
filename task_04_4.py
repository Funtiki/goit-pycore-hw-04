"""
Консольний бот-помічник для управління книгою контактів.
Дозволяє додавати, змінювати, шукати номери телефонів та переглядати всі збережені контакти.
"""

def parse_input(user_input):
    """
    Розбирає введений користувачем рядок на команду та її аргументи.

    Аргументи:
        user_input (str): Рядок вводу користувача.

    Повертає:
        tuple: Кортеж, де перший елемент — команда (str), а решта — аргументи (list).
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Додає новий контакт до словника контактів.

    Аргументи:
        args (list): Список аргументів, що містить ім'я та номер телефону.
        contacts (dict): Словник для зберігання контактів.

    Повертає:
        str: Повідомлення про успішне додавання контакту.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Змінює номер телефону для існуючого контакту.

    Аргументи:
        args (list): Список аргументів, що містить ім'я та новий номер телефону.
        contacts (dict): Словник для зберігання контактів.

    Повертає:
        str: Повідомлення про оновлення контакту або помилку, якщо ім'я не знайдено.
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    """
    Виводить номер телефону за вказаним ім'ям контакту.

    Аргументи:
        args (list): Список аргументів, що містить ім'я контакту.
        contacts (dict): Словник для зберігання контактів.

    Повертає:
        str: Номер телефону або повідомлення про помилку, якщо ім'я не знайдено.
    """
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    """
    Виводить усі збережені контакти з їхніми номерами телефонів.

    Аргументи:
        contacts (dict): Словник для зберігання контактів.

    Повертає:
        str: Відформатований рядок з усіма записами або повідомлення про їх відсутність.
    """
    if not contacts:
        return "No contacts saved."

    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    """
    Головна функція програми, яка керує основним циклом обробки команд бота.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        # Захист від порожнього вводу, щоб програма не падала на split()
        if not user_input.strip():
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
