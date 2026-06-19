import json
import os

FILE_PATH = "data/products.json"

def load_products():
    if not os.path.isfile(FILE_PATH):
        return {"disposables": {}, "liquids": {}, "cartridges": {}, "snus": {}, "pods": {}}

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_products(data):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_category(category: str):
    data = load_products()
    return data.get(category, {})

def add_product(category: str, product_name: str, product_data: dict):
    data = load_products()

    if category not in data:
        data[category] = {}

    data[category][product_name] = product_data

    save_products(data)