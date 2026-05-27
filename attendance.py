import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="payroll"
)

cursor = conn.cursor()


def mark_attendance():

    attendance_id = int(input("Attendance ID: "))
    emp_id = int(input("Employee ID: "))
    month = input("Month: ")
    working_days = int(input("Working Days: "))
    present_days = int(input("Present Days: "))

    query = """
    INSERT INTO attendance
    (attendance_id, emp_id, month, working_days, present_days)
    VALUES (%s,%s,%s,%s,%s)
    """

    values = (
        attendance_id,
        emp_id,
        month,
        working_days,
        present_days
    )

    cursor.execute(query, values)

    conn.commit()

    print("Attendance Added Successfully")


def view_attendance():

    cursor.execute("SELECT * FROM attendance")

    rows = cursor.fetchall()

    for row in rows:
        print(row)


while True:

    print("\nATTENDANCE MANAGEMENT")

    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        mark_attendance()

    elif choice == "2":
        view_attendance()

    elif choice == "3":
        break