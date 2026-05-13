# annex-credit-risk-pipeline
## Project Overview

This project is an end-to-end ETL and analytics pipeline built using Apache Airflow, Docker, and Python.

The pipeline processes:
- Credit data
- Sales data
- NPS survey data

It performs:
- Data ingestion
- Data cleaning
- Feature engineering
- Data quality validation
- Business analysis

The final output is a consolidated analytical dataset for credit risk monitoring and customer insights.

---

# Technologies Used

- Python
- Apache Airflow
- Docker
- Pandas
- PostgreSQL
- VS Code

---

# Project Structure

```text
airflow/
│
├── dags/
│   └── annexTE_Peter.py
│
├── scripts/
│   ├── ingest.py
│   ├── clean.py
│   ├── features.py
│   ├── quality.py
│   └── analysis.py
│
├── data/
│   ├── raw/
│   │   ├── Credit Data/
│   │   ├── Sales and Customer Data/
│   │   └── NPS DATA/
│   │
│   ├── processed/
│   ├── final/
│   ├── quality/
│   └── analysis/
│
├── logs/
├── plugins/
├── docker-compose.yaml
└── README.md
