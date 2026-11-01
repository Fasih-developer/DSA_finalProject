
import mysql.connector


def get_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MUHAMMAD1122",
        database="surplus_connect"
    )

    return connection


# Test database connection

try:

    connection = get_connection()

    if connection.is_connected():
        print("Database connected successfully!")

    connection.close()

except mysql.connector.Error as error:

    print("Database connection failed:", error)

import mysql.connector

from database import get_connection

try:

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM food_donations")

    donations = cursor.fetchall()

    for donation in donations:
        print(donation)

    cursor.close()
    connection.close()

except mysql.connector.Error as error:

    print("Error:", error)