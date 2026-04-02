from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.sale import Sale
from datetime import datetime
from typing import Optional
import pandas as pd

def get_total_revenue(db: Session):
    result = db.query(func.sum(Sale.amount)).filter(Sale.status == "won").scalar()
    return {"total_revenue": result or 0}

def get_revenue_by_category(db: Session):
    result = db.query(Sale.category, func.sum(Sale.amount))\
        .filter(Sale.status == "won")\
        .group_by(Sale.category)\
        .all()
    return [{"category": r[0], "revenue": r[1]} for r in result]

def get_top_customers(db: Session, limit: int = 5):
    result = db.query(Sale.customer_name, func.sum(Sale.amount))\
        .filter(Sale.status == "won")\
        .group_by(Sale.customer_name)\
        .order_by(func.sum(Sale.amount).desc())\
        .limit(limit)\
        .all()
    return [{"customer": r[0], "total": r[1]} for r in result]

def get_conversion_rate(db: Session):
    total = db.query(func.count(Sale.id)).scalar()
    won = db.query(func.count(Sale.id)).filter(Sale.status == "won").scalar()
    rate = (won / total * 100) if total > 0 else 0
    return {"total_sales": total, "won": won, "conversion_rate": round(rate, 2)}

def get_insights(db: Session):
    sales = db.query(Sale).all()
    if not sales:
        return {"message": "No data available"}

    df = pd.DataFrame([{
        "amount": s.amount,
        "quantity": s.quantity,
        "product": s.product,
        "category": s.category,
        "status": s.status
    } for s in sales])

    won_df = df[df["status"] == "won"]

    return {
        "average_ticket": round(won_df["amount"].mean(), 2) if not won_df.empty else 0,
        "total_quantity_sold": int(df["quantity"].sum()),
        "top_product": df.groupby("product")["amount"].sum().idxmax() if not df.empty else None,
        "top_category": df.groupby("category")["amount"].sum().idxmax() if not df.empty else None,
    }