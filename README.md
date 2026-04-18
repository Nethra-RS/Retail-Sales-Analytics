# 📊 Retail Sales Analytics & Forecasting Project

## 🚀 Overview
This project analyzes a global retail dataset to uncover key business insights and forecast future sales. It demonstrates a complete data pipeline from raw data ingestion to business intelligence visualization.

The goal is to answer critical business questions such as:
- Who are the top revenue-generating customers?
- Which regions and categories perform best?
- What trends exist in sales over time?
- What can we expect in the near future?

---

## 🧱 Data Pipeline

Raw CSV → SQL Database → Data Transformation → Python Analysis → Tableau Dashboard

### 🔹 Steps:
1. **Data Ingestion**
   - Loaded raw CSV data into SQLite database

2. **Data Cleaning & Transformation**
   - Converted date fields into proper format
   - Removed inconsistencies and ensured data quality
   - Created a cleaned table (`orders_clean`)

3. **SQL Analysis**
   - Aggregated sales by customer, region, segment, and category
   - Built queries for business insights

4. **Python Analysis**
   - Performed exploratory data analysis (EDA)
   - Generated trends and distributions
   - Built a simple forecasting model (7-day moving average)

5. **Dashboard (Tableau)**
   - Designed interactive dashboards for business users
   - Added KPIs, filters, and insights

---

## 📊 Key Metrics

- **Total Sales:** ~$2.24M  
- **Total Orders:** 4,859  
- **Average Order Value:** ~$461  
- **Forecast (Next Period):** ~$2.17K  

---

## 🔍 Key Insights

### 📌 Business Performance
- Revenue is highly concentrated among top customers, with the highest contributor generating over $25K  
- The Consumer segment leads with ~$1.14M, contributing more than 50% of total revenue  
- The West region is the top performer (~$710K), while the South underperforms (~$389K)  
- Technology is the leading category (~$827K), contributing ~36.6% of total sales  

### 📌 Trends & Patterns
- Sales are highly skewed, with most transactions under $500 and a few high-value orders driving revenue  
- Strong seasonality observed, with peaks in November (~$117K) and December (~$83K)  
- Significant gap between top products (~$61K) and low-performing products (<$10)  

---

## 📈 Forecasting

A simple **7-day moving average model** was used to estimate short-term sales:

- Forecasted daily sales: ~$2.17K  
- Indicates stable short-term performance based on recent trends  

> Note: This is a baseline model and can be extended using advanced time series techniques.

---

## 🛠️ Tech Stack

- **SQL (SQLite)** – Data storage & transformation  
- **Python (Pandas)** – Data analysis  
- **Tableau** – Data visualization & dashboarding  

---

## 📊 Dashboard Features

- Interactive filters (Date, Region)  
- KPI cards (Sales, Orders, AOV, Forecast)  
- Sales trend with forecast  
- Segment, category, and region performance  
- Customer and product insights  
- Sales distribution analysis  

---

## 📂 Project Structure

data_analyst_project/
│
├── data/
│ └── train.csv
│
├── sql/
│ ├── database_setup.py
│ └── transformation.sql
│
├── notebooks/
│ └── analysis.py
│
├── app/
│ └── (optional dashboard or app files)
│
├── forecast.csv
└── README.md


---

## 💡 Business Recommendations

- Focus on retaining high-value customers driving revenue  
- Invest in high-performing regions like the West  
- Improve performance in underperforming regions (South)  
- Optimize product portfolio by addressing low-performing items  
- Leverage seasonal trends for inventory and marketing strategies  

---

## 🎥 Project Walkthrough

(👉 Add your video link here)

---

## 📌 Conclusion

This project demonstrates end-to-end data analysis capabilities, combining SQL, Python, and Tableau to deliver actionable business insights and forecasting.

