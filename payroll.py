import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="payroll"
)

cursor = conn.cursor()


def generate_payroll():

    payroll_id = int(input("Payroll ID: "))
    emp_id = int(input("Employee ID: "))
    basic_salary = float(input("Basic Salary: "))
    bonus = float(input("Bonus: "))

    cursor.execute(
        "SELECT working_days, present_days FROM attendance WHERE emp_id=%s",
        (emp_id,)
    )

    attendance = cursor.fetchone()

    if attendance is None:
        print("Attendance record not found")
        return

    working_days = attendance[0]
    present_days = attendance[1]

    per_day_salary = basic_salary / working_days

    net_salary = (per_day_salary * present_days) + bonus

    query = """
    INSERT INTO payroll
    (payroll_id, emp_id, basic_salary, bonus, net_salary)
    VALUES (%s,%s,%s,%s,%s)
    """

    values = (
        payroll_id,
        emp_id,
        basic_salary,
        bonus,
        net_salary
    )

    cursor.execute(query, values)

    conn.commit()

    print("Payroll Generated")
    print("Net Salary =", round(net_salary, 2))


def view_payroll():

    cursor.execute("SELECT * FROM payroll")

    rows = cursor.fetchall()

    for row in rows:
        print("-" * 50)
        print(f"Payroll ID   : {row[0]}")
        print(f"Employee ID  : {row[1]}")
        print(f"Basic Salary : Rs. {float(row[2]):,.2f}")
        print(f"Bonus        : Rs. {float(row[3]):,.2f}")
        print(f"Net Salary   : Rs. {float(row[4]):,.2f}")

while True:

    print("\nPAYROLL MANAGEMENT")

    print("1. Generate Payroll")
    print("2. View Payroll")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        generate_payroll()

    elif choice == "2":
        view_payroll()

    elif choice == "3":
        break