import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='deeChu@2004',database='hotel_dbms')
my_cursor=conn.cursor()
conn.commit()
conn.close()
print("MySQL Connector is installed and working!")