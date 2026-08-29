import requests
import json

def collect_cat_facts (count, filename):
    facts_list = []
    url = "https://catfact.ninja/fact"
    
    for _ in range(count):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            facts_list.append(data["fact"])
        else:
            print(f"ошибка сервера: {response.status_code}")
    with open (filename, "w", encoding = "utf-8") as f:
        json.dump(facts_list, f, ensure_ascii = False, indent = 4) 
    print(f"сохранено {len(facts_list)} фактов в {filename}")

collect_cat_facts(3,"cats.json")



    

