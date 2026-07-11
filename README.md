# 🧹 Data Normalizer API

A high-performance, asynchronous REST API built with **FastAPI** that ingests messy CSV, Excel, and JSON files, automatically cleans and standardizes the data, detects schemas, and returns normalized datasets with detailed validation reports.

The project is designed with scalability, asynchronous processing, clean architecture, and production-ready practices in mind.

---

## 🚀 Features

- Upload CSV, Excel, and JSON files
- Automatic column name standardization
- Data type detection and schema inference
- Date format normalization
- Missing value handling
- Data validation reports
- Async FastAPI architecture
- PostgreSQL database integration
- SQLAlchemy 2.0 Async ORM
- Pydantic v2 validation
- Comprehensive Pytest test suite
- Interactive Swagger Documentation

---

# 📸 Screenshots

## Swagger API Documentation

Interactive API documentation generated automatically by FastAPI.

> Replace this section with your Swagger screenshot.

![Swagger UI](https://github.com/user-attachments/assets/f8b0f45a-befe-4770-8686-c4aebc7dfe0d)

---

## Upload API Response

Uploading a dataset successfully returns job information and processing status.

> Replace this section with your API response screenshot.

![Upload Response](<img width="999" height="597" alt="s1" src="https://github.com/user-attachments/assets/c7ed53d5-6d80-4b39-9403-b65d30acebcc" />
)

---

## Test Suite

All unit and integration tests passing successfully.

> Replace this section with your Pytest screenshot.

![Tests](<img width="621" height="285" alt="test" src="https://github.com/user-attachments/assets/019b0f88-9003-4b9d-a361-bf4d1bbfe1d1" />
)

---

# 🏗 Project Structure

```text
data-normalizer-api
│
├── app
│   ├── config
│   ├── core
│   │   ├── data_cleaner.py
│   │   ├── date_unifier.py
│   │   ├── name_standardizer.py
│   │   ├── reporter.py
│   │   └── schema_detector.py
│   │
│   ├── db
│   │   ├── models
│   │   ├── base.py
│   │   └── session.py
│   │
│   ├── routers
│   │   ├── upload.py
│   │   ├── status.py
│   │   └── result.py
│   │
│   ├── services
│   │   └── processing.py
│   │
│   ├── utils
│   └── main.py
│
├── tests
│   ├── integration
│   └── unit
│
├── data
├── .env.example
├── requirements.txt
├── README.md
└── alembic.ini
```

---

# ⚙️ Technology Stack

| Category | Technology |
|------------|------------|
| Language | Python 3.12 |
| Framework | FastAPI |
| Server | Uvicorn |
| Database | PostgreSQL |
| ORM | SQLAlchemy 2.0 Async |
| Migrations | Alembic |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Validation | Pydantic v2 |
| Testing | Pytest + HTTPX |
| Deployment | Render |

---

# 🧠 Data Processing Pipeline

The API follows a modular pipeline for cleaning and normalizing datasets.

## 1. Name Standardizer

Converts inconsistent column names into clean snake_case.

Example:

```
 First Name
USER-ID
Employee ID
```

becomes

```
first_name
user_id
employee_id
```

---

## 2. Schema Detector

Automatically detects:

- Integer
- Float
- Boolean
- Datetime
- String

using Pandas intelligent type inference.

---

## 3. Date Unifier

Supports multiple date formats including:

```
2024-01-20
20/01/2024
Jan 20 2024
2024.01.20
```

and converts them into

```
YYYY-MM-DD HH:MM:SS
```

---

## 4. Data Cleaner

Responsible for

- Removing unnecessary whitespace
- Handling null values
- Converting data types
- Cleaning inconsistent values

---

## 5. Reporter

Generates processing reports including

- Schema summary
- Validation logs
- Missing values
- Processing statistics

---

# 📂 Supported File Formats

| Format | Supported |
|----------|-----------|
| CSV | ✅ |
| Excel (.xlsx) | ✅ |
| JSON | ✅ |

---

# 📡 API Endpoints

## Upload Dataset

```
POST /upload
```

Uploads a CSV, Excel or JSON dataset.

---

## Check Job Status

```
GET /status/{job_id}
```

Returns

- Pending
- Processing
- Completed
- Failed

---

## Fetch Processing Result

```
GET /result/{job_id}
```

Returns

- Schema report
- Validation logs
- Cleaning summary

---

# 🧪 Running Tests

Execute all tests

```bash
pytest
```

Expected output

```
========================

9 passed

========================
```

---

# 🚀 Local Installation

## Clone Repository

```bash
git clone https://github.com/abdullah-forge/data-normalizer-api.git
```

```
cd data-normalizer-api
```

---

## Create Virtual Environment

Windows

```bash
py -3.12 -m venv venv
```

Activate

```bash
.\venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Copy

```
.env.example
```

to

```
.env
```

Update PostgreSQL credentials.

---

## Apply Migrations

```bash
alembic upgrade head
```

---

## Run Server

```bash
uvicorn app.main:app --reload
```

Server

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

Redoc

```
http://localhost:8000/redoc
```

---

# 🌐 Deployment

This project is deployed using **Render**.

Production URL


```
(https://data-normalizer-api-1ery.onrender.com/docs#/Result/get_result_result__job_id__get)
```


# 🔒 Security

- Environment variables stored in `.env`
- `.env` excluded using `.gitignore`
- Safe configuration masking using Pydantic Settings
- SQL Injection protection through SQLAlchemy ORM
- Strong validation using Pydantic v2
- Asynchronous database sessions

---

# 📁 Sample Dataset

A sample dataset used during testing is included inside the project.

It contains intentionally messy data including

- Mixed date formats
- Missing values
- Inconsistent column names
- Invalid numeric values
- Extra whitespace

Use this dataset to test the API quickly.
I have uploaded in main folder

---

# 🛣 Roadmap

- Docker support
- Background task queue
- Download cleaned dataset
- Authentication
- File history
- Dashboard
- Data quality scoring
- AI-powered schema suggestions
- Cloud storage integration

---

# 👨‍💻 Author

**Abdullah**

Computer Engineering Undergraduate

GitHub

https://github.com/abdullah-forge

---

## ⭐ Support

If you found this project useful, consider giving it a **Star** on GitHub.

It helps others discover the project and motivates future improvements.
