import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="db-mysql",
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


