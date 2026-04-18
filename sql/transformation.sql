DROP TABLE IF EXISTS orders_clean;

CREATE TABLE orders_clean AS
SELECT DISTINCT
    "Row ID",
    "Order ID",
    -- Fix Order Date
DATE(
    SUBSTR("Order Date", 7, 4) || '-' ||
    SUBSTR("Order Date", 4, 2) || '-' ||
    SUBSTR("Order Date", 1, 2)
) AS order_date,

-- Fix Ship Date
DATE(
    SUBSTR("Ship Date", 7, 4) || '-' ||
    SUBSTR("Ship Date", 4, 2) || '-' ||
    SUBSTR("Ship Date", 1, 2)
) AS ship_date,

    TRIM("Customer Name") AS customer_name,
    "Customer ID",

    TRIM(Segment) AS segment,
    TRIM(Category) AS category,
    TRIM("Sub-Category") AS sub_category,
    TRIM("Product Name") AS product_name,

    TRIM(Country) AS country,
    TRIM(City) AS city,
    TRIM(State) AS state,
    TRIM(Region) AS region,
    TRIM("Ship Mode") AS ship_mode,

    CAST(Sales AS REAL) AS sales

FROM orders
WHERE Sales IS NOT NULL
  AND Sales > 0;