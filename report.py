import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="payroll"
)

cursor = conn.cursor()


def employee_report():

    cursor.execute("""
    SELECT emp_id, emp_name, gender, dept_id
    FROM employee
    """)

    rows = cursor.fetchall()

    print("\n===== EMPLOYEE REPORT =====")

    for row in rows:
        print(row)


def attendance_report():

    cursor.execute("""
    SELECT attendance_id, emp_id, month, working_days, present_days
    FROM attendance
    """)

    rows = cursor.fetchall()

    print("\n===== ATTENDANCE REPORT =====")

    for row in rows:
        print(row)


def payroll_report():

    cursor.execute("""
    SELECT payroll_id, emp_id, basic_salary, bonus, net_salary
    FROM payroll
    """)

    rows = cursor.fetchall()

    print("\n===== PAYROLL REPORT =====")

    for row in rows:
        print(row)


while True:

    print("\n==========================")
    print("        REPORTS")
    print("==========================")
    print("1. Employee Report")
    print("2. Attendance Report")
    print("3. Payroll Report")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        employee_report()

    elif choice == "2":
        attendance_report()

    elif choice == "3":
        payroll_report()

    elif choice == "4":
        print("Exiting Reports...")
        break

    else:
        print("Invalid Choice")