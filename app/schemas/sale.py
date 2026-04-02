from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SaleBase(BaseModel):
    customer_name: str
    product: str
    category: str
    amount: float
    quantity: int
    date: datetime
    status: str  # won / lost / pending
    sales_stage: str  # prospecting / negotiation / closed_won / closed_lost

class SaleCreate(SaleBase):
    pass

class SaleUpdate(BaseModel):
    customer_name: Optional[str] = None
    product: Optional[str] = None
    category: Optional[str] = None
    amount: Optional[float] = None
    quantity: Optional[int] = None
    date: Optional[datetime] = None
    status: Optional[str] = None
    sales_stage: Optional[str] = None

class SaleResponse(SaleBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True