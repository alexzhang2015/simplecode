from fastapi import FastAPI, APIRouter

app = FastAPI()

# products服务
products_router = APIRouter()


@products_router.get("/products/{product_id}")
async def get_product(product_id):
    return {"id": product_id, "name": f"Product {product_id}"}

app.include_router(products_router)

# reviews服务
reviews_router = APIRouter()


@reviews_router.get("/reviews")
async def get_reviews(product_id):
    return [{"product_id": product_id, "rating": 5, "comment": "Amazing!"}]

app.include_router(reviews_router)

# orders服务
orders_router = APIRouter()


@orders_router.get("/orders")
async def get_orders():
    return [{"id": 1, "product_id": 123, "amount": 2}]

app.include_router(orders_router)

# users服务
users_router = APIRouter()


@users_router.get("/users")
async def get_users():
    return [{"id": 1, "name": "John Doe"}]

app.include_router(users_router)

# 在主应用中运行整个服务
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8001)
