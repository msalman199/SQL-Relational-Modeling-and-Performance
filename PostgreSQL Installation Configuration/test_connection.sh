#!/bin/bash

# TODO: Complete this script to test database connectivity
# Requirements:
# 1. Test connection to testdb as app_user
# 2. Execute a simple query (SELECT version();)
# 3. Display connection success/failure message
# 4. Exit with appropriate status code

DB_HOST="localhost"
DB_NAME="testdb"
DB_USER="app_user"
DB_PASS="AppUserPass456!"

# TODO: Use PGPASSWORD environment variable and psql command
# Hint: PGPASSWORD=$DB_PASS psql -h $DB_HOST -U $DB_USER -d $DB_NAME -c "YOUR_QUERY"

echo "Testing database connectivity..."

# TODO: Implement connection test

# TODO: Check exit status and display appropriate message
