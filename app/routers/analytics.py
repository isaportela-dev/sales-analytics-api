from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import analytics_service

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/total-revenue")
def total_revenue(db: Session = Depends(get_db)):
    return analytics_service.get_total_revenue(db)

@router.get("/revenue-by-category")
def revenue_by_category(db: Session = Depends(get_db)):
    return analytics_service.get_revenue_by_category(db)

@router.get("/top-customers")
def top_customers(limit: int = 5, db: Session = Depends(get_db)):
    return analytics_service.get_top_customers(db, limit)

@router.get("/conversion-rate")
def conversion_rate(db: Session = Depends(get_db)):
    return analytics_service.get_conversion_rate(db)

@router.get("/insights")
def insights(db: Session = Depends(get_db)):
    return analytics_service.get_insights(db)