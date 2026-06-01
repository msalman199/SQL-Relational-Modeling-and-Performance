# 🐘 Connect to PostgreSQL Guide

<div align="center">

# 🚀 Connect to PostgreSQL

### 📚 Complete Hands-On PostgreSQL Installation & Connection 

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=linux)
![CLI](https://img.shields.io/badge/Command-Line-black?style=for-the-badge&logo=gnubash)
![Database](https://img.shields.io/badge/SQL-Database-success?style=for-the-badge&logo=sqlite)
![DevOps](https://img.shields.io/badge/DevOps-Lab-red?style=for-the-badge&logo=dev.to)

### 🎯 Learn PostgreSQL Installation, Configuration, Authentication & Connectivity

</div>

---

# 📖 Overview

This lab introduces PostgreSQL, one of the world's most popular open-source relational database systems. You will install PostgreSQL, connect using the command-line interface, create databases and users, configure authentication, and verify connectivity.

---

# 🎯 Learning Objectives

By the end of this lab, you will be able to:

✅ Install PostgreSQL server and client tools

✅ Verify PostgreSQL service status

✅ Connect using PostgreSQL command-line client (psql)

✅ Create databases and database users

✅ Configure password authentication

✅ Test database connectivity

✅ Troubleshoot common PostgreSQL issues

---

# 📋 Prerequisites

| Requirement | Description |
|------------|-------------|
| 🐧 Linux Knowledge | Basic Linux command line skills |
| 🗄️ Database Basics | Understanding of databases |
| 🔐 Sudo Access | Access to a Linux machine with sudo privileges |
| 🌐 Internet Access | Required for package installation |

---

# 🖥️ Environment Information

| Component | Value |
|------------|---------|
| Operating System | Ubuntu / Debian Linux |
| Database | PostgreSQL |
| Client Tool | psql |
| Estimated Duration | 45 Minutes |

---

# 🏗️ Architecture Overview

```text
┌─────────────────┐
│ Linux Machine   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ PostgreSQL      │
│ Server          │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ psql Client     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Databases       │
│ Users & Roles   │
└─────────────────┘
```

---

# 🛠️ Task 1: Install PostgreSQL

---

## 🔹 Step 1: Update Package Repository

Before installing software, update your package repository.

```bash
sudo apt update
```

### 📌 What This Does

- Refreshes package information
- Downloads latest repository metadata
- Ensures newest packages are available

### ✅ Expected Result

```text
Package lists updated successfully
```

---

## 🔹 Step 2: Install PostgreSQL

Install PostgreSQL server and additional utilities.

```bash
sudo apt install postgresql postgresql-contrib -y
```

### 📌 Components Installed

| Package | Purpose |
|----------|----------|
| postgresql | Database Server |
| postgresql-contrib | Additional Extensions |
| psql | Database Client |

### ✅ Expected Result

```text
Installation completed successfully
```

---

## 🔹 Step 3: Verify PostgreSQL Service

Check PostgreSQL status.

```bash
sudo systemctl status postgresql
```

### ✅ Expected Output

```text
Active: active (running)
```

### 🚨 If Not Running

Start the service manually:

```bash
sudo systemctl start postgresql
```

Verify again:

```bash
sudo systemctl status postgresql
```

---

## 🔹 Step 4: Check PostgreSQL Version

Verify installation.

```bash
psql --version
```

### ✅ Expected Output

```text
psql (PostgreSQL) 14.x
```

---

# 🛠️ Task 2: Configure Database Credentials and Connect

---

## 🔹 Step 1: Switch to PostgreSQL User

PostgreSQL automatically creates a system account named postgres.

```bash
sudo -i -u postgres
```

### 📌 Purpose

Provides administrative database access.

### ✅ Expected Result

```bash
postgres@hostname:~$
```

---

## 🔹 Step 2: Access PostgreSQL Prompt

Launch PostgreSQL shell.

```bash
psql
```

### ✅ Expected Output

```text
postgres=#
```

### 📌 Meaning

You are now connected to PostgreSQL.

---

## 🔹 Step 3: List All Databases

Display available databases.

```sql
\l
```

### ✅ Expected Databases

```text
postgres
template0
template1
```

---

## 🔹 Step 4: Display Connection Information

Check connection details.

```sql
\conninfo
```

### ✅ Example Output

```text
Connected to database "postgres"
User "postgres"
Port 5432
```

---

## 🔹 Step 5: Create a Test Database

Create a new database.

```sql
CREATE DATABASE testdb;
```

### ✅ Expected Output

```text
CREATE DATABASE
```

Verify creation:

```sql
\l
```

### ✅ Expected Result

```text
testdb
```

appears in the database list.

---

## 🔹 Step 6: Connect to the New Database

Switch to the newly created database.

```sql
\c testdb
```

### ✅ Expected Output

```text
You are now connected to database "testdb"
```

---

## 🔹 Step 7: Exit PostgreSQL

Exit PostgreSQL shell.

```sql
\q
```

Return to normal Linux user.

```bash
exit
```

---

# 🛠️ Task 3: Create a Custom Database User

---

## 🔹 Step 1: Create New User

Run:

```bash
sudo -u postgres createuser --interactive
```

### Enter

```text
Role name: labuser
Superuser: n
```

### ✅ Expected Result

```text
Role created
```

---

## 🔹 Step 2: Set User Password

Open PostgreSQL shell.

```bash
sudo -u postgres psql
```

Set password:

```sql
ALTER USER labuser WITH PASSWORD 'securepassword123';
```

### ✅ Expected Output

```text
ALTER ROLE
```

---

## 🔹 Step 3: Grant Database Permissions

Allow user access to test database.

```sql
GRANT ALL PRIVILEGES ON DATABASE testdb TO labuser;
```

### ✅ Expected Output

```text
GRANT
```

Exit:

```sql
\q
```

---

## 🔹 Step 4: Configure Password Authentication

Edit authentication configuration.

```bash
sudo nano /etc/postgresql/*/main/pg_hba.conf
```

Locate:

```text
local   all   all   peer
```

Replace with:

```text
local   all   all   md5
```

### 📌 What This Does

Enables password-based authentication.

---

## 🔹 Step 5: Restart PostgreSQL

Apply configuration changes.

```bash
sudo systemctl restart postgresql
```

### ✅ Expected Result

```text
Service restarted successfully
```

---

## 🔹 Step 6: Test User Connection

Connect using new credentials.

```bash
psql -U labuser -d testdb -h localhost
```

Enter password:

```text
securepassword123
```

### ✅ Expected Output

```text
testdb=>
```

List databases:

```sql
\l
```

Exit:

```sql
\q
```

---

# 🔍 Verification Checklist

---

## ✅ Verify PostgreSQL Version

```bash
psql --version
```

---

## ✅ Verify Service Status

```bash
sudo systemctl status postgresql
```

---

## ✅ Verify PostgreSQL Connection

```bash
sudo -u postgres psql -c "\conninfo"
```

---

## ✅ Verify Database Exists

```bash
sudo -u postgres psql -c "\l" | grep testdb
```

---

## ✅ Verify Custom User Access

```bash
psql -U labuser -d testdb -h localhost -c "\conninfo"
```

---

# 📊 Expected Results

You should successfully see:

✅ PostgreSQL version information

✅ PostgreSQL service running

✅ Successful postgres user connection

✅ Successful custom user connection

✅ testdb database available

✅ Authentication working correctly

---

# 🚨 Troubleshooting Guide

---

## ❌ Error: psql command not found

### Solution

```bash
sudo apt install postgresql-client
```

---

## ❌ Error: Connection Refused

### Solution

Start PostgreSQL:

```bash
sudo systemctl start postgresql
```

Verify:

```bash
sudo systemctl status postgresql
```

---

## ❌ Error: Authentication Failed

### Solution Checklist

✔ Verify username

✔ Verify password

✔ Verify pg_hba.conf uses md5

✔ Restart PostgreSQL

```bash
sudo systemctl restart postgresql
```

---

## ❌ Error: Permission Denied

### Solution

Use sudo:

```bash
sudo command
```

or switch to postgres user:

```bash
sudo -i -u postgres
```

---

# 🎓 Key PostgreSQL Commands Cheat Sheet

| Command | Purpose |
|-----------|---------|
| psql | Open PostgreSQL CLI |
| \l | List Databases |
| \c database | Connect Database |
| \conninfo | Connection Info |
| \du | List Users |
| \dt | List Tables |
| \q | Exit psql |

---

# 🏆 Lab Completion Summary

Congratulations! 🎉

You have successfully:

✅ Installed PostgreSQL Server

✅ Installed PostgreSQL Client Tools

✅ Verified PostgreSQL Service

✅ Connected using psql

✅ Created a Database

✅ Created a Database User

✅ Configured Password Authentication

✅ Granted Database Permissions

✅ Tested User Connectivity

✅ Verified Successful Database Operations

---

# 🌟 Why PostgreSQL Matters

PostgreSQL is one of the most powerful and widely used open-source relational database systems in the world.

Organizations using PostgreSQL include:

🏢 Enterprise Applications

☁️ Cloud Platforms

📊 Data Analytics Systems

🛒 E-Commerce Platforms

🚀 DevOps & CI/CD Workflows

📱 Modern Web Applications

Mastering PostgreSQL is an essential skill for:

- Database Administrators (DBA)
- Backend Developers
- DevOps Engineers
- Cloud Engineers
- Data Engineers
- Software Architects

---

# 🚀 Next Steps

In future PostgreSQL labs, you will learn:

🔹 Creating Tables

🔹 Inserting Data

🔹 SQL Queries

🔹 Database Backups

🔹 Indexing & Optimization

🔹 User Management

🔹 Replication

🔹 High Availability

🔹 PostgreSQL Security Best Practices

---

<div align="center">

### 🐘 PostgreSQL Installation & Connectivity Mastered

⭐ Happy Learning & Keep Building Amazing Database Solutions! ⭐

</div>
