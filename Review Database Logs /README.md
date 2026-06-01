# 📋 PostgreSQL Database Log Analysis 

<div align="center">

# 🔍 Review Database Logs

### 📚 Learn PostgreSQL Log Analysis, Error Detection & Performance Troubleshooting

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=linux)
![Shell](https://img.shields.io/badge/Bash-Scripting-black?style=for-the-badge&logo=gnubash)
![Monitoring](https://img.shields.io/badge/Monitoring-Logs-success?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Lab-red?style=for-the-badge)

### 🎯 Master PostgreSQL Logging, Error Analysis & Slow Query Detection

</div>

---

# 📖 Overview

Database logs are one of the most valuable resources for troubleshooting, monitoring, and performance optimization. In this lab, you will learn how to configure PostgreSQL logging, locate log files, analyze database activity, identify slow queries, detect errors, and generate automated reports.

---

# 🎯 Learning Objectives

By the end of this lab, you will be able to:

✅ Locate PostgreSQL log files

✅ Configure PostgreSQL logging settings

✅ Identify query execution logs

✅ Detect slow-performing SQL queries

✅ Find and categorize database errors

✅ Create automated log analysis scripts

✅ Generate troubleshooting reports

✅ Understand PostgreSQL logging best practices

---

# 📋 Prerequisites

| Requirement | Description |
|------------|-------------|
| 🐧 Linux Fundamentals | Basic Linux command-line knowledge |
| 🗄️ Database Knowledge | Understanding of databases |
| 📝 Text Editor Skills | Familiarity with nano or vim |
| 🐘 PostgreSQL Basics | Basic understanding of PostgreSQL |

---

# 🖥️ Environment Information

| Component | Value |
|------------|---------|
| Database | PostgreSQL |
| OS | Ubuntu / Debian Linux |
| Log Location | PostgreSQL Log Directory |
| Shell | Bash |
| Estimated Duration | 60 Minutes |

---

# 🏗️ PostgreSQL Logging Architecture

```text
┌────────────────────┐
│ Application Query  │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ PostgreSQL Server  │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ Logging Collector  │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ PostgreSQL Logs    │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ Analysis Scripts   │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ Reports & Alerts   │
└────────────────────┘
```

---

# 🛠️ Environment Setup

---

# 🔹 Step 1: Install PostgreSQL

Update package repository.

```bash
sudo apt update
```

Install PostgreSQL packages.

```bash
sudo apt install postgresql postgresql-contrib -y
```

Start PostgreSQL service.

```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

Verify service status.

```bash
sudo systemctl status postgresql
```

### ✅ Expected Output

```text
active (running)
```

---

# 🔹 Step 2: Enable Detailed Logging

Switch to PostgreSQL administrative account.

```bash
sudo -i -u postgres
```

Open PostgreSQL configuration.

```bash
nano /etc/postgresql/*/main/postgresql.conf
```

---

## 🔧 Configure Logging Parameters

Locate and update the following settings:

```ini
logging_collector = on
log_directory = 'log'
log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'
log_statement = 'all'
log_duration = on
log_min_duration_statement = 100
log_line_prefix = '%t [%p]: [%l-1] user=%u,db=%d '
```

---

## 📌 What Each Setting Does

| Parameter | Purpose |
|------------|---------|
| logging_collector | Enables log collection |
| log_directory | Log storage location |
| log_filename | Log file naming format |
| log_statement | Logs all SQL statements |
| log_duration | Records execution times |
| log_min_duration_statement | Logs slow queries |
| log_line_prefix | Adds useful metadata |

---

Save the file:

```text
Ctrl + O
Enter
Ctrl + X
```

Exit postgres account:

```bash
exit
```

Restart PostgreSQL.

```bash
sudo systemctl restart postgresql
```

---

# 🔹 Step 3: Generate Sample Database Activity

Switch to postgres user.

```bash
sudo -i -u postgres
```

Create database.

```bash
createdb testdb
```

Connect to PostgreSQL.

```bash
psql testdb
```

---

# 🛠️ Create Sample Table

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary NUMERIC
);
```

---

# 🛠️ Insert Sample Data

```sql
INSERT INTO employees (name, department, salary) VALUES
('Alice Johnson', 'Engineering', 75000),
('Bob Smith', 'Marketing', 65000),
('Carol White', 'Engineering', 80000),
('David Brown', 'Sales', 70000);
```

---

# ⚡ Generate Query Activity

Fast query:

```sql
SELECT * FROM employees WHERE id = 1;
```

---

Slow query:

```sql
SELECT pg_sleep(0.5), * FROM employees;
```

---

Error query:

```sql
SELECT * FROM nonexistent_table;
```

---

Complex query:

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

---

Exit PostgreSQL.

```sql
\q
```

Exit postgres account.

```bash
exit
```

---

# 🎯 Task 1: Locate and Access Log Files

---

# 🔹 Step 1: Find PostgreSQL Data Directory

```bash
sudo -u postgres psql -c "SHOW data_directory;"
```

### ✅ Expected Output

```text
/var/lib/postgresql/XX/main
```

---

# 🔹 Step 2: Locate Log Files

```bash
sudo ls -lh /var/lib/postgresql/*/main/log/
```

---

View newest logs.

```bash
sudo ls -lht /var/lib/postgresql/*/main/log/
```

---

Follow live logs.

```bash
sudo tail -f /var/lib/postgresql/*/main/log/postgresql-*.log
```

Stop monitoring:

```text
Ctrl + C
```

---

# 🔹 Step 3: Create Working Copy

Copy log file locally.

```bash
sudo cp /var/lib/postgresql/*/main/log/postgresql-*.log ~/db_log.txt
```

Update ownership.

```bash
sudo chown $USER:$USER ~/db_log.txt
```

View log.

```bash
cat ~/db_log.txt
```

---

# 🎯 Task 2: Analyze Query Logs

---

# 🔹 Step 1: Search Query Activity

Find SELECT statements.

```bash
grep "SELECT" ~/db_log.txt
```

---

Find INSERT statements.

```bash
grep "INSERT" ~/db_log.txt
```

---

Show all SQL statements.

```bash
grep -i "statement:" ~/db_log.txt
```

---

# 🔹 Step 2: Identify Slow Queries

Display duration logs.

```bash
grep "duration:" ~/db_log.txt
```

---

Show duration with query context.

```bash
grep -A 1 "duration:" ~/db_log.txt
```

---

# 🛠️ Create Slow Query Analysis Script

```bash
nano analyze_slow_queries.sh
```

Add:

```bash
#!/bin/bash

LOG_FILE="$HOME/db_log.txt"
THRESHOLD=100

echo "=== Slow Query Analysis ==="
echo "Threshold: ${THRESHOLD}ms"
echo ""

grep "duration:" "$LOG_FILE" | while read line; do
    duration=$(echo "$line" | grep -oP 'duration: \K[0-9.]+')

    if (( $(echo "$duration > $THRESHOLD" | bc -l) )); then
        echo "Duration: ${duration}ms"
        echo "$line"
        echo "---"
    fi
done
```

---

Make executable.

```bash
chmod +x analyze_slow_queries.sh
```

Run script.

```bash
./analyze_slow_queries.sh
```

---

# 🔹 Step 3: Examine Query Patterns

```bash
echo "=== Query Type Summary ==="
echo "SELECT queries: $(grep -c "SELECT" ~/db_log.txt)"
echo "INSERT queries: $(grep -c "INSERT" ~/db_log.txt)"
echo "UPDATE queries: $(grep -c "UPDATE" ~/db_log.txt)"
echo "DELETE queries: $(grep -c "DELETE" ~/db_log.txt)"
```

---

# 🎯 Task 3: Detect and Review Errors

---

# 🔹 Step 1: Search Error Messages

Find errors.

```bash
grep "ERROR:" ~/db_log.txt
```

---

Find warnings.

```bash
grep "WARNING:" ~/db_log.txt
```

---

Find fatal errors.

```bash
grep "FATAL:" ~/db_log.txt
```

---

# 🔹 Step 2: Create Error Summary Script

```bash
nano error_summary.sh
```

Add:

```bash
#!/bin/bash

LOG_FILE="$HOME/db_log.txt"

echo "=== Database Error Summary ==="

echo "Total Errors: $(grep -c "ERROR:" "$LOG_FILE")"
echo "Total Warnings: $(grep -c "WARNING:" "$LOG_FILE")"

echo ""
echo "=== Common Error Types ==="

grep "ERROR:" "$LOG_FILE" \
| cut -d':' -f4- \
| sort \
| uniq -c \
| sort -rn

echo ""
echo "=== Recent Errors ==="

grep "ERROR:" "$LOG_FILE" | tail -5
```

---

Make executable.

```bash
chmod +x error_summary.sh
```

Run.

```bash
./error_summary.sh
```

---

# 🔹 Step 3: Analyze Specific Errors

Connection issues.

```bash
grep -i "connection" ~/db_log.txt | grep -i "error"
```

---

Permission issues.

```bash
grep -i "permission denied" ~/db_log.txt
```

---

Syntax issues.

```bash
grep -i "syntax error" ~/db_log.txt
```

---

# 🎯 Task 4: Document Findings

---

# 🔹 Step 1: Create Log Analysis Report

```bash
nano log_analysis_report.txt
```

---

## 📋 Report Template

```text
=== PostgreSQL Log Analysis Report ===

Date:
Analyzed Log:
Analysis Period:

--- SUMMARY ---

Total Log Entries:
Total Queries Executed:
Total Errors Found:
Total Warnings Found:

--- SLOW QUERIES ---

Number of Slow Queries (>100ms):

Top 3 Slowest Queries:

1.
2.
3.

--- ERRORS DETECTED ---

Most Common Error Type:
Occurrences:

Critical Errors:

-

--- RECOMMENDATIONS ---

1.
2.
3.

--- NOTES ---

Additional observations
```

---

# 🔹 Step 2: Generate Automated Report

Create report generator.

```bash
nano generate_report.sh
```

Add:

```bash
#!/bin/bash

LOG_FILE="$HOME/db_log.txt"
REPORT_FILE="$HOME/log_analysis_report_$(date +%Y%m%d_%H%M%S).txt"

{
echo "=== PostgreSQL Log Analysis Report ==="
echo "Generated: $(date)"
echo ""

echo "--- SUMMARY ---"
echo "Total Lines: $(wc -l < "$LOG_FILE")"
echo "Total Queries: $(grep -c "statement:" "$LOG_FILE")"
echo "Total Errors: $(grep -c "ERROR:" "$LOG_FILE")"
echo "Total Warnings: $(grep -c "WARNING:" "$LOG_FILE")"

echo ""
echo "--- QUERY BREAKDOWN ---"

echo "SELECT: $(grep -c "SELECT" "$LOG_FILE")"
echo "INSERT: $(grep -c "INSERT" "$LOG_FILE")"
echo "UPDATE: $(grep -c "UPDATE" "$LOG_FILE")"
echo "DELETE: $(grep -c "DELETE" "$LOG_FILE")"

echo ""
echo "--- SLOW QUERIES ---"

grep "duration:" "$LOG_FILE" | head -5

echo ""
echo "--- RECENT ERRORS ---"

grep "ERROR:" "$LOG_FILE" | tail -5

echo ""
echo "--- RECOMMENDATIONS ---"

if [ $(grep -c "duration:" "$LOG_FILE") -gt 0 ]; then
echo "- Review slow queries"
fi

if [ $(grep -c "ERROR:" "$LOG_FILE") -gt 0 ]; then
echo "- Investigate database errors"
fi

echo "- Tune logging thresholds"

} > "$REPORT_FILE"

echo "Report generated: $REPORT_FILE"

cat "$REPORT_FILE"
```

---

Make executable.

```bash
chmod +x generate_report.sh
```

Run.

```bash
./generate_report.sh
```

---

# ✅ Verification

---

## Verify Log Access

```bash
test -r ~/db_log.txt \
&& echo "SUCCESS: Log file readable" \
|| echo "FAIL: Cannot read log file"
```

---

## Verify Analysis Scripts

```bash
ls -l analyze_slow_queries.sh
ls -l error_summary.sh
ls -l generate_report.sh
```

---

## Verify Generated Reports

```bash
ls -lh log_analysis_report_*.txt
```

---

# 📚 Knowledge Check

Answer these questions:

### ❓ Where are PostgreSQL logs stored?

```text
/var/lib/postgresql/<version>/main/log/
```

---

### ❓ Which parameter logs all SQL statements?

```ini
log_statement = 'all'
```

---

### ❓ How can slow queries be identified?

```text
Search for duration entries
```

Example:

```bash
grep "duration:" db_log.txt
```

---

### ❓ Difference Between ERROR and WARNING?

| Level | Meaning |
|---------|---------|
| ERROR | Operation failed |
| WARNING | Potential issue but operation continues |

---

# 🚨 Troubleshooting Guide

---

## ❌ Cannot Find Logs

### Solution

Verify logging enabled.

```ini
logging_collector = on
```

Check service.

```bash
sudo systemctl status postgresql
```

---

## ❌ Empty Log Files

### Solution

Generate activity after enabling logging.

Check:

```ini
log_statement = 'all'
```

---

## ❌ Permission Denied

### Solution

Use sudo or copy files locally.

```bash
sudo cp logfile ~/db_log.txt
```

---

## ❌ grep Returns Nothing

### Solution

Check log contains data.

```bash
wc -l ~/db_log.txt
```

---

# 📊 PostgreSQL Log Analysis Cheat Sheet

| Command | Purpose |
|----------|---------|
| tail -f | Monitor logs live |
| grep | Search logs |
| wc -l | Count lines |
| sort | Sort output |
| uniq | Remove duplicates |
| chmod +x | Make executable |
| cat | Display file |
| nano | Edit file |

---

# 🏆 Lab Completion Summary

Congratulations! 🎉

You have successfully:

✅ Installed PostgreSQL

✅ Enabled Detailed Logging

✅ Generated Database Activity

✅ Located Log Files

✅ Reviewed Query Logs

✅ Identified Slow Queries

✅ Detected Database Errors

✅ Created Analysis Scripts

✅ Generated Automated Reports

✅ Practiced Database Troubleshooting

---

# 🌟 Why Log Analysis Matters

Database logs are critical for:

🔍 Troubleshooting Issues

⚡ Performance Optimization

🛡️ Security Auditing

📊 Capacity Planning

🚨 Incident Investigation

☁️ DevOps Monitoring

🏢 Production Operations

A skilled Database Administrator or DevOps Engineer regularly reviews logs to keep systems healthy and reliable.

---

# 🚀 Next Steps

Continue learning:

🔹 PostgreSQL Performance Tuning

🔹 pgBadger Log Analysis

🔹 Database Monitoring Tools

🔹 Prometheus & Grafana

🔹 Query Optimization

🔹 PostgreSQL Security Auditing

🔹 Replication Monitoring

🔹 High Availability Systems

---

<div align="center">

# 🎯 Successfully Completed

## 🔍 PostgreSQL Log Analysis & Troubleshooting Mastered

### ⭐ Keep Monitoring, Optimizing & Scaling Your Databases! ⭐

</div>
