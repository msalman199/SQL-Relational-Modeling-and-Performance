# 🗄️ Schema Design Exercises 

<div align="center">

# 🚀 Database Schema Design & Normalization 

### 📚 Hands-On PostgreSQL Database Design Exercise

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge\&logo=postgresql)
![SQL](https://img.shields.io/badge/SQL-DDL-success?style=for-the-badge\&logo=postgresql)
![Normalization](https://img.shields.io/badge/Normalization-1NF%20%7C%202NF%20%7C%203NF-orange?style=for-the-badge)
![Database Design](https://img.shields.io/badge/Database-Schema%20Design-purple?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-red?style=for-the-badge\&logo=linux)

### 🎯 Learn Entity Modeling, Relationships, Normalization & Schema Creation

</div>

---

# 📖 Overview

In this lab, you will design a relational database schema for a University Course Registration System.

You will:

✅ Identify entities and attributes

✅ Define relationships

✅ Apply normalization rules

✅ Create normalized tables

✅ Implement foreign key constraints

✅ Verify schema integrity

---

# 🎯 Learning Objectives

By the end of this lab, you will be able to:

* Identify entities and attributes from business requirements
* Design Entity Relationship (ER) models
* Apply 1NF, 2NF, and 3NF normalization
* Create normalized PostgreSQL tables
* Implement primary and foreign keys
* Validate relationships using SQL queries

---

# 📋 Prerequisites

| Requirement           | Description                               |
| --------------------- | ----------------------------------------- |
| 🐧 Linux Basics       | Basic command-line navigation             |
| 🗄️ Database Concepts | Understanding of tables and relationships |
| 🔑 Keys               | Knowledge of primary and foreign keys     |
| 📝 SQL Basics         | Familiarity with SQL data types           |
| 🔐 Access             | Linux machine with sudo privileges        |

---

# 🖥️ Environment Setup

## 🔹 Install PostgreSQL

Update packages:

```bash
sudo apt update
```

Install PostgreSQL:

```bash
sudo apt install -y postgresql postgresql-contrib
```

Start service:

```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

Connect as postgres user:

```bash
sudo -u postgres psql
```

---

## 🔹 Create Lab Database

```sql
CREATE DATABASE schema_lab;
```

Connect:

```sql
\c schema_lab
```

Exit:

```sql
\q
```

---

## 🔹 Access Database

```bash
sudo -u postgres psql -d schema_lab
```

---

# 🏗️ Task 1: Entity Identification & Relationship Design

---

## 📚 Business Scenario

Design a University Course Registration System.

Requirements:

* Students enroll in courses
* Courses are taught by instructors
* Instructors teach multiple courses
* Students receive grades
* Enrollment semester must be tracked

---

## 🔹 Step 1.1: Identify Entities

Create design notes:

```bash
nano schema_design.txt
```

### Example Entity Analysis

---

### 👨‍🎓 Students

Attributes:

* student_id (Primary Key)
* name
* email
* enrollment_date

---

### 👨‍🏫 Instructors

Attributes:

* instructor_id (Primary Key)
* name
* email
* department

---

### 📚 Courses

Attributes:

* course_id (Primary Key)
* course_code
* course_title
* credit_hours
* instructor_id (Foreign Key)

---

### 📝 Enrollments

Attributes:

* student_id
* course_id
* semester
* grade

---

## 🔹 Step 1.2: Define Relationships

Document relationships:

```text
Student ----- Enrolls In ----- Course
Cardinality: Many-to-Many

Instructor ----- Teaches ----- Course
Cardinality: One-to-Many
```

---

## 📊 ER Diagram

```text
Students
   |
   | M:N
   |
Enrollments
   |
   |
Courses
   |
   | 1:N
   |
Instructors
```

---

# 🧹 Task 2: Apply Normalization Rules

---

## 🔹 Step 2.1: Review Poor Design

Example of bad schema:

```sql
CREATE TABLE course_records (
    student_id INT,
    student_name VARCHAR(100),
    student_email VARCHAR(100),
    enrollment_date DATE,
    course_code VARCHAR(10),
    course_title VARCHAR(100),
    credit_hours INT,
    instructor_name VARCHAR(100),
    instructor_email VARCHAR(100),
    instructor_dept VARCHAR(50),
    semester VARCHAR(20),
    grade CHAR(2)
);
```

---

## 🔹 Step 2.2: Analyze Problems

Create file:

```bash
nano normalization_analysis.txt
```

---

### 🚫 Unnormalized Issues

* Student data repeated for every course
* Course data duplicated
* Instructor data duplicated

---

### 🚫 1NF Violations

* Potential repeating enrollment information

---

### 🚫 2NF Violations

* Student information depends only on student_id
* Course information depends only on course_code

---

### 🚫 3NF Violations

* Instructor department depends on instructor
* Instructor email depends on instructor

---

# ✅ Normalized Design

---

## 👨‍🎓 Students Table

```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    enrollment_date DATE NOT NULL
);
```

---

## 👨‍🏫 Instructors Table

```sql
CREATE TABLE instructors (
    instructor_id SERIAL PRIMARY KEY,
    instructor_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department VARCHAR(100) NOT NULL
);
```

---

## 📚 Courses Table

```sql
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    course_title VARCHAR(200) NOT NULL,
    credit_hours INT NOT NULL,
    instructor_id INT NOT NULL,
    FOREIGN KEY (instructor_id)
        REFERENCES instructors(instructor_id)
);
```

---

## 📝 Enrollments Table

```sql
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    semester VARCHAR(20) NOT NULL,
    grade CHAR(2),

    PRIMARY KEY(student_id, course_id),

    FOREIGN KEY(student_id)
        REFERENCES students(student_id),

    FOREIGN KEY(course_id)
        REFERENCES courses(course_id)
);
```

---

# 🚀 Task 3: Implement Schema

---

## 🔹 Step 3.1: Save Schema

Create SQL file:

```bash
nano normalized_schema.sql
```

Paste all CREATE TABLE statements.

Execute:

```bash
sudo -u postgres psql -d schema_lab -f normalized_schema.sql
```

---

## 🔹 Step 3.2: Insert Sample Data

Create:

```bash
nano sample_data.sql
```

---

### 👨‍🏫 Insert Instructors

```sql
INSERT INTO instructors
(instructor_name,email,department)
VALUES
('Dr. Ahmed','ahmed@uni.edu','Computer Science'),
('Dr. Sarah','sarah@uni.edu','Mathematics');
```

---

### 📚 Insert Courses

```sql
INSERT INTO courses
(course_code,course_title,credit_hours,instructor_id)
VALUES
('CS101','Database Systems',3,1),
('CS102','Operating Systems',4,1),
('MTH101','Calculus',3,2);
```

---

### 👨‍🎓 Insert Students

```sql
INSERT INTO students
(student_name,email,enrollment_date)
VALUES
('Ali Khan','ali@email.com','2024-01-01'),
('Sara Malik','sara@email.com','2024-01-02'),
('Usman Tariq','usman@email.com','2024-01-03');
```

---

### 📝 Insert Enrollments

```sql
INSERT INTO enrollments
VALUES
(1,1,'Fall2025','A'),

(1,2,'Fall2025','B+'),

(2,1,'Fall2025','A-'),

(2,3,'Fall2025','B'),

(3,2,'Fall2025','A');
```

Execute:

```bash
sudo -u postgres psql -d schema_lab -f sample_data.sql
```

---

# 🔍 Step 3.3: Verification Queries

Create:

```bash
nano verification_queries.sql
```

---

## Query 1: Courses with Instructors

```sql
SELECT
    c.course_title,
    i.instructor_name
FROM courses c
JOIN instructors i
ON c.instructor_id=i.instructor_id;
```

---

## Query 2: Students in CS101

```sql
SELECT
    s.student_name
FROM students s
JOIN enrollments e
ON s.student_id=e.student_id
JOIN courses c
ON e.course_id=c.course_id
WHERE c.course_code='CS101';
```

---

## Query 3: Student Grades

```sql
SELECT
    s.student_name,
    c.course_title,
    e.grade
FROM students s
JOIN enrollments e
ON s.student_id=e.student_id
JOIN courses c
ON c.course_id=e.course_id;
```

---

## Query 4: Enrollment Count

```sql
SELECT
    c.course_title,
    COUNT(*) AS total_students
FROM courses c
JOIN enrollments e
ON c.course_id=e.course_id
GROUP BY c.course_title;
```

---

Run verification:

```bash
sudo -u postgres psql -d schema_lab -f verification_queries.sql
```

---

# ✅ Verification

---

## List Tables

```sql
\dt
```

Expected:

```text
students
instructors
courses
enrollments
```

---

## Describe Tables

```sql
\d students
\d instructors
\d courses
\d enrollments
```

---

## Verify Foreign Keys

```sql
SELECT
    tc.table_name,
    kcu.column_name,
    ccu.table_name,
    ccu.column_name
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu
ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type='FOREIGN KEY';
```

---

# ✔️ Normalization Checklist

| Rule                  | Status                       |
| --------------------- | ---------------------------- |
| 1NF                   | ✅ Atomic Values              |
| 2NF                   | ✅ No Partial Dependencies    |
| 3NF                   | ✅ No Transitive Dependencies |
| Referential Integrity | ✅ Enforced                   |
| Redundancy            | ✅ Eliminated                 |

---

# 🚨 Troubleshooting

---

## Error: Relation Already Exists

```sql
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS students;
```

---

## Error: Foreign Key Violation

Insert data in this order:

```text
Instructors
    ↓
Courses
    ↓
Students
    ↓
Enrollments
```

---

## Error: Syntax Error

Check:

* Missing commas
* Missing semicolons
* Incorrect data types

---

# 🏆 Lab Completion Summary

Congratulations! 🎉

You successfully:

✅ Identified entities

✅ Defined relationships

✅ Designed ER structure

✅ Applied normalization

✅ Created normalized schema

✅ Implemented primary keys

✅ Implemented foreign keys

✅ Inserted sample data

✅ Verified relationships

---

# 🌟 Key Takeaways

🔹 Normalization reduces redundancy

🔹 Foreign keys enforce integrity

🔹 Junction tables solve many-to-many relationships

🔹 Proper schema design improves consistency

🔹 Good database design improves performance and scalability

---

# 🚀 Next Steps

Continue learning:

* BCNF Normalization
* Fourth Normal Form (4NF)
* Indexing Strategies
* Query Optimization
* Advanced ER Modeling
* Database Performance Tuning
* Data Warehousing Concepts

---

<div align="center">

# 🎯 Successfully Completed

## 🗄️ Schema Design & Normalization Mastered

### ⭐ Build Better Databases with Proper Design! ⭐

</div>
