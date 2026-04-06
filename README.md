# Sales Analytics API

A backend application for managing and analyzing sales data, simulating a real-world business environment.

Built with Python, FastAPI, PostgreSQL, and Pandas — featuring a live dashboard frontend that consumes the API in real time.

🔗 **Live Demo:** _coming soon_  
📊 **Dashboard:** _coming soon_

---

## About the Project

This project simulates a mini CRM + analytics system, designed to reflect real sales operations workflows.

The system tracks opportunities across the entire sales funnel — from prospecting to closed deals — and generates KPIs that sales teams use to make decisions: total revenue, conversion rate, average ticket, and top customers.

The data model and business logic were designed based on how real CRM systems (like SAP Sales Cloud) structure sales pipelines.

---

## Features

**Sales Management**
- Create, list, update and delete sales records
- Filter by customer, status, category, and date range
- Track sales stage: `prospecting → negotiation → closed_won / closed_lost`

**Analytics & KPIs**
- Total revenue from won deals
- Conversion rate across all opportunities
- Revenue breakdown by product category
- Top customers by revenue
- Analytical insights powered by Pandas: average ticket, top product, top category

**Infrastructure**
- Dockerized environment — API and database start with a single command
- Database migrations managed with Alembic
- Auto-generated API documentation via Swagger UI

**Frontend Dashboard**
- HTML/CSS/JS dashboard consuming the API in real time
- KPI cards, top customers table, and recent sales with status badges

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Data Analysis | Pandas |
| Containerization | Docker + Docker Compose |
| Frontend | HTML, CSS, JavaScript |

---

## Project Structure

```
sales-analytics-api/
├── app/
│   ├── main.py         # App entrypoint and middleware
│   ├── database.py     # Database connection and session
│   ├── models/         # SQLAlchemy table definitions
│   ├── schemas/        # Pydantic validation schemas
│   ├── routers/        # API route definitions
│   └── services/       # Business logic and analytics
├── alembic/            # Database migration files
├── frontend/           # Dashboard (HTML/CSS/JS)
├── seed.py             # Sample data for demonstration
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

---

## API Endpoints

### Sales
| Method | Endpoint | Description |
|---|---|---|
| POST | `/sales/` | Create a new sale |
| GET | `/sales/` | List sales with optional filters |
| GET | `/sales/{id}` | Get sale by ID |
| PUT | `/sales/{id}` | Update a sale |
| DELETE | `/sales/{id}` | Delete a sale |

### Analytics
| Method | Endpoint | Description |
|---|---|---|
| GET | `/analytics/total-revenue` | Total revenue from won deals |
| GET | `/analytics/conversion-rate` | Win rate across all opportunities |
| GET | `/analytics/revenue-by-category` | Revenue grouped by product category |
| GET | `/analytics/top-customers` | Top customers by revenue |
| GET | `/analytics/insights` | Pandas-powered analytical insights |

---

## Running Locally

**Prerequisites:** Docker and Docker Compose installed.
```bash
# Clone the repository
git clone https://github.com/isaportela-dev/sales-analytics-api.git
cd sales-analytics-api

# Start the API and database
docker-compose up --build

# Apply database migrations
alembic upgrade head

# (Optional) Load sample data
python seed.py
```

API will be available at `http://localhost:8000`  
Swagger docs at `http://localhost:8000/docs`

---

## Dashboard

Open `frontend/index.html` in your browser with the API running locally, or access the live version at the link above.

---

## Author

**Isabella Portela**  
Backend Developer | Python · FastAPI · Java · Spring Boot  
[GitHub](https://github.com/isaportela-dev) · [LinkedIn](https://www.linkedin.com/in/isabellarportela)