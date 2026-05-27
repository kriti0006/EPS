# Employee Payroll Management System

## Overview

Employee Payroll Management System is a Python and MySQL based application developed to manage employee records, attendance, payroll generation, reports, and analytics.

The system allows users to store employee information, track attendance, generate payroll automatically, and view reports and statistics.

---

## Features

### Employee Management
- Add Employee
- View Employees
- Search Employee
- Delete Employee

### Attendance Management
- Mark Attendance
- View Attendance Records

### Payroll Management
- Generate Payroll
- View Payroll Records

### Reports
- Employee Report
- Attendance Report
- Payroll Report

### Analytics
- Total Employees
- Highest Salary
- Lowest Salary
- Average Salary

---

## Technologies Used

- Python
- MySQL
- XAMPP
- VS Code

---

## Database Tables

### Employee
- emp_id
- emp_name
- gender
- dob
- dept_id
- user_id

### Department
- dept_id
- dept_name
- location
- manager_name
- contact_no

### Attendance
- attendance_id
- emp_id
- month
- working_days
- present_days

### Payroll
- payroll_id
- emp_id
- basic_salary
- bonus
- net_salary

### Users
- user_id
- username
- password
- role
- contact_no

---

## Project Structure

```text
EPS/
├── analytics.py
├── attendance.py
├── database.py
├── employee.py
├── payroll.py
├── report.py
├── main.py
├── README.md
├── employee_payroll_system.sql
├── ER_diagram.jpg
└── screenshots/
```

---

## How to Run

### 1. Start XAMPP

Start:
- Apache
- MySQL

### 2. Import Database

Open phpMyAdmin and import:

```text
employee_payroll_system.sql
```

### 3. Install Dependency

```bash
python -m pip install mysql-connector-python
```

### 4. Run Application

```bash
python main.py
```

---

## Screenshots

Screenshots of:
- Main Menu
- Employee Management
- Attendance Management
- Payroll Management
- Reports
- Analytics

are available in the `screenshots` folder.

---

## Future Improvements

- Streamlit GUI
- Authentication System
- Employee Dashboard
- Export Reports to PDF
- Salary Slip Generation

---

## Author

Kriti Sharma

B.Tech Computer Science Engineering