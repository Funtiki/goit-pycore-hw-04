"""Візуалізує структуру директорії в терміналі з використанням кольорів."""

import sys
from pathlib import Path

from colorama import Fore, init


def print_tree(directory, prefix=" "):
    """
    Рекурсивно виводить вміст директорії directory у вигляді дерева.

    Директорії виводяться синім кольором, файли - зеленим.
    prefix - початок рядка, що малює вертикальні лінії батьківських рівнів.
    """
    try:
        # Спочатку директорії, потім файли; всередині груп - за алфавітом
        items = sorted(
            directory.iterdir(),
            key=lambda item: (not item.is_dir(), item.name.lower()),
        )
    except PermissionError:
        # Немає прав на читання: повідомляємо і йдемо далі, не падаємо
        print(f"{prefix}┗ {Fore.RED}[доступ заборонено]")
        return

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "┗" if is_last else "┣"  # останній елемент закриває гілку

        if item.is_dir():
            print(f"{prefix}{connector} {Fore.BLUE}📂{item.name}")
            # Символічні посилання не відкриваємо, інакше можливий нескінченний цикл
            if not item.is_symlink():
                # Під останнім елементом вертикальна лінія вже не потрібна
                extension = "  " if is_last else "┃ "
                print_tree(item, prefix + extension)  # рекурсивний виклик
        else:
            print(f"{prefix}{connector} {Fore.GREEN}📜{item.name}")


def main():
    """Точка входу: перевіряє шлях з аргументу і виводить дерево директорії."""
    # sys.argv[0] - ім'я скрипта, sys.argv[1] - шлях, тому очікуємо рівно 2 елементи
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python task_04_3.py <шлях_до_директорії>", file=sys.stderr)
        sys.exit(1)  # ненульовий статус виходу означає помилку

    root = Path(sys.argv[1])

    if not root.exists():
        print(f"{Fore.RED}Помилка: шлях не існує: {root}", file=sys.stderr)
        sys.exit(1)
    if not root.is_dir():
        print(f"{Fore.RED}Помилка: шлях не веде до директорії: {root}", file=sys.stderr)
        sys.exit(1)

    # Абсолютний шлях: для "." ім'я папки інакше було б порожнім
    root = root.resolve()
    print(f"{Fore.BLUE}📦{root.name or root}")
    print_tree(root)


if __name__ == "__main__":
    # autoreset=True скидає колір після кожного print, тож колір не "протікає" далі
    init(autoreset=True)
    main()
    