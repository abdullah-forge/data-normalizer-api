Data Normalizer API
A high-performance, asynchronous REST API built to ingest messy CSV, Excel, and JSON files, clean them, standardize schemas, and output normalized data.

Current Status: 🏗️ Phase 1 Complete (Foundation & Database Layer)

🛠️ Tech Stack (Implemented So Far)
Language: Python 3.12
Framework: FastAPI
Database: PostgreSQL
ORM: SQLAlchemy 2.0 (Async)
Migrations: Alembic (Async configured)
Data Processing: Pandas, NumPy (To be implemented in next phase)
Validation: Pydantic v2
📁 Project Structure (Phase 1)
data-normalizer/├── alembic/                  # DB Migrations (Async ready)├── app/│   ├── config/│   │   └── settings.py       # Secure Pydantic settings (auto-masks DB URLs)│   ├── db/│   │   ├── base.py           # SQLAlchemy DeclarativeBase│   │   ├── session.py        # Async Engine & Session Factory│   │   └── models/│   │       └── job.py        # Job ORM Model (SQLAlchemy 2.0 syntax)│   └── main.py               # (Pending)├── .env.example              # Safe template for environment variables├── .gitignore                ├── alembic.ini               ├── pytest.ini                # Pytest configuration├── requirements.txt          └── README.md
🚀 Setup & Installation
Prerequisites
Python 3.12 installed on your system.
PostgreSQL running locally (or a remote DB URL).
Steps

Clone the repository:
git clone https://github.com/abdullah-forge/data-normalizer-api.git
cd data-normalizer-api

Create and Activate Virtual Environment:
# Windows (Using py launcher for specific version)
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1

Configure Environment Variables:
# Copy the example file
cp .env.example .env

# Copy the example file
cp .env.example .env
pip install -r requirements.txt

Run Database Migrations:
# Generate migration script for the 'jobs' table
alembic revision --autogenerate -m "create jobs table"

# Apply migrations to the database
alembic upgrade head

Security Implementation
This project takes security seriously even at the foundation level:

Pydantic Settings Masking: Directly printing the settings object or using settings.get_safe_dict() automatically masks sensitive data (like database passwords) into ****.
Safe Defaults: .env.example contains dummy values. The real secrets are strictly ignored by Git.

 What's Next? (Phase 2)
 Implement app/core/name_standardizer.py (Regex & String ops)
 Implement app/core/schema_detector.py (Pandas type inference)
 Implement app/core/data_cleaner.py (Null handling)
 Create FastAPI endpoints (/upload, /status, /result)
 Write Pytest integration tests
