from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import get_db
from models import Product

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
def get_products():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    db.close()
    return products



@app.post("/products")
def add_product(product: Product):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO products (name, price, image, review_image) VALUES (%s, %s, %s, %s)",
        (product.name, product.price, product.image, product.review_image)
    )
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Product created"}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    db.close()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
