"""Підрахунок загальної та середньої зарплати розробників з текстового файлу."""

import pathlib


def total_salary(path):
    """
    Повертає кортеж (загальна сума, середня зарплата) з файлу path.

    Формат рядка: "Ім'я Прізвище,зарплата". Некоректні рядки пропускаються.
    Якщо файл недоступний або не містить коректних даних, повертає (0, 0).
    """
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue

                try:
                    _, salary = line.split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Рядок {line_number} пропущено (невірний формат): {line!r}")

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return 0, 0
    except (UnicodeDecodeError, OSError) as e:
        print(f"Помилка під час читання файлу: {e}")
        return 0, 0

    if count == 0:
        return 0, 0

    return total, total // count


def main():
    """Точка входу: читає salary_file.txt поруч зі скриптом і виводить результат."""
    path = pathlib.Path(__file__).parent / "salary_file.txt"
    total, average = total_salary(path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


if __name__ == "__main__":
    main()
    