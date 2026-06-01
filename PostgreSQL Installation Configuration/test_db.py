import psycopg2

def test_connection():
    """
    Test PostgreSQL connection and execute a simple query.
    
    TODO: Complete the connection parameters
    TODO: Implement error handling
    TODO: Execute a test query and display results
    """
    try:
        # TODO: Complete connection parameters
        conn = psycopg2.connect(
            host="localhost",
            database="testdb",
            user="app_user",
            password="AppUserPass456!"
        )
        
        # TODO: Create cursor and execute query
        cursor = conn.cursor()
        
        # TODO: Execute SELECT query on products table
        
        # TODO: Fetch and print results
        
        # TODO: Close cursor and connection
        
        print("Connection successful!")
        
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_connection()
