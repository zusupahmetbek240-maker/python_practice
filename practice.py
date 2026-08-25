import json
user_profile = {
    "nickname": "figeron1020qq",
    "prof_lvl": 10,
    "games": ["Resident 2 Remake", "Alan Wake"],
    "is_active": "True"
}
with open("profile.json", "w", encoding = "utf-8") as f:
    json.dump(user_profile, f, ensure_ascii = False, indent = 4)
with open("profile.json", "r", encoding = "utf-8") as f:
    loaded_prof = json.load(f)

def safe_load_profile(filename):
    try:
        with open(filename, "r", encoding = "utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
            return "Файл не найден ептыть!"
    except json.JSONDecodeError:
            return "Файл поврежден бляэ"
print(safe_load_profile("profile.json"))
print(safe_load_profile("reg_data.json"))
print("тип данных:", type(loaded_prof))
print("уровень профиля:",(loaded_prof["prof_lvl"]))
print("Вторая любимая игра:",(loaded_prof["games"][1]))

