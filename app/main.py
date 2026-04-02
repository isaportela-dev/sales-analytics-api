from fastapi import FastAPI
from app.routers import sales, analytics

app = FastAPI(
    title="Sales Analytics API",
    description="API for managing and analyzing sales data",
    version="1.0.0"
)

app.include_router(sales.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"message": "Sales Analytics API is running"}