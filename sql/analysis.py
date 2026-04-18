import sqlite3
import pandas as pd

# -------------------------------
# Connect to SQLite database
# -------------------------------
conn = sqlite3.connect('sales.db')

# -------------------------------
# 1. Check for duplicate records
# -------------------------------
duplicate_query = """
SELECT *,
       COUNT(*) as count
FROM orders
GROUP BY 
    "Order ID",
    "Order Date",
    "Ship Date",
    "Customer ID",
    "Customer Name",
    Segment,
    Country,
    City,
    State,
    Region,
    Category,
    "Sub-Category",
    "Product Name",
    Sales
HAVING count > 1;
"""

duplicates = pd.read_sql(duplicate_query, conn)
print("\nDuplicate Check:\n", duplicates)

# Insight: duplicates found but handled them in transformation step, so no duplicates in clean table


# -------------------------------
# 2. Top Customers Analysis
# -------------------------------
top_customers_query = """
SELECT customer_name, SUM(sales) as revenue
FROM orders_clean
GROUP BY customer_name
ORDER BY revenue DESC
LIMIT 10;
"""

top_customers = pd.read_sql(top_customers_query, conn)
print("\nTop Customers:\n", top_customers)

# Insight: Revenue is concentrated among a small group of top customers, with the highest contributor generating over 25K in sales, indicating strong customer concentration.


# -------------------------------
# 3. Segment Performance
# -------------------------------
segment_query = """
SELECT Segment, SUM(Sales) as revenue
FROM orders_clean
GROUP BY Segment
ORDER BY revenue DESC;
"""

segment_perf = pd.read_sql(segment_query, conn)
print("\nSegment Performance:\n", segment_perf)

#Insight: The Consumer segment is the largest contributor to revenue, followed by Corporate and Home Office, indicating that the business may want to focus marketing efforts on the Consumer segment for growth opportunities.


# -------------------------------
# 4. Region Performance
# -------------------------------
region_query = """
SELECT Region, SUM(Sales) as revenue
FROM orders_clean
GROUP BY Region
ORDER BY revenue DESC;
"""

region_perf = pd.read_sql(region_query, conn)
print("\nRegion Performance:\n", region_perf)

# Insight: The West region is the top-performing region in terms of revenue, followed by the East, South, and Central regions, suggesting that the business may want to investigate factors contributing to the West's success and consider strategies to boost performance in the other regions.


# -------------------------------
# 5. Category Performance
# -------------------------------
category_query = """
SELECT Category, SUM(Sales) as revenue
FROM orders_clean
GROUP BY Category
ORDER BY revenue DESC;
"""

category_perf = pd.read_sql(category_query, conn)
print("\nCategory Performance:\n", category_perf)

#  Insight: The Technology category is the highest revenue generator, followed by Furniture and Office Supplies, indicating that the business may want to prioritize inventory and marketing efforts around Technology products to maximize revenue growth.

# -------------------------------
# 6. Daily Sales Trend
# -------------------------------
daily_sales_query = """
SELECT order_date, SUM(Sales) as total_sales
FROM orders_clean
GROUP BY order_date
ORDER BY order_date;
"""

daily_sales = pd.read_sql(daily_sales_query, conn)
print("\nDaily Sales (Sample):\n", daily_sales.head())

# Insight: Sales show strong seasonality, with peak performance observed during end-of-year months, likely driven by holiday demand
# -------------------------------
# 7. Forecast (7-day moving average)
# -------------------------------
forecast_value = daily_sales['total_sales'].tail(7).mean()

print("\nNext 7 Days Forecast (Moving Avg):", forecast_value)

# Save forecast output
forecast_df = pd.DataFrame({
    'metric': ['Forecast'],
    'value': [forecast_value]
})

forecast_df.to_csv("forecast.csv", index=False)
#Insight: A simple 7-day moving average was used to estimate short-term sales, indicating stable near-term performance with minimal volatility.


# -------------------------------
# 8. Data Quality Check
# -------------------------------
print("\nRaw count:", pd.read_sql("SELECT COUNT(*) FROM orders", conn))
print("Clean count:", pd.read_sql("SELECT COUNT(*) FROM orders_clean", conn))

df = pd.read_sql("SELECT * FROM orders_clean", conn)
print("\nMissing Values:\n", df.isnull().sum())

# Insight: No missing values found in clean dataset, indicating good data quality after transformation steps.

# -------------------------------
# 9. Monthly Sales Trend
# -------------------------------
monthly_query = """
SELECT 
    STRFTIME('%Y-%m', order_date) as month,
    SUM(sales) as revenue
FROM orders_clean
GROUP BY month
ORDER BY month;
"""

monthly_sales = pd.read_sql(monthly_query, conn)
print("\nMonthly Sales:\n", monthly_sales)

#  Insight: The monthly sales trend shows a general upward trajectory with some seasonal fluctuations, suggesting that the business may experience higher sales during certain months, which could be leveraged for targeted marketing campaigns and inventory planning.

# -------------------------------
# 10. Top Products
# -------------------------------
top_products_query = """
SELECT product_name, SUM(sales) as revenue
FROM orders_clean
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;
"""

top_products = pd.read_sql(top_products_query, conn)
print("\nTop Products:\n", top_products)


# -------------------------------
# 11. Low Performing Products
# -------------------------------
low_products_query = """
SELECT product_name, SUM(sales) as revenue
FROM orders_clean
GROUP BY product_name
ORDER BY revenue ASC
LIMIT 10;
"""

low_products = pd.read_sql(low_products_query, conn)
print("\nLow Performing Products:\n", low_products)

# Insight: There is a significant revenue gap between top-performing and low-performing products, with the highest-selling product generating over 60K while several products contribute less than $10.


# -------------------------------
# 12. Customer Segmentation
# -------------------------------
customer_df = pd.read_sql("""
SELECT 
    "Customer ID",
    customer_name,
    SUM(sales) as total_spent
FROM orders_clean
GROUP BY "Customer ID", customer_name
""", conn)

# Segment customers into 3 groups
customer_df['segment'] = pd.qcut(
    customer_df['total_spent'],
    3,
    labels=['Low', 'Medium', 'High']
)

print("\nCustomer Segmentation:\n", customer_df.head())

# Insight: Customers are segmented into three groups based on total spending, with the 'High' segment representing the top spenders who contribute significantly to revenue, while the 'Low' segment may require targeted marketing efforts to increase engagement and spending.

# -------------------------------
# 13. Revenue Contribution by Category
# -------------------------------
contribution_query = """
SELECT 
    category,
    SUM(sales) as revenue,
    ROUND(SUM(sales) * 100.0 / SUM(SUM(sales)) OVER (), 2) as percent
FROM orders_clean
GROUP BY category;
"""

print("\nCategory Contribution:\n", pd.read_sql(contribution_query, conn))

# -------------------------------
# 0. KPI Calculations
# -------------------------------

kpi_query = """
SELECT 
    SUM(sales) AS total_sales,
    COUNT(DISTINCT "Order ID") AS total_orders,
    SUM(sales) * 1.0 / COUNT(DISTINCT "Order ID") AS avg_order_value
FROM orders_clean;
"""

kpis = pd.read_sql(kpi_query, conn)

total_sales = kpis['total_sales'][0]
total_orders = kpis['total_orders'][0]
avg_order_value = kpis['avg_order_value'][0]

print("\nKPI Summary:")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: ${avg_order_value:,.2f}")