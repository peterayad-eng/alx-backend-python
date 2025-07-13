import mysql.connector
from mysql.connector import Error

class ExecuteQuery:
    def __init__(self, host, user, password, database, query, params=()):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor(dictionary=True)
            self.cursor.execute(self.query, self.params)
            self.results = self.cursor.fetchall()
            return self.results
        except Error as e:
            print(f"Database error: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

query = "SELECT * FROM users WHERE age > %s"
params = (25,)

with ExecuteQuery(
    host='localhost',
    user='db_user',
    password='',
    database='db',
    query=query,
    params=params
) as results:
    for row in results:
        print(row)

