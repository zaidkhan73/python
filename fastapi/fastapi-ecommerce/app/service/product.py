import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path(__file__).parent.parent / "data" / "products.json"

def load_products() -> List[Dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE,"r",encoding="utf-8") as file:
        return json.load(file)

def get_all_products() -> List[Dict]:
    return load_products()

def save_products(products: List[Dict]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=2,ensure_ascii=False)


def add_product(product: Dict) -> Dict:
    products = load_products()
    if any(p["sku"] == product["sku"] for p in products):
        raise ValueError(f"Product with SKU '{product['sku']}' already exists.")
    products.append(product)
    save_products(products)
    return product

def delete_product(product_id: str) -> None:
    products = load_products()
    products = [p for p in products if p["id"] != product_id]
    deleted = property.pop("id", None) in [p["id"] for p in products]
    if not deleted:
        raise ValueError(f"Product with ID '{product_id}' not found.")
    save_products(products)
