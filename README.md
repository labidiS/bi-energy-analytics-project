# BI Energy Analytics Project

## Overview

This project demonstrates an **end-to-end data analytics pipeline**, from raw data ingestion to analytics-ready modeling and business visualization.

The goal is to show how operational data can be transformed into reliable metrics and exposed to stakeholders through a BI layer.

---

## Tech Stack

* **Python** (pandas, SQLAlchemy) – data ingestion
* **PostgreSQL** – data warehouse
* **SQL** – data transformations and modeling
* **Looker Studio** – dashboard visualization
* **Git / GitHub** – version control

---

## Data Source

The project uses the **Olist e-commerce dataset**, representing a Brazilian online marketplace:

* Customers place orders on the platform
* Each order can contain multiple products
* Data includes orders, customers, and order items

---

## Project Architecture

```
CSV files
  ↓
Python ingestion
  ↓
PostgreSQL RAW tables
  ↓
SQL STAGING tables
  ↓
Analytics MART (fact_orders)
  ↓
BI visualization (Looker Studio)
```

---

## Data Layers

### RAW

Raw tables are direct copies of the source CSV files.

* Purpose: preserve original data without modification

### STAGING

Staging tables clean and prepare the data:

* type casting (dates, timestamps)
* schema normalization
* basic validations

### MART

The analytics layer contains a fact table:

* **fact_orders**
* One row per order
* Used as the single source of truth for analytics

---

## Key Metrics

* **Orders**
  Number of customer orders (one order = one checkout)

* **Revenue (conceptual)**
  Monetary value of orders (requires aggregation at order level to avoid duplication from order items)

---

## Dashboard
<img width="1173" height="805" alt="Screenshot 2026-01-12 at 04 30 04" src="https://github.com/user-attachments/assets/e3f22f7c-dfa3-4794-8a4b-a38cbdd1d159" />


A dashboard was built in **Looker Studio** to visualize business KPIs.

### Shown insights:

* Orders over time
* Trend and seasonality (e.g. Black Friday peak)

The dashboard is based on pre-aggregated SQL results to ensure consistent business logic.

---

## What This Project Demonstrates

* Building an end-to-end analytics pipeline
* Working with SQL-based data modeling
* Understanding data grain and aggregation issues
* Separating data engineering, analytics, and BI layers
* Communicating insights clearly through dashboards


---

## Author

Samar Labidi


