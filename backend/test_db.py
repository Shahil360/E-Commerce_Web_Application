import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1377",
        database="e_commerce"
    )
    print("Connected successfully!")
except Exception as e:
    print("Error:", e)
