# 🚀 Complex Query Writing 
### 🐘 PostgreSQL Advanced SQL Queries, JOINs, Subqueries & Analytics

<p align="center">

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Advanced_SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Complex_Queries-blue?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Database-Analytics-green?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=linux)
![Hands-On Lab](https://img.shields.io/badge/Hands--On-Lab-red?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Level-Intermediate-yellow?style=for-the-badge)

</p>

---

# 📖 Overview

This lab focuses on writing advanced SQL queries using PostgreSQL. You will learn how to combine data from multiple tables, use subqueries, perform analytical calculations with window functions, and generate business reports using advanced aggregations.

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

✅ Write advanced SQL queries using JOINs

✅ Combine data from multiple related tables

✅ Implement subqueries for complex filtering

✅ Use window functions for analytical calculations

✅ Apply GROUP BY and HAVING clauses

✅ Create business intelligence reports

✅ Analyze sales and customer data efficiently

---

# 🛠️ Prerequisites

- Basic SQL knowledge (SELECT, WHERE, ORDER BY)
- Understanding of database tables
- Familiarity with relational databases
- Linux command-line basics
- PostgreSQL fundamentals

---

# 🌍 Environment Setup

---

## 🔄 Step 1: Update Package Repository

```bash
sudo apt update
```

---

## 📦 Step 2: Install PostgreSQL

```bash
sudo apt install -y postgresql postgresql-contrib
```

---

## ▶️ Step 3: Start PostgreSQL

```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

---

## 👤 Step 4: Switch to PostgreSQL User

```bash
sudo -i -u postgres
```

---

# 🗄️ Create Database and Sample Data

---

## 🔹 Access PostgreSQL

```bash
psql
```

---

## 🔹 Create Database

```sql
CREATE DATABASE sales_analytics;
```

---

## 🔹 Connect Database

```sql
\c sales_analytics
```

---

# 🏗️ Create Tables

---

## 👥 Customers Table

```sql
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    country VARCHAR(50),
    registration_date DATE
);
```

---

## 📦 Products Table

```sql
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10,2)
);
```

---

## 🛒 Orders Table

```sql
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE,
    total_amount DECIMAL(10,2)
);
```

---

## 📋 Order Items Table

```sql
CREATE TABLE order_items (
    item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    price DECIMAL(10,2)
);
```

---

# 📝 Insert Sample Data

---

## 👥 Customers

```sql
INSERT INTO customers (customer_name, city, country, registration_date) VALUES
('Alice Johnson', 'New York', 'USA', '2023-01-15'),
('Bob Smith', 'Los Angeles', 'USA', '2023-02-20'),
('Carol White', 'Chicago', 'USA', '2023-03-10'),
('David Brown', 'Houston', 'USA', '2023-04-05'),
('Eve Davis', 'Phoenix', 'USA', '2023-05-12');
```

---

## 📦 Products

```sql
INSERT INTO products (product_name, category, unit_price) VALUES
('Laptop', 'Electronics', 999.99),
('Mouse', 'Electronics', 29.99),
('Keyboard', 'Electronics', 79.99),
('Desk Chair', 'Furniture', 249.99),
('Monitor', 'Electronics', 399.99),
('Desk Lamp', 'Furniture', 49.99);
```

---

## 🛒 Orders

```sql
INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2023-06-01', 1079.98),
(2, '2023-06-05', 249.99),
(1, '2023-06-10', 399.99),
(3, '2023-06-15', 1329.97),
(4, '2023-06-20', 79.98),
(5, '2023-06-25', 999.99),
(2, '2023-07-01', 449.98),
(3, '2023-07-05', 29.99);
```

---

## 📋 Order Items

```sql
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 999.99),
(1, 3, 1, 79.99),
(2, 4, 1, 249.99),
(3, 5, 1, 399.99),
(4, 1, 1, 999.99),
(4, 2, 1, 29.99),
(4, 6, 6, 49.99),
(5, 2, 1, 29.99),
(5, 6, 1, 49.99),
(6, 1, 1, 999.99),
(7, 5, 1, 399.99),
(7, 6, 1, 49.99),
(8, 2, 1, 29.99);
```

---

# 🔥 Task 1: Working with JOINs

---

## 🎯 Objective

Combine multiple tables to create business reports.

---

## 🔹 Step 1: INNER JOIN

```sql
SELECT
    o.order_id,
    o.order_date,
    c.customer_name,
    c.city,
    o.total_amount
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
ORDER BY o.order_date;
```

---

## 🔹 Step 2: Multiple JOINs

```sql
SELECT
    o.order_id,
    c.customer_name,
    p.product_name,
    oi.quantity,
    oi.price
FROM order_items oi
JOIN orders o
ON oi.order_id = o.order_id
JOIN products p
ON oi.product_id = p.product_id
JOIN customers c
ON o.customer_id = c.customer_id
WHERE p.category='Electronics'
ORDER BY o.order_id;
```

---

## 🔹 Step 3: LEFT JOIN

Find customers without orders.

```sql
SELECT
    c.customer_name,
    c.city,
    c.registration_date
FROM customers c
LEFT JOIN orders o
ON c.customer_id=o.customer_id
WHERE o.order_id IS NULL;
```

---

# 🔍 Task 2: Subqueries

---

## 🎯 Objective

Use nested SQL queries for advanced filtering.

---

## 🔹 Products Ordered More Than Once

```sql
SELECT product_name, category, unit_price
FROM products
WHERE product_id IN (
    SELECT product_id
    FROM order_items
    GROUP BY product_id
    HAVING COUNT(*) > 1
);
```

---

## 🔹 Customers Spending Above Average

```sql
SELECT
    c.customer_name,
    (
        SELECT SUM(total_amount)
        FROM orders o2
        WHERE o2.customer_id=c.customer_id
    ) AS total_spent
FROM customers c
WHERE (
        SELECT SUM(total_amount)
        FROM orders o2
        WHERE o2.customer_id=c.customer_id
      )
>
(
    SELECT AVG(customer_total)
    FROM (
        SELECT SUM(total_amount) AS customer_total
        FROM orders
        GROUP BY customer_id
    ) avg_table
)
ORDER BY total_spent DESC;
```

---

## 🔹 Customer Order Counts

```sql
SELECT
    customer_name,
    city,
    (
        SELECT COUNT(*)
        FROM orders o
        WHERE o.customer_id=c.customer_id
    ) AS order_count
FROM customers c
ORDER BY order_count DESC;
```

---

# 📊 Task 3: Window Functions

---

## 🎯 Objective

Perform advanced analytical calculations.

---

## 🏆 ROW_NUMBER & RANK

```sql
SELECT
    c.customer_name,
    SUM(o.total_amount) AS total_spent,
    ROW_NUMBER() OVER(ORDER BY SUM(o.total_amount) DESC) AS row_num,
    RANK() OVER(ORDER BY SUM(o.total_amount) DESC) AS rank_num
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;
```

---

## 📈 Running Total

```sql
SELECT
    order_date,
    SUM(total_amount) AS daily_total,
    SUM(SUM(total_amount))
    OVER(ORDER BY order_date) AS running_total
FROM orders
GROUP BY order_date
ORDER BY order_date;
```

---

## 🥇 Customer Order Ranking

```sql
SELECT
    c.customer_name,
    o.order_date,
    o.total_amount,
    ROW_NUMBER()
    OVER(
        PARTITION BY o.customer_id
        ORDER BY o.order_date
    ) AS order_rank
FROM orders o
JOIN customers c
ON o.customer_id=c.customer_id
ORDER BY c.customer_name;
```

---

# 📊 Task 4: Advanced Aggregations

---

## 🎯 Objective

Generate analytical business reports.

---

## 📅 Sales by Category and Month

```sql
SELECT
    p.category,
    DATE_TRUNC('month',o.order_date) AS month,
    SUM(oi.price*oi.quantity) AS total_sales,
    COUNT(*) AS order_count,
    AVG(oi.price) AS avg_order_value
FROM order_items oi
JOIN orders o
ON oi.order_id=o.order_id
JOIN products p
ON oi.product_id=p.product_id
GROUP BY p.category,
         DATE_TRUNC('month',o.order_date)
HAVING SUM(oi.price*oi.quantity) > 500
ORDER BY month;
```

---

## 🌎 ROLLUP Report

```sql
SELECT
    COALESCE(country,'ALL COUNTRIES') AS country,
    COALESCE(city,'ALL CITIES') AS city,
    SUM(o.total_amount) AS total_sales
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY ROLLUP(country,city)
ORDER BY country,city;
```

---

## 💰 Customer Spending Categories

```sql
SELECT
CASE
    WHEN customer_total > 1000 THEN 'High'
    WHEN customer_total BETWEEN 500 AND 1000 THEN 'Medium'
    ELSE 'Low'
END AS spending_category,
COUNT(*) AS customer_count,
SUM(customer_total) AS total_revenue
FROM (
    SELECT
        customer_id,
        SUM(total_amount) AS customer_total
    FROM orders
    GROUP BY customer_id
) customer_spending
GROUP BY spending_category
ORDER BY total_revenue DESC;
```

---

# ✅ Verification Commands

---

## 🔍 Verify Product Categories

```sql
SELECT DISTINCT category
FROM order_items oi
JOIN products p
ON oi.product_id=p.product_id;
```

---

## 🔍 Verify Products Ordered More Than Once

```sql
SELECT
    product_id,
    COUNT(*) AS order_count
FROM order_items
GROUP BY product_id
HAVING COUNT(*) > 1;
```

---

## 🔍 Verify Running Totals

```sql
SELECT
    order_date,
    SUM(total_amount)
    OVER(ORDER BY order_date) AS running_total
FROM orders
ORDER BY order_date;
```

---

## 🔍 Verify Total Sales

```sql
SELECT SUM(total_amount)
FROM orders;
```

---

# 🛠️ Troubleshooting

---

## ❌ JOIN Returns Too Many Rows

✔ Verify JOIN conditions

✔ Check foreign key relationships

✔ Use DISTINCT if necessary

---

## ❌ Subquery Returns Multiple Rows

✔ Use `IN` instead of `=`

✔ Add `LIMIT 1` when needed

✔ Verify subquery logic

---

## ❌ Window Function Error

✔ Ensure `OVER()` clause exists

✔ Verify `PARTITION BY`

✔ Verify `ORDER BY`

---

## ❌ GROUP BY Error

✔ Include all non-aggregated columns

✔ Verify column names

✔ Check aggregate functions

---

# 🎓 Lab Summary

Congratulations! You have successfully learned:

✅ INNER JOIN, LEFT JOIN, and Multi-Table JOINs

✅ Nested Subqueries

✅ Correlated Subqueries

✅ Window Functions

✅ ROW_NUMBER(), RANK()

✅ Running Totals

✅ PARTITION BY

✅ GROUP BY & HAVING

✅ ROLLUP Reports

✅ CASE-Based Analytics

✅ Business Intelligence Query Techniques

---

# 🚀 Key Takeaways

- JOINs combine related tables into meaningful reports.
- Subqueries enable advanced filtering and calculations.
- Window functions provide powerful analytical capabilities.
- Aggregations summarize large datasets efficiently.
- Complex SQL skills are essential for Data Analytics, BI, Data Engineering, and Database Administration.

---

# 🔚 Exit PostgreSQL

```sql
\q
```

---

# ⛔ Stop PostgreSQL Service

```bash
exit
sudo systemctl stop postgresql
```

---

## 🎉 Congratulations!

You have completed the **Complex Query Writing Lab** and are now capable of creating advanced SQL reports using PostgreSQL for real-world business analytics and data-driven decision making.

🚀 Happy Querying!
