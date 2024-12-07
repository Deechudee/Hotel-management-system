import mysql.connector
import hashlib

def get_connection():
    """Returns a connection to the MySQL database."""
    connection = mysql.connector.connect(
        host="localhost",  # your MySQL server address
        user="root",       # your MySQL username
        password="deeChu@2004",  # your MySQL password
        database="hotel_db"  # the database you want to connect to
    )
    return connection

# Function to check if the email exists
def check_email_exists(email):
    db_connection = get_connection()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    db_connection.close()
    return user

# Function to update the password
def update_password(email, new_password):
    hashed_password = hashlib.sha256(new_password.encode()).hexdigest()  # Hash the password
    db_connection = get_connection()
    cursor = db_connection.cursor()
    cursor.execute("UPDATE users SET password = %s WHERE email = %s", (hashed_password, email))
    db_connection.commit()
    cursor.close()
    db_connection.close()
