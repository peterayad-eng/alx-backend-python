import sqlite3
import functools
from datetime import datetime

#### decorator to lof SQL queries

def log_queries(func):
    def wrapper(*args,**kwargs):
        if args:
            query = args[0]
        else:
            query = kwargs.get('query')

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if query:
            print(f"[{timestamp}]INFO: Executing SQL query: {query}")
        else:
            print(f"[{timestamp}] WARNING: No SQL query detected in function call")

        return func(*args,**kwargs)

    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")

