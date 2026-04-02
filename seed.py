from app.database import SessionLocal
from app.models.sale import Sale
from datetime import datetime

db = SessionLocal()

sales = [
    Sale(customer_name="Empresa ABC", product="SAP S/4HANA", category="ERP", amount=50000, quantity=1, date=datetime(2026, 1, 10), status="won", sales_stage="closed_won"),
    Sale(customer_name="Tech Solutions", product="SAP Analytics Cloud", category="Analytics", amount=32000, quantity=2, date=datetime(2026, 1, 15), status="won", sales_stage="closed_won"),
    Sale(customer_name="Global Logistics", product="SAP IBP", category="Supply Chain", amount=75000, quantity=1, date=datetime(2026, 1, 20), status="won", sales_stage="closed_won"),
    Sale(customer_name="Retail Pro", product="SAP Commerce", category="Retail", amount=28000, quantity=3, date=datetime(2026, 1, 25), status="lost", sales_stage="closed_lost"),
    Sale(customer_name="FinanceCorp", product="SAP S/4HANA", category="ERP", amount=90000, quantity=1, date=datetime(2026, 2, 3), status="won", sales_stage="closed_won"),
    Sale(customer_name="MedTech Inc", product="SAP Analytics Cloud", category="Analytics", amount=41000, quantity=2, date=datetime(2026, 2, 8), status="pending", sales_stage="negotiation"),
    Sale(customer_name="AgriGroup", product="SAP IBP", category="Supply Chain", amount=63000, quantity=1, date=datetime(2026, 2, 14), status="won", sales_stage="closed_won"),
    Sale(customer_name="Empresa ABC", product="SAP Commerce", category="Retail", amount=19000, quantity=4, date=datetime(2026, 2, 18), status="lost", sales_stage="closed_lost"),
    Sale(customer_name="BuildCo", product="SAP S/4HANA", category="ERP", amount=55000, quantity=1, date=datetime(2026, 2, 22), status="pending", sales_stage="prospecting"),
    Sale(customer_name="Tech Solutions", product="SAP IBP", category="Supply Chain", amount=48000, quantity=2, date=datetime(2026, 3, 1), status="won", sales_stage="closed_won"),
    Sale(customer_name="Global Logistics", product="SAP Analytics Cloud", category="Analytics", amount=37000, quantity=1, date=datetime(2026, 3, 5), status="won", sales_stage="closed_won"),
    Sale(customer_name="FinanceCorp", product="SAP Commerce", category="Retail", amount=22000, quantity=2, date=datetime(2026, 3, 10), status="pending", sales_stage="negotiation"),
    Sale(customer_name="RetailPro", product="SAP S/4HANA", category="ERP", amount=81000, quantity=1, date=datetime(2026, 3, 15), status="won", sales_stage="closed_won"),
    Sale(customer_name="MedTech Inc", product="SAP IBP", category="Supply Chain", amount=69000, quantity=1, date=datetime(2026, 3, 20), status="lost", sales_stage="closed_lost"),
    Sale(customer_name="AgriGroup", product="SAP Analytics Cloud", category="Analytics", amount=44000, quantity=2, date=datetime(2026, 3, 25), status="won", sales_stage="closed_won"),
]

db.add_all(sales)
db.commit()
db.close()

print("Seed data inserted successfully!")
