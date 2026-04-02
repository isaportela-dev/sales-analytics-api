from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    product = Column(String, nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)  # won / lost / pending
    sales_stage = Column(String, nullable=False)  # prospecting / negotiation / closed_won / closed_lost
    created_at = Column(DateTime, server_default=func.now())