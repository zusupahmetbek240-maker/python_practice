import json
wallets = [
    {"address": 1, "currency": "BTC", "balance_usd": 943},
    {"address": 2, "currency": "ETH", "balance_usd": 4291},
    {"address": 3, "currency": "LTC", "balance_usd": 1985},
    {"address": 4, "currency": "ETH", "balance_usd": 376 }
]

file_path = "wallets.json"

with open(file_path, "w", encoding = "utf-8") as f:
    json.dump(wallets, f, ensure_ascii = False, indent = 4)

def load_wallets(filename, min_balance=None):
    with open(filename, "r", encoding = "utf-8") as f:
         data = json.load(f)
    if min_balance is not None:
        return [w for w in data if w["balance_usd"] > min_balance]
    return data
all_data = load_wallets(file_path)
rich_wallets = load_wallets(file_path, min_balance=1000) 
print("wallets that > 1000$:", rich_wallets)
