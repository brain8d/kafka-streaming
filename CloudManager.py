import psycopg2
import logging

logging.basicConfig(
    format="%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s",
    level=logging.INFO,
    filename="consumer.log",
)

class CloudManager:
    def __init__(self, host, port, user, password, dbname):#specify stuff):
        self.endpoint = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname

    def create_connection(self):
        try:
            connection = psycopg2.connect(
                host = self.endpoint,
                port = self.port,
                dbname=self.dbname,
                user=self.user,
                password= self.password,
            )
            logging.info("Connection to database succesfully")
            return connection
        except Exception as e:
            logging.error("Failed to connect to the database", e)

# TODO check this function
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


    def create_table(self):
        # create schema
        pass 

    def insert_data(self):
        pass