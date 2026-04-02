from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.sale import SaleCreate, SaleUpdate, SaleResponse
from app.services import sale_service
from typing import List, Optional
from datetime import datetime

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/", response_model=SaleResponse)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    return sale_service.create_sale(db, sale)

@router.get("/", response_model=List[SaleResponse])
def list_sales(
    customer_name: Optional[str] = None,
    status: Optional[str] = None,
    category: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    return sale_service.get_sales(db, customer_name, status, category, start_date, end_date)

@router.get("/{sale_id}", response_model=SaleResponse)
def get_sale(sale_id: int, db: Session = Depends(get_db)):
    sale = sale_service.get_sale_by_id(db, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

@router.put("/{sale_id}", response_model=SaleResponse)
def update_sale(sale_id: int, sale: SaleUpdate, db: Session = Depends(get_db)):
    updated = sale_service.update_sale(db, sale_id, sale)
    if not updated:
        raise HTTPException(status_code=404, detail="Sale not found")
    return updated

@router.delete("/{sale_id}", response_model=SaleResponse)
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    deleted = sale_service.delete_sale(db, sale_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Sale not found")
    return deleted