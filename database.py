import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="payroll"
    )

    cursor = conn.cursor()

    print("Database Connected Successfully!")

except Exception as e:
    print("Error:", e)