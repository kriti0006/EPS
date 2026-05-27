import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="payroll"
)

cursor = conn.cursor()


def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    emp_name = input("Enter Name: ")
    gender = input("Enter Gender: ")
    dob = input("Enter DOB (YYYY-MM-DD): ")
    dept_id = int(input("Enter Department ID: "))

    query = """
    INSERT INTO employee
    (emp_id, emp_name, gender, dob, dept_id)
    VALUES (%s,%s,%s,%s,%s)
    """

    values = (emp_id, emp_name, gender, dob, dept_id)

    cursor.execute(query, values)

    conn.commit()

    print("Employee Added Successfully")


def view_employees():
    cursor.execute("SELECT * FROM employee")

    rows = cursor.fetchall()

    for row in rows:
        print("-" * 60)
        print(f"Employee ID : {row[0]}")
        print(f"Name        : {row[1]}")
        print(f"Gender      : {row[2]}")
        print(f"DOB         : {row[3]}")
        print(f"Department  : {row[4]}")
        print(f"User ID     : {row[5]}")
        


def search_employee():
    emp_id = int(input("Enter Employee ID: "))

    query = "SELECT * FROM employee WHERE emp_id=%s"

    cursor.execute(query, (emp_id,))

    result = cursor.fetchone()

    print(result)


def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))

    query = "DELETE FROM employee WHERE emp_id=%s"

    cursor.execute(query, (emp_id,))

    conn.commit()

    print("Employee Deleted")


while True:

    print("\nEMPLOYEE MANAGEMENT")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        break