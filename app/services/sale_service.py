from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.sale import Sale
from app.schemas.sale import SaleCreate, SaleUpdate
from datetime import datetime
from typing import Optional

def create_sale(db: Session, sale: SaleCreate):
    db_sale = Sale(**sale.model_dump())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def get_sales(
    db: Session,
    customer_name: Optional[str] = None,
    status: Optional[str] = None,
    category: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
):
    query = db.query(Sale)

    if customer_name:
        query = query.filter(Sale.customer_name.ilike(f"%{customer_name}%"))
    if status:
        query = query.filter(Sale.status == status)
    if category:
        query = query.filter(Sale.category == category)
    if start_date:
        query = query.filter(Sale.date >= start_date)
    if end_date:
        query = query.filter(Sale.date <= end_date)

    return query.all()

def get_sale_by_id(db: Session, sale_id: int):
    return db.query(Sale).filter(Sale.id == sale_id).first()

def update_sale(db: Session, sale_id: int, sale: SaleUpdate):
    db_sale = get_sale_by_id(db, sale_id)
    if not db_sale:
        return None
    for key, value in sale.model_dump(exclude_unset=True).items():
        setattr(db_sale, key, value)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def delete_sale(db: Session, sale_id: int):
    db_sale = get_sale_by_id(db, sale_id)
    if not db_sale:
        return None
    db.delete(db_sale)
    db.commit()
    return db_sale