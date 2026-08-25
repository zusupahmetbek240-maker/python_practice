import json

print("=== 1. БЕЗОПАСНОЕ ПОЛУЧЕНИЕ ИЗ СПИСКА ===")
# функция достает элемент по индексу; если индекса нет или передан не список — возвращает None
def safe_list_get(lst, index):
    try:
        return lst[index]
    except (IndexError, TypeError):
        return None

items = ["яблоко", "банан", "груша"]
print("элемент по индексу 1:", safe_list_get(items, 1))
print("несуществующий индекс:", safe_list_get(items, 99))


print("\n=== 2. БЕЗОПАСНОЕ ПОЛУЧЕНИЕ ИЗ СЛОВАРЯ ===")
# функция достает значение по ключу; если ключа нет или передан не словарь — возвращает None
def safe_dict_get(d, key):
    try:
        return d[key]
    except (KeyError, TypeError):
        return None

person = {"name": "Akhmetbek", "city": "Uralsk"}
print("город:", safe_dict_get(person, "city"))
print("возраст (нет ключа):", safe_dict_get(person, "age"))


print("\n=== 3. БЕЗОПАСНАЯ КОНВЕРТАЦИЯ В ДРОБНОЕ ЧИСЛО ===")
# пробует привести к float; при несовместимом типе или кривой строке возвращает 0.0
def safe_to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0

print("строка 60 ->", safe_to_float("60"))
print("число 123 ->", safe_to_float(123))
print("None ->", safe_to_float(None))
print("невалидный текст ->", safe_to_float("сергей"))


print("\n=== 4. БЕЗОПАСНЫЙ ПОДСЧЕТ ДЛИНЫ ===")
# возвращает длину объекта; если тип не поддерживает len() — возвращает 0
def safe_str_len(value):
    try:
        return len(value)
    except TypeError:
        return 0

print("длина числа 123 ->", safe_str_len(123))
print("длина кортежа ->", safe_str_len((1, 2)))
print("длина строки ->", safe_str_len("665"))


print("\n=== 5. БАЗОВАЯ РАБОТА С ТЕКСТОВЫМ ФАЙЛОМ ===")
# запись двух строк в текстовый файл
with open("user.txt", "w", encoding="utf-8") as f:
    f.write("Akhmetbek\n")
    f.write("Уральск\n")

# чтение содержимого файла целиком
with open("user.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("содержимое user.txt:")
print(content.strip())


print("=== 6. РАБОТА С JSON И БЕЗОПАСНОЕ ЧТЕНИЕ ===")
user_profile = {
    "nickname": "figeron1020qq",
    "prof_lvl": 10,
    "games": ["Resident 2 Remake", "Alan Wake"],
    "is_active": True
}

# сериализация словаря в json-файл с отступами
with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(user_profile, f, ensure_ascii=False, indent=4)

# чтение json с перехватом отсутствия файла и битого синтаксиса
def safe_load_profile(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return "Файл не найден"
    except json.JSONDecodeError:
        return "Файл поврежден"

loaded_prof = safe_load_profile("profile.json")
print("успешная загрузка:", loaded_prof)
print("тест ошибки отсутствия файла:", safe_load_profile("reg_data.json"))
print("тип данных:", type(loaded_prof))
print("уровень профиля:", loaded_prof["prof_lvl"])
print("вторая игра из списка:", loaded_prof["games"][1])