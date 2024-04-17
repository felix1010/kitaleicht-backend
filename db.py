
import psycopg2
import mysql.connector
from mysql.connector import Error

# connect to postgre
def connect_to_postgres():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="admin",
            host="localhost",
            port="5432",
            database="kitaleicht"
        )
        return connection
    except Exception as e:
        print("Error connecting to PostgreSQL database:", e)


def connect_to_mysql():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="kitaleicht",
            user="root",
            password="root"
        )
        if connection.is_connected():
            print("连接到 MySQL 数据库成功")
    except Error as e:
        print(f"连接到 MySQL 数据库时发生错误: {e}")
    
    return connection

def close_mysql_connection(connection):
    if connection:
        connection.close()
        print("MySQL 连接已关闭")


