
import psycopg2

# 连接到 PostgreSQL 数据库
def connect_to_db():
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
