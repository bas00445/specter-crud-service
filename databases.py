import psycopg2
from config import CRUD_DATABASE_URI, COMPONENT_DATABASE_URI, RECOMMEND_DATABASE_URI
'''
        self.conn = crud_database_connection
        self.cursor = self.conn.cursor()
def connect_db():
    crud_database_connection = psycopg2.connect(CRUD_DATABASE_URI)
    component_database_connection = psycopg2.connect(COMPONENT_DATABASE_URI)
    recommend_database_connection = psycopg2.connect(RECOMMEND_DATABASE_URI)

    return crud_database_connection, component_database_connection, recommend_database_connection

def disconnect_db(conn1, conn2, conn3):
'''

