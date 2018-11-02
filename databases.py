import psycopg2
from config import CRUD_DATABASE_URI, COMPONENT_DATABASE_URI, RECOMMEND_DATABASE_URI

crud_database_connection = psycopg2.connect(CRUD_DATABASE_URI)
component_database_connection = psycopg2.connect(COMPONENT_DATABASE_URI)
recommend_database_connection = psycopg2.connect(RECOMMEND_DATABASE_URI)
