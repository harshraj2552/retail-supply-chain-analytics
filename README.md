# Retail Supply Chain Analytics

## Project Overview

Retail Supply Chain Analytics is an end-to-end data analytics project developed using Python, SQL, and Power BI. The project simulates a retail supply chain environment by generating transactional data, performing business analysis, and visualizing insights through an interactive dashboard.

The objective is to analyze sales performance, product trends, category performance, and overall business metrics to support data-driven decision-making.

---

## Tech Stack

- Python (Pandas, NumPy, Faker, Matplotlib)
- MySQL
- Power BI
- Git & GitHub

---

## Project Architecture

```text
Python
   ↓
CSV Dataset Generation
   ↓
MySQL Database
   ↓
SQL Analysis
   ↓
Power BI Dashboard
```

---

## Dataset Information

The project consists of multiple datasets representing a retail supply chain ecosystem:

- Orders Dataset
- Products Dataset
- Suppliers Dataset
- Warehouses Dataset
- Inventory Dataset

### Dataset Size

| Dataset | Records |
|----------|----------|
| Orders | 50,000 |
| Products | 500 |
| Suppliers | 20 |
| Warehouses | 5 |
| Inventory | 1,000+ |

---

## Key Performance Indicators (KPIs)

| KPI | Value |
|------|--------|
| Total Revenue | ₹256.08M |
| Units Sold | 71K |
| Total Orders | 12.85K |
| Average Order Value | ₹19.92K |

---

## Business Insights

- Home Appliances emerged as the highest revenue-generating category.
- Electronics was the second-best performing category with strong sales contribution.
- Picture Folder generated the highest revenue among all products.
- Other top-performing products included Size Monitor, Spend Toaster, Water Iron, and Either Laptop.
- Monthly revenue remained relatively stable throughout the analysis period.
- Revenue ranged between approximately ₹9M and ₹12M for most months.
- The decline in the final month is due to incomplete monthly transactional data.
- The average order value of ₹19.92K indicates strong revenue generation per order.

---

## SQL Analysis

Business analysis was performed using SQL queries including:

- Total Revenue Analysis
- Sales Performance Analysis
- Product Performance Analysis
- Supplier Analysis
- Inventory Monitoring
- Category-wise Revenue Analysis
- Monthly Revenue Trend Analysis

Files:

```text
sql/schema.sql
sql/analysis_queries.sql
```

---

## Python Analysis

Exploratory Data Analysis (EDA) was performed using Python.

### Analysis Performed

- Data Validation
- Missing Value Analysis
- Statistical Summary
- Revenue Distribution Analysis
- Monthly Revenue Trend Analysis
- Category-wise Revenue Analysis

Libraries Used:

```python
pandas
numpy
matplotlib
faker
```

Files:

```text
python/generate_dataset.py
python/exploratory_analysis.py
```

---

## Power BI Dashboard

### Dashboard Features

- Total Revenue KPI
- Units Sold KPI
- Total Orders KPI
- Average Order Value KPI
- Monthly Revenue Trend
- Revenue by Category
- Top Products by Revenue

### Dashboard Preview

![Retail Supply Chain Dashboard](images/dashboard.png)

---

## Dashboard Insights

### Revenue by Category

- Home Appliances generated the highest revenue.
- Electronics followed closely behind.
- Office Supplies and Furniture also contributed significantly to total sales.

### Top Products by Revenue

Top-performing products include:

1. Picture Folder
2. Size Monitor
3. Spend Toaster
4. Water Iron
5. Either Laptop

### Monthly Revenue Trend

- Revenue remained consistent across most months.
- Monthly revenue generally ranged between ₹9M–₹12M.
- The final month's lower revenue is due to incomplete transactional records.

---

## Project Structure

```text
retail-supply-chain-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── python/
│   ├── generate_dataset.py
│   └── exploratory_analysis.py
│
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
│
├── powerbi/
│   └── Retail_Supply_Chain_Analytics.pbix
│
├── images/
│   └── dashboard.png
│
├── README.md
│
└── .gitignore
```

---

## Future Enhancements

- Real-Time Data Integration
- Automated ETL Pipeline
- Inventory Optimization
- Demand Forecasting
- Supplier Performance Scoring
- Advanced Power BI Reporting

---

## Author

**Harsh Raj**

Aspiring Data Analyst

Skills:
- SQL
- Python
- Power BI
- Data Analysis
- Data Visualization
- Business Intelligence

---