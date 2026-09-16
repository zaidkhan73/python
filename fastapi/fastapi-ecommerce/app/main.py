from fastapi import FastAPI, HTTPException, Query
from service.product import add_product, get_all_products
from schema.product import Product
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI E-commerce application!"}


# @app.get("/products")
# def get_products():
#     return get_all_products()


@app.get("/products")
def list_products(
    name: str = Query(
        default=None,
        min_length=1,
        max_length=50,
        description="Search by product name (case-insensitive)",
    ),
    sort_by_price: bool = Query(default=False, description="Sort products by price "),
    order: str = Query(
        default="asc",
        description="Order of sorting: 'asc' for ascending, 'desc' for descending",
    ),
    limit: int = Query(
        default=5,
        ge=1,
        le=100,
        description="Limit the number of products returned (default: 5)",
    ),
):
    products = get_all_products()
    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

    if not products:
        raise HTTPException(
            status_code=404, detail="No products found matching the search criteria"
        )

    if sort_by_price:
        reverse = order.lower() == "desc"
        products = sorted(products, key=lambda p: p.get("price", 0), reverse=reverse)

    products = products[:limit]
    total = len(products)

    return {"total": total, "products": products}


@app.get("/products/{product_id}")
def get_product_by_id(product_id: str):
    products = get_all_products()
    product = [p for p in products if p.get("id") == product_id]
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product[0]


@app.post("/products", status_code=201)
def create_product(product: Product):
    product_dict = product.model_dump(mode="json")
    product_dict["id"] = str(uuid4())
    product_dict["created_at"] = datetime.utcnow().isoformat() + "Z"
    try:
        add_product(product_dict)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return product.model_dump(product_dict, mode="json")

@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: UUID):
    try:
        delete_product(product_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": "Product deleted successfully"}


@app.get("/items/{id}")
def get_item(id: int):
    products = ["Laptop", "Smartphone", "Tablet", "Headphones"]
    if id < 0 or id >= len(products):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": id, "item_name": products[id]}
