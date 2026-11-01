"""Читання інформації про котів з текстового файлу."""

import pathlib


def get_cats_info(path):
    """
    Повертає список словників з інформацією про котів з файлу path.

    Формат рядка: "id,ім'я,вік". Кожен словник має ключі "id", "name", "age"
    (значення зберігаються рядками, як в очікуваному результаті).
    Некоректні рядки пропускаються. Якщо файл недоступний, повертає [].
    """
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue

                try:
                    cat_id, name, age = (part.strip() for part in line.split(","))
                except ValueError:
                    print(f"Рядок {line_number} пропущено (невірний формат): {line!r}")
                    continue

                if not (cat_id and name and age):
                    print(f"Рядок {line_number} пропущено (порожнє поле): {line!r}")
                    continue

                cats.append({"id": cat_id, "name": name, "age": age})

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return []
    except (UnicodeDecodeError, OSError) as e:
        print(f"Помилка під час читання файлу: {e}")
        return []

    return cats


def print_cats(cats):
    """Друкує список словників: кожен словник в окремому рядку з відступом."""
    print("[")
    for cat in cats:
        # {{ і }} дають літеральні дужки, а {cat["id"]} підставляє значення
        print(
            f'    {{"id": "{cat["id"]}", "name": "{cat["name"]}", '
            f'"age": "{cat["age"]}"}},'
        )
    print("]")


def main():
    """Точка входу: читає cats_file.txt поруч зі скриптом і виводить результат."""
    path = pathlib.Path(__file__).parent / "cats_file.txt"
    cats_info = get_cats_info(path)
    print_cats(cats_info)


if __name__ == "__main__":
    main()
    