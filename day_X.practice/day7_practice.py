import json

def update_user_level(filename, added_levels):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    data["prof_lvl"] += added_levels
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    return data["prof_lvl"]
    
def add_user_game(filename, new_game):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    data["games"].append(new_game)
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    return data["games"]

with open("profile.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Список игр пользователя:", data["games"])

import json
def get_user_by_id(filename, user_id):
    with open(filename, "r", encoding = "utf-8") as f:
        users = json.load(f)
    for user in users:
        if user["id"] == user_id:
                return user
    return None
def get_user_by_name(filename, user_name):
    with open(filename, "r", encoding = "utf-8") as f:
        names = json.load(f)
    for nick in names:
        if nick["name"] == user_name:
            return nick
    return None
print(get_user_by_name("users.json", 2))