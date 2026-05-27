import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="payroll"
)

cursor = conn.cursor()


def total_employees():
    cursor.execute("SELECT COUNT(*) FROM employee")
    result = cursor.fetchone()
    print("\nTotal Employees =", result[0])


def highest_salary():
    cursor.execute("SELECT MAX(net_salary) FROM payroll")
    result = cursor.fetchone()
    print("\nHighest Salary =", result[0])


def lowest_salary():
    cursor.execute("SELECT MIN(net_salary) FROM payroll")
    result = cursor.fetchone()
    print("\nLowest Salary =", result[0])


def average_salary():
    cursor.execute("SELECT AVG(net_salary) FROM payroll")
    result = cursor.fetchone()
    print("\nAverage Salary =", round(result[0], 2))


while True:

    print("\n==========================")
    print("       ANALYTICS")
    print("==========================")
    print("1. Total Employees")
    print("2. Highest Salary")
    print("3. Lowest Salary")
    print("4. Average Salary")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        total_employees()

    elif choice == "2":
        highest_salary()

    elif choice == "3":
        lowest_salary()

    elif choice == "4":
        average_salary()

    elif choice == "5":
        break

    else:
        print("Invalid Choice")