# 🐘 PostgreSQL Installation & Configuration 

<div align="center">

# 🚀 PostgreSQL Installation & Configuration

### 📚 Complete Hands-On PostgreSQL Administration 

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)
![Linux](https://img.shields.io/badge/Linux-Ubuntu%20%7C%20CentOS-orange?style=for-the-badge&logo=linux)
![SQL](https://img.shields.io/badge/SQL-Database-success?style=for-the-badge&logo=postgresql)
![Security](https://img.shields.io/badge/Security-Authentication-red?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Lab-purple?style=for-the-badge)

### 🎯 Learn PostgreSQL Installation, User Management, Authentication & Connectivity

</div>

---

# 📖 Overview

This lab provides hands-on experience installing and configuring PostgreSQL on Linux. You will learn how to install PostgreSQL, create users and roles, configure authentication methods, manage permissions, and test database connectivity using both command-line and Python.

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

✅ Install PostgreSQL on Linux

✅ Configure PostgreSQL for production environments

✅ Create and manage database users and roles

✅ Configure authentication using pg_hba.conf

✅ Configure PostgreSQL networking and logging

✅ Implement role-based access control (RBAC)

✅ Test connectivity using CLI and Python

✅ Verify permissions and authentication settings

---

# 📋 Prerequisites

| Requirement | Description |
|------------|-------------|
| 🐧 Linux Basics | Basic Linux command-line knowledge |
| 🗄️ Database Concepts | Understanding of tables, users and permissions |
| 📝 Text Editor | Familiarity with nano or vi |
| 🔐 Administrative Access | Root or sudo privileges |

---

# 🖥️ Environment Requirements

| Component | Requirement |
|------------|-------------|
| Operating System | Ubuntu 20.04+ / CentOS 8+ |
| Memory | Minimum 2GB RAM |
| Storage | Minimum 10GB Free Space |
| Network | Internet Connectivity |
| Database | PostgreSQL |

---

# 🏗️ PostgreSQL Architecture Overview

```text
┌───────────────────────┐
│ Client Applications   │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ PostgreSQL Server     │
├───────────────────────┤
│ Authentication Layer  │
│ Role Management       │
│ Database Engine       │
│ Query Processor       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Databases & Tables    │
└───────────────────────┘
```

---

# 🛠️ Task 1: Install PostgreSQL

---

## 🔹 Step 1.1: Update System Packages

### Ubuntu / Debian

```bash
sudo apt update && sudo apt upgrade -y
```

### CentOS / RHEL

```bash
sudo dnf update -y
```

### ✅ Expected Result

```text
System packages updated successfully
```

---

## 🔹 Step 1.2: Install PostgreSQL

### Ubuntu / Debian

```bash
sudo apt install postgresql postgresql-contrib -y
```

### CentOS / RHEL

```bash
sudo dnf install postgresql-server postgresql-contrib -y

sudo postgresql-setup --initdb
```

### 📌 Installed Components

| Package | Purpose |
|----------|---------|
| postgresql | Database Server |
| postgresql-contrib | Additional Extensions |
| psql | Database Client |

---

## 🔹 Step 1.3: Start and Enable PostgreSQL

Start service:

```bash
sudo systemctl start postgresql
```

Enable on boot:

```bash
sudo systemctl enable postgresql
```

Verify status:

```bash
sudo systemctl status postgresql
```

### ✅ Expected Output

```text
active (running)
```

---

## 🔹 Step 1.4: Verify Installation

Check version:

```bash
psql --version
```

Example:

```text
psql (PostgreSQL) 14.x
```

Verify listening port:

```bash
sudo ss -tunelp | grep 5432
```

### 📌 Default Port

```text
5432
```

---

# 👥 Task 2: Configure Users and Roles

---

## 🔹 Step 2.1: Access PostgreSQL

Switch to postgres user.

```bash
sudo -i -u postgres
```

Launch PostgreSQL shell.

```bash
psql
```

### ✅ Expected Prompt

```text
postgres=#
```

---

## 🔹 Step 2.2: Create Roles

Create administrator role.

```sql
CREATE ROLE db_admin
WITH LOGIN PASSWORD 'SecureAdminPass123!';
```

Grant administrative privileges.

```sql
ALTER ROLE db_admin
WITH SUPERUSER CREATEDB CREATEROLE;
```

---

Create application user.

```sql
CREATE ROLE app_user
WITH LOGIN PASSWORD 'AppUserPass456!';
```

---

Create read-only user.

```sql
CREATE ROLE readonly_user
WITH LOGIN PASSWORD 'ReadOnlyPass789!';
```

---

Verify roles.

```sql
\du
```

### ✅ Expected Roles

```text
db_admin
app_user
readonly_user
```

---

## 🔹 Step 2.3: Create Database

Create test database.

```sql
CREATE DATABASE testdb OWNER app_user;
```

Connect to database.

```sql
\c testdb
```

---

## 🔹 Create Products Table

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔹 Grant Permissions

Grant application user privileges.

```sql
GRANT ALL PRIVILEGES ON DATABASE testdb TO app_user;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_user;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app_user;
```

---

Grant read-only access.

```sql
GRANT CONNECT ON DATABASE testdb TO readonly_user;

GRANT USAGE ON SCHEMA public TO readonly_user;

GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_user;
```

Exit PostgreSQL.

```sql
\q
```

Exit postgres account.

```bash
exit
```

---

# 🔐 Task 3: Configure Authentication

---

## 🔹 Step 3.1: Locate Configuration Files

Find configuration file.

```bash
sudo -u postgres psql -c "SHOW config_file;"
```

### Common Locations

#### Ubuntu / Debian

```text
/etc/postgresql/[version]/main/
```

#### CentOS / RHEL

```text
/var/lib/pgsql/data/
```

---

## 🔹 Step 3.2: Configure pg_hba.conf

Create backup.

```bash
sudo cp /etc/postgresql/*/main/pg_hba.conf \
/etc/postgresql/*/main/pg_hba.conf.backup
```

Edit file.

```bash
sudo nano /etc/postgresql/*/main/pg_hba.conf
```

---

### Add Authentication Rules

```ini
# TYPE  DATABASE  USER  ADDRESS  METHOD

local   all   all                     md5

host    all   all   127.0.0.1/32      md5

host    all   all   ::1/128           md5

host    testdb  app_user      192.168.1.0/24   md5

host    testdb  readonly_user 192.168.1.0/24   md5
```

---

# 📚 Authentication Methods

| Method | Description |
|----------|-------------|
| md5 | Encrypted password authentication |
| peer | Uses Linux username |
| trust | No password required |
| scram-sha-256 | Modern secure authentication |

---

## 🔹 Step 3.3: Configure postgresql.conf

Edit configuration.

```bash
sudo nano /etc/postgresql/*/main/postgresql.conf
```

Update settings.

```ini
listen_addresses = 'localhost'

max_connections = 100

shared_buffers = 256MB

logging_collector = on

log_directory = 'log'

log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'

log_statement = 'all'
```

---

# 📌 Configuration Explanation

| Parameter | Purpose |
|------------|----------|
| listen_addresses | Network interfaces |
| max_connections | Maximum clients |
| shared_buffers | Memory allocation |
| logging_collector | Enable logging |
| log_statement | Log SQL statements |

---

## 🔹 Step 3.4: Restart PostgreSQL

Apply changes.

```bash
sudo systemctl restart postgresql
```

Verify status.

```bash
sudo systemctl status postgresql
```

### ✅ Expected Result

```text
active (running)
```

---

# 🌐 Task 4: Test Connectivity

---

## 🔹 Step 4.1: Test app_user Connection

Connect using password authentication.

```bash
psql -U app_user -d testdb -h localhost
```

Password:

```text
AppUserPass456!
```

---

Insert sample data.

```sql
INSERT INTO products (name, price)
VALUES ('Laptop', 999.99);

INSERT INTO products (name, price)
VALUES ('Mouse', 29.99);
```

View data.

```sql
SELECT * FROM products;
```

Exit.

```sql
\q
```

---

## 🔹 Step 4.2: Test Read-Only User

Connect.

```bash
psql -U readonly_user -d testdb -h localhost
```

Password:

```text
ReadOnlyPass789!
```

---

Read operation.

```sql
SELECT * FROM products;
```

### ✅ Expected Result

Query succeeds.

---

Write operation.

```sql
INSERT INTO products (name, price)
VALUES ('Keyboard', 79.99);
```

### ❌ Expected Result

```text
Permission denied
```

Exit.

```sql
\q
```

---

## 🔹 Step 4.3: Create Bash Connection Test Script

Create file.

```bash
nano test_connection.sh
```

Add:

```bash
#!/bin/bash

DB_HOST="localhost"
DB_NAME="testdb"
DB_USER="app_user"
DB_PASS="AppUserPass456!"

echo "Testing database connectivity..."

PGPASSWORD=$DB_PASS \
psql \
-h $DB_HOST \
-U $DB_USER \
-d $DB_NAME \
-c "SELECT version();" >/dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✅ Connection Successful"
    exit 0
else
    echo "❌ Connection Failed"
    exit 1
fi
```

---

Make executable.

```bash
chmod +x test_connection.sh
```

Run.

```bash
./test_connection.sh
```

### ✅ Expected Output

```text
Connection Successful
```

---

## 🔹 Step 4.4: Test Using Python

Install dependencies.

```bash
sudo apt install python3-pip -y

pip3 install psycopg2-binary
```

---

Create Python script.

```python
import psycopg2

def test_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="testdb",
            user="app_user",
            password="AppUserPass456!"
        )

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products;")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        conn.close()

        print("Connection successful!")

    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_connection()
```

Run script.

```bash
python3 test_db.py
```

---

# ✅ Verification Checklist

---

## Verify Service Status

```bash
sudo systemctl is-active postgresql
```

Expected:

```text
active
```

---

## Verify Roles

```bash
sudo -u postgres psql -c "\du"
```

Expected roles:

```text
db_admin
app_user
readonly_user
```

---

## Verify Database

```bash
sudo -u postgres psql -c "\l" | grep testdb
```

Expected:

```text
testdb
```

---

## Verify Authentication

```bash
psql -U app_user \
-d testdb \
-h localhost \
-c "SELECT current_user;"
```

Expected:

```text
app_user
```

---

## Verify Permissions

Application user:

```bash
psql -U app_user \
-d testdb \
-h localhost \
-c "SELECT COUNT(*) FROM products;"
```

Read-only user:

```bash
psql -U readonly_user \
-d testdb \
-h localhost \
-c "SELECT COUNT(*) FROM products;"
```

---

# 🚨 Troubleshooting Guide

---

## ❌ Cannot Connect

### Check Service

```bash
sudo systemctl status postgresql
```

### Check Listening Port

```bash
sudo ss -tunelp | grep 5432
```

### Check Authentication Rules

```bash
sudo nano pg_hba.conf
```

---

## ❌ Password Authentication Failed

Verify roles.

```bash
sudo -u postgres psql -c "\du"
```

Verify md5 configuration.

```ini
host all all 127.0.0.1/32 md5
```

Restart PostgreSQL.

```bash
sudo systemctl restart postgresql
```

---

## ❌ Permission Denied

Check roles.

```sql
\du
```

Check database ownership.

```sql
\l
```

Grant permissions.

```sql
GRANT ALL PRIVILEGES ...
```

---

## ❌ Cannot Locate Configuration Files

Find configuration file.

```bash
sudo -u postgres psql -c "SHOW config_file;"
```

---

# 📚 PostgreSQL Administration Cheat Sheet

| Command | Purpose |
|----------|---------|
| psql | PostgreSQL CLI |
| \du | List Roles |
| \l | List Databases |
| \c dbname | Connect Database |
| \dt | List Tables |
| systemctl status postgresql | Service Status |
| SHOW config_file; | Config Location |
| GRANT | Assign Permissions |
| ALTER ROLE | Modify Role |
| CREATE DATABASE | Create Database |

---

# 🏆 Lab Completion Summary

Congratulations! 🎉

You have successfully:

✅ Installed PostgreSQL

✅ Started and Enabled Service

✅ Created Database Roles

✅ Created Databases

✅ Assigned Permissions

✅ Configured Authentication

✅ Configured Network Access

✅ Configured Logging

✅ Tested Connectivity

✅ Implemented Role-Based Access Control

---

# 🌟 Key Takeaways

🔐 PostgreSQL uses role-based security.

📄 pg_hba.conf controls authentication.

🛡️ Different authentication methods provide different security levels.

👥 User roles should follow least-privilege principles.

⚙️ Configuration changes require service restart.

📊 Logging is critical for troubleshooting and monitoring.

---

# 🚀 Next Steps

Continue learning:

🔹 PostgreSQL Backups & Recovery

🔹 Replication & High Availability

🔹 Query Optimization

🔹 Database Monitoring

🔹 SSL/TLS Encryption

🔹 PostgreSQL Extensions

🔹 Performance Tuning

🔹 Disaster Recovery

🔹 Advanced Security Controls

---

<div align="center">

# 🎯 Successfully Completed

## 🐘 PostgreSQL Installation & Configuration Mastered

### ⭐ Build Secure, Scalable & Production-Ready Databases! ⭐

</div>
