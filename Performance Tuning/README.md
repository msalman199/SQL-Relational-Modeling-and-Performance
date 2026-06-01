# ⚡ PostgreSQL Performance Tuning 
### 🚀 Index Optimization, Query Analysis & Database Configuration Tuning

<p align="center">

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Performance_Tuning-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Optimization-blue?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Database-Indexing-green?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Server-orange?style=for-the-badge&logo=linux)
![Performance](https://img.shields.io/badge/Focus-Performance_Improvement-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Advanced-yellow?style=for-the-badge)

</p>

---

# 📖 Overview

This lab focuses on **PostgreSQL performance optimization techniques**, including query analysis, indexing strategies, configuration tuning, and benchmarking improvements.

You will learn how to identify slow queries and dramatically improve database performance using real-world optimization techniques.

---

# 🎯 Learning Objectives

By the end of this lab, you will be able to:

✅ Identify slow SQL queries using `EXPLAIN ANALYZE`  
✅ Create and optimize indexes  
✅ Tune PostgreSQL configuration parameters  
✅ Benchmark query performance improvements  
✅ Analyze query execution plans  
✅ Improve database scalability and efficiency  

---

# 🛠️ Prerequisites

- Basic SQL knowledge (SELECT, JOIN, WHERE)
- Understanding of relational databases
- Linux command-line basics
- PostgreSQL fundamentals
- Awareness of database performance concepts

---

# ⚙️ Environment Setup

---

## 🔄 Step 1: Update System

```bash
sudo apt update
```

---

## 📦 Step 2: Install PostgreSQL

```bash
sudo apt install -y postgresql postgresql-contrib
```

---

## ▶️ Step 3: Start Service

```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

---

## 👤 Step 4: Switch User

```bash
sudo -i -u postgres
```

---

# 🗄️ Create Test Database

---

```bash
createdb perflab
psql perflab
```

---

# 📊 Generate Sample Data

---

## 👤 Users Table

```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 📦 Orders Table

```sql
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER,
    product_name VARCHAR(100),
    amount DECIMAL(10,2),
    order_date TIMESTAMP DEFAULT NOW()
);
```

---

## 🚀 Insert Large Dataset

```sql
INSERT INTO users (username, email)
SELECT 
    'user_' || generate_series,
    'user_' || generate_series || '@example.com'
FROM generate_series(1, 100000);
```

---

```sql
INSERT INTO orders (user_id, product_name, amount, order_date)
SELECT 
    (random() * 99999 + 1)::INTEGER,
    'Product_' || (random() * 100)::INTEGER,
    (random() * 1000)::DECIMAL(10,2),
    NOW() - (random() * 365 || ' days')::INTERVAL
FROM generate_series(1, 500000);
```

---

# 🔥 Task 1: Analyze Slow Queries

---

## ⏱️ Enable Timing

```sql
\timing on
```

---

## 🐌 Baseline Queries

```sql
SELECT u.username, COUNT(o.order_id), SUM(o.amount)
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE u.email LIKE '%5000@%'
GROUP BY u.username;
```

---

```sql
SELECT * FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-06-30'
ORDER BY amount DESC
LIMIT 100;
```

---

```sql
SELECT product_name, COUNT(*), AVG(amount)
FROM orders
WHERE amount > 500
GROUP BY product_name;
```

---

## 🧠 Analyze Execution Plan

```sql
EXPLAIN ANALYZE
SELECT u.username, COUNT(o.order_id)
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE u.email LIKE '%5000@%'
GROUP BY u.username;
```

---

### 📌 Key Metrics to Record:

- Execution Time
- Planning Time
- Scan Type (Seq Scan / Index Scan)
- Rows Processed

---

# 🚧 Task 2: Index Optimization

---

## 📌 Create Indexes

```sql
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_users_email ON users(email);
```

---

## ⚡ Composite Indexes

```sql
CREATE INDEX idx_orders_amount_date ON orders(amount, order_date);

CREATE INDEX idx_orders_product ON orders(product_name);
```

---

## 🔍 Verify Index Usage

```sql
EXPLAIN ANALYZE
SELECT u.username, COUNT(o.order_id)
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE u.email LIKE '%5000@%'
GROUP BY u.username;
```

---

## 📊 Check Index Stats

```sql
\d orders
```

---

# ⚙️ Task 3: Database Configuration Tuning

---

## 🔍 Check Settings

```sql
SHOW shared_buffers;
SHOW work_mem;
SHOW effective_cache_size;
```

---

## ⚡ Recommended Settings

| Parameter | Value |
|----------|------|
| shared_buffers | 1GB |
| effective_cache_size | 3GB |
| work_mem | 32MB |
| maintenance_work_mem | 512MB |

---

## 🛠️ Edit Config

```bash
sudo nano /etc/postgresql/*/main/postgresql.conf
```

---

## 📌 Update Values

```conf
shared_buffers = 1GB
effective_cache_size = 3GB
work_mem = 32MB
maintenance_work_mem = 512MB
random_page_cost = 1.1
```

---

## 🔄 Restart Service

```bash
sudo systemctl restart postgresql
```

---

# 📈 Task 4: Benchmark Performance

---

## 🧪 Benchmark Script

```sql
\timing on
```

---

```sql
SELECT u.username, COUNT(o.order_id), SUM(o.amount)
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE u.email LIKE '%5000@%'
GROUP BY u.username;
```

---

```sql
SELECT * FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-06-30'
AND amount > 500
ORDER BY amount DESC
LIMIT 100;
```

---

## 📊 Compare Results

| Query | Before | After | Improvement |
|------|--------|------|------------|
| Q1 | ___ ms | ___ ms | ___ % |
| Q2 | ___ ms | ___ ms | ___ % |
| Q3 | ___ ms | ___ ms | ___ % |

---

# 📊 Advanced Analysis

---

## 💾 Cache Hit Ratio

```sql
SELECT 
    sum(heap_blks_hit) / 
    (sum(heap_blks_hit) + sum(heap_blks_read)) * 100 AS cache_hit_ratio
FROM pg_statio_user_tables;
```

---

## 🔍 Unused Indexes

```sql
SELECT 
    indexname,
    idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0;
```

---

# 🧪 Verification

---

## ✔ Index Verification

```sql
SELECT indexname FROM pg_indexes WHERE tablename='orders';
```

---

## ✔ Config Verification

```sql
SELECT name, setting
FROM pg_settings
WHERE name IN ('shared_buffers','work_mem');
```

---

## ✔ Performance Test

```sql
EXPLAIN ANALYZE
SELECT u.username, COUNT(o.order_id)
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.username;
```

---

# 🛠️ Troubleshooting

---

## ❌ Index Not Used

✔ Run ANALYZE

```sql
ANALYZE users;
ANALYZE orders;
```

---

## ❌ Slow Query Still Slow

✔ Check execution plan  
✔ Avoid functions on indexed columns  
✔ Verify WHERE clause usage  

---

## ❌ Out of Memory

```sql
SET work_mem = '16MB';
```

---

# 🎓 Conclusion

You have successfully learned:

✅ Query performance analysis  
✅ Index creation & optimization  
✅ Composite indexing  
✅ PostgreSQL tuning parameters  
✅ Benchmarking techniques  
✅ Execution plan analysis  

---

# 🚀 Key Takeaways

- Indexes significantly improve read performance
- EXPLAIN ANALYZE is essential for optimization
- Configuration tuning depends on system resources
- Always benchmark before and after changes
- Statistics (ANALYZE) help query planner decisions

---

# 🔚 Cleanup (Optional)

```sql
\q
```

```bash
exit
sudo -u postgres dropdb perflab
```

---

## 🎉 Congratulations!

You now understand **real-world PostgreSQL performance tuning techniques** used in production systems for scaling databases and improving query efficiency.

🚀 Keep optimizing like a Database Engineer!
