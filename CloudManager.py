import psycopg2
import logging

logging.basicConfig(
    format="%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s",
    level=logging.INFO,
    filename="consumer.log",
)

class CloudManager:
    def __init__(self, endpoint, port, user, password, dbname, ssl_certificate):#specify stuff):
        self.endpoint = endpoint
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        self.ssl_certificate = ssl_certificate


    def create_connection(self):
        try:
            connection = psycopg2.connect(
                endpoint = self.endpoint,
                port = self.port,
                dbname=self.dbname,
                user=self.user,
                password= self.password,
                ssl_certificate = self.ssl_certificate
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