# 📊 Run Read-Only SQL Queries with SQLite

<div align="center">

# 🚀 SQLite Read-Only Query 

### 📚 Learn SQL Data Retrieval, Filtering, Sorting & Analysis

![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![SQL](https://img.shields.io/badge/SQL-Queries-success?style=for-the-badge&logo=mysql)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=linux)
![Data Analysis](https://img.shields.io/badge/Data-Analysis-purple?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Lab-red?style=for-the-badge)

### 🎯 Master SELECT, WHERE, ORDER BY, LIMIT & Aggregate Functions

</div>

---

# 📖 Overview

This lab introduces the fundamentals of SQL read-only queries using SQLite. You will learn how to retrieve, filter, sort, limit, and analyze data without modifying the database.

Read-only queries are among the safest SQL operations because they never alter data, making them perfect for learning and data exploration.

---

# 🎯 Learning Objectives

By the end of this lab, you will be able to:

✅ Execute SELECT queries

✅ Retrieve data from database tables

✅ Filter records using WHERE

✅ Sort data using ORDER BY

✅ Limit results using LIMIT

✅ Use aggregate functions

✅ Analyze and interpret query results

✅ Join multiple tables

---

# 📋 Prerequisites

| Requirement | Description |
|------------|-------------|
| 🐧 Linux Basics | Basic command-line knowledge |
| 🗄️ Database Awareness | Understanding of what a database is |
| 📂 Terminal Navigation | Familiarity with Linux terminal |
| 🎯 SQL Experience | Not Required |

---

# 🖥️ Environment Information

| Component | Value |
|------------|---------|
| Database Engine | SQLite |
| Operating System | Ubuntu / Debian Linux |
| Database File | company.db |
| Estimated Duration | 60 Minutes |

---

# 🏗️ SQL Learning Architecture

```text
┌───────────────────┐
│ SQLite Database   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ SELECT Queries    │
└─────────┬─────────┘
          │
          ▼
 ┌─────────────────┐
 │ Filter Data     │
 │ WHERE Clause    │
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │ Sort Results    │
 │ ORDER BY        │
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │ Limit Results   │
 │ LIMIT Clause    │
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │ Analyze Data    │
 │ COUNT AVG SUM   │
 └─────────────────┘
```

---

# 🛠️ Environment Setup

---

# 🔹 Step 1: Install SQLite

Update package repositories.

```bash
sudo apt update
```

Install SQLite.

```bash
sudo apt install -y sqlite3
```

Verify installation.

```bash
sqlite3 --version
```

### ✅ Expected Output

```text
3.x.x
```

---

# 🔹 Step 2: Create Lab Directory

Create a workspace.

```bash
mkdir ~/sql-lab
cd ~/sql-lab
```

---

# 🔹 Step 3: Create Database

Launch SQLite.

```bash
sqlite3 company.db
```

### ✅ Expected Output

```text
SQLite version x.x.x
sqlite>
```

---

# 🛠️ Create Sample Database

---

## 🔹 Create Departments Table

```sql
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT NOT NULL,
    location TEXT
);
```

---

## 🔹 Create Employees Table

```sql
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dept_id INTEGER,
    salary REAL,
    hire_date TEXT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

---

## 🔹 Insert Department Data

```sql
INSERT INTO departments VALUES (1, 'Engineering', 'New York');
INSERT INTO departments VALUES (2, 'Sales', 'Chicago');
INSERT INTO departments VALUES (3, 'Marketing', 'Los Angeles');
INSERT INTO departments VALUES (4, 'HR', 'New York');
```

---

## 🔹 Insert Employee Data

```sql
INSERT INTO employees VALUES (1, 'John', 'Smith', 1, 75000, '2020-01-15');
INSERT INTO employees VALUES (2, 'Sarah', 'Johnson', 2, 65000, '2019-03-22');
INSERT INTO employees VALUES (3, 'Mike', 'Williams', 1, 82000, '2018-07-10');
INSERT INTO employees VALUES (4, 'Emily', 'Brown', 3, 58000, '2021-05-18');
INSERT INTO employees VALUES (5, 'David', 'Jones', 1, 71000, '2020-11-03');
INSERT INTO employees VALUES (6, 'Lisa', 'Davis', 2, 69000, '2019-09-14');
INSERT INTO employees VALUES (7, 'James', 'Miller', 4, 54000, '2021-02-28');
INSERT INTO employees VALUES (8, 'Anna', 'Wilson', 3, 62000, '2020-06-07');
```

Exit SQLite.

```sql
.quit
```

---

# 🎯 Task 1: Run Basic SELECT Queries

---

## 🔹 Step 1: Connect to Database

```bash
sqlite3 company.db
```

---

## 🔹 Step 2: View Available Tables

```sql
.tables
```

### ✅ Expected Output

```text
departments
employees
```

---

## 🔹 Step 3: View Table Structure

Employees table schema:

```sql
.schema employees
```

Departments table schema:

```sql
.schema departments
```

### 📌 Observe

- Column names
- Data types
- Primary keys
- Foreign keys
- Relationships

---

## 🔹 Step 4: Basic SELECT Queries

Select all employee data.

```sql
SELECT * FROM employees;
```

---

Select specific columns.

```sql
SELECT first_name, last_name, salary
FROM employees;
```

---

View all departments.

```sql
SELECT * FROM departments;
```

---

View department names only.

```sql
SELECT dept_name
FROM departments;
```

### 💡 Key Concept

```sql
*
```

means "all columns".

Selecting specific columns improves performance and readability.

---

# 🎯 Task 2: Filter Data Using WHERE

---

## 🔹 Step 1: Numeric Filtering

Employees earning above 70,000.

```sql
SELECT first_name,last_name,salary
FROM employees
WHERE salary > 70000;
```

---

Employees earning exactly 65,000.

```sql
SELECT first_name,last_name,salary
FROM employees
WHERE salary = 65000;
```

---

Employees in Department 1.

```sql
SELECT first_name,last_name,dept_id
FROM employees
WHERE dept_id = 1;
```

---

## 🔹 Step 2: Text Filtering

Find John Smith.

```sql
SELECT *
FROM employees
WHERE first_name='John'
AND last_name='Smith';
```

---

Last names starting with J.

```sql
SELECT first_name,last_name
FROM employees
WHERE last_name LIKE 'J%';
```

---

Departments in New York.

```sql
SELECT *
FROM departments
WHERE location='New York';
```

### 💡 Important Note

SQL Keywords:

```sql
SELECT
WHERE
FROM
```

are case-insensitive.

Text values are case-sensitive.

Always use:

```sql
'Text'
```

for string values.

---

## 🔹 Step 3: Multiple Conditions

Engineering employees earning over 70,000.

```sql
SELECT e.first_name,
       e.last_name,
       e.salary,
       d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id=d.dept_id
WHERE d.dept_name='Engineering'
AND e.salary>70000;
```

---

Employees hired in 2020 or 2021.

```sql
SELECT first_name,last_name,hire_date
FROM employees
WHERE hire_date LIKE '2020%'
OR hire_date LIKE '2021%';
```

---

# 🎯 Task 3: Sort and Limit Results

---

## 🔹 Step 1: ORDER BY

Sort salaries ascending.

```sql
SELECT first_name,last_name,salary
FROM employees
ORDER BY salary;
```

---

Sort salaries descending.

```sql
SELECT first_name,last_name,salary
FROM employees
ORDER BY salary DESC;
```

---

Sort by last name.

```sql
SELECT first_name,last_name
FROM employees
ORDER BY last_name;
```

---

Sort by department then salary.

```sql
SELECT first_name,last_name,dept_id,salary
FROM employees
ORDER BY dept_id,salary DESC;
```

### 💡 Key Concept

| Keyword | Meaning |
|----------|---------|
| ASC | Ascending (Default) |
| DESC | Descending |

---

## 🔹 Step 2: LIMIT Results

Top 3 highest-paid employees.

```sql
SELECT first_name,last_name,salary
FROM employees
ORDER BY salary DESC
LIMIT 3;
```

---

Most recently hired employees.

```sql
SELECT first_name,last_name,hire_date
FROM employees
ORDER BY hire_date DESC
LIMIT 5;
```

---

First 2 employees alphabetically.

```sql
SELECT first_name,last_name
FROM employees
ORDER BY last_name
LIMIT 2;
```

---

## 🔹 Step 3: Combine WHERE + ORDER BY + LIMIT

Top Engineering employees.

```sql
SELECT e.first_name,
       e.last_name,
       e.salary,
       d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id=d.dept_id
WHERE d.dept_name='Engineering'
ORDER BY e.salary DESC
LIMIT 2;
```

---

Employees earning above 60k sorted by hire date.

```sql
SELECT first_name,
       last_name,
       salary,
       hire_date
FROM employees
WHERE salary > 60000
ORDER BY hire_date
LIMIT 3;
```

---

# 🎯 Task 4: Analyze Query Results

---

## 🔹 Step 1: COUNT Function

Total employees.

```sql
SELECT COUNT(*)
FROM employees;
```

---

Employees per department.

```sql
SELECT dept_id,
COUNT(*) AS employee_count
FROM employees
GROUP BY dept_id;
```

---

Departments per location.

```sql
SELECT location,
COUNT(*) AS dept_count
FROM departments
GROUP BY location;
```

---

## 🔹 Step 2: Aggregate Functions

Average salary.

```sql
SELECT AVG(salary)
FROM employees;
```

---

Minimum and maximum salaries.

```sql
SELECT MIN(salary),
       MAX(salary)
FROM employees;
```

---

Total salary by department.

```sql
SELECT d.dept_name,
SUM(e.salary)
FROM employees e
JOIN departments d
ON e.dept_id=d.dept_id
GROUP BY d.dept_name;
```

---

Average salary by department.

```sql
SELECT d.dept_name,
AVG(e.salary)
FROM employees e
JOIN departments d
ON e.dept_id=d.dept_id
GROUP BY d.dept_name
ORDER BY AVG(e.salary) DESC;
```

---

# 📈 Comprehensive Analysis Query

```sql
SELECT
e.first_name || ' ' || e.last_name AS full_name,
d.dept_name,
d.location,
e.salary,
e.hire_date
FROM employees e
JOIN departments d
ON e.dept_id=d.dept_id
WHERE e.salary >= 60000
ORDER BY d.dept_name,e.salary DESC;
```

### 🔍 Questions to Analyze

- How many employees earn above 60,000?
- Which department has the highest earners?
- Which location contains the most employees?
- What hiring patterns do you observe?

---

# ✅ Verification Exercises

---

## 1️⃣ Sales Department Employees

```sql
SELECT e.first_name,
       e.last_name,
       d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id=d.dept_id
WHERE d.dept_name='Sales';
```

### Expected

```text
Sarah Johnson
Lisa Davis
```

---

## 2️⃣ Lowest Paid Employees

```sql
SELECT first_name,last_name,salary
FROM employees
ORDER BY salary
LIMIT 3;
```

### Expected

```text
James Miller
Emily Brown
Anna Wilson
```

---

## 3️⃣ Employees Hired in 2020

```sql
SELECT COUNT(*)
FROM employees
WHERE hire_date LIKE '2020%';
```

### Expected

```text
3
```

---

## 4️⃣ Average Salary After 2019

```sql
SELECT AVG(salary)
FROM employees
WHERE hire_date > '2019-12-31';
```

### Expected

```text
Approximately 65000
```

---

# 🚨 Troubleshooting Guide

---

## ❌ No Such Table

### Solution

Connect to correct database.

```bash
sqlite3 company.db
```

---

## ❌ Query Returns No Results

### Solution

Check:

- Spelling
- WHERE conditions
- Data values
- Table contents

---

## ❌ Syntax Error

### Solution

Use single quotes:

```sql
'John'
```

NOT:

```sql
"John"
```

---

## ❌ Column Not Found

### Solution

Check schema.

```sql
.schema employees
```

or

```sql
.schema departments
```

---

# 🎓 SQL Commands Cheat Sheet

| Command | Purpose |
|----------|---------|
| SELECT | Retrieve data |
| FROM | Specify table |
| WHERE | Filter rows |
| ORDER BY | Sort results |
| LIMIT | Restrict output |
| COUNT() | Count rows |
| AVG() | Average values |
| SUM() | Total values |
| MIN() | Lowest value |
| MAX() | Highest value |
| GROUP BY | Group records |
| JOIN | Combine tables |

---

# 🏆 Lab Completion Summary

Congratulations! 🎉

You have successfully:

✅ Installed SQLite

✅ Created a Database

✅ Created Tables

✅ Inserted Sample Data

✅ Executed SELECT Queries

✅ Filtered Records with WHERE

✅ Sorted Results with ORDER BY

✅ Limited Results with LIMIT

✅ Joined Multiple Tables

✅ Used Aggregate Functions

✅ Analyzed Business Data

---

# 🌟 Why These Skills Matter

SQL is the foundation of modern data systems.

These skills are essential for:

👨‍💻 Software Engineers

☁️ Cloud Engineers

⚙️ DevOps Engineers

📊 Data Analysts

🗄️ Database Administrators

📈 Business Intelligence Teams

Mastering read-only queries allows you to safely explore, analyze, and understand data before making any modifications.

---

# 🚀 Next Steps

Continue learning:

🔹 INSERT Statements

🔹 UPDATE Records

🔹 DELETE Operations

🔹 Advanced JOINs

🔹 Subqueries

🔹 Views

🔹 Indexes

🔹 Database Optimization

🔹 PostgreSQL & MySQL Administration

---

<div align="center">

# 🎯 Successfully Completed

## 📊 SQL Read-Only Query Fundamentals Mastered

### ⭐ Keep Practicing SQL and Become a Data Expert! ⭐

</div>
