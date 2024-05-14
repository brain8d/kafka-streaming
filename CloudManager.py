import psycopg2

def create_connection():
    try:
        connection = psycopg2.connect(
            host="delhaize-db",
            database="delhaize-db-instance-1-us-east.czkwus82o4b9.us-east-1.rds.amazonaws.com",
            user="delhaize_dba",
            password="jkhhaaejhea888lknslan)"
        )
        print("Connection successful")
        return connection
    except Exception as e:
        print("Failed to connect to the database")
        print(e)

def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    try:
        if params is None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)
        connection.commit()
        return cursor.fetchall()
    except Exception as e:
        print(f"Failed to execute query: {query}")
        print(e)