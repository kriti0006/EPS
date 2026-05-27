while True:

    print("\n================================")
    print("    EMPLOYEE PAYROLL SYSTEM")
    print("================================")

    print("1. Employee Management")
    print("2. Attendance Management")
    print("3. Payroll Management")
    print("4. Reports")
    print("5. Analytics")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        exec(open("employee.py").read())

    elif choice == "2":
        exec(open("attendance.py").read())

    elif choice == "3":
        exec(open("payroll.py").read())

    elif choice == "4":
        exec(open("report.py").read())

    elif choice == "5":
        exec(open("analytics.py").read())

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")