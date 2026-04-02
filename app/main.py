from fastapi import FastAPI
from app.routers import sales

app = FastAPI(
    title="Sales Analytics API",
    description="API for managing and analyzing sales data",
    version="1.0.0"
)

app.include_router(sales.router)

@app.get("/")
def root():
    return {"message": "Sales Analytics API is running"}