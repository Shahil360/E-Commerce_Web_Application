import mysql.connector

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "1377"
DB_NAME = "e_commerce"

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = conn.cursor()

cursor.execute(f"CREATE DATABASE IF NOT EXISTS e_commerce")

conn.database = DB_NAME

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10,2),
    image VARCHAR(255),
    review_image VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    mobile VARCHAR(20),
    password VARCHAR(255),
    is_admin TINYINT(1)
)
""")

cursor.close()
conn.close()

def get_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

