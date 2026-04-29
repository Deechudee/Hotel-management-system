import os
import mysql.connector

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
my_cursor=conn.cursor()
conn.commit()
conn.close()
print("MySQL Connector is installed and working!")