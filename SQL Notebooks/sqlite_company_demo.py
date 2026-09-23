import sqlite3

# Connect to the SQLite database.
connection = sqlite3.connect("company.db")

# Create a cursor for executing SQL commands.
cursor = connection.cursor()

# Create the tables.
cursor.execute("DROP TABLE IF EXISTS employee")
cursor.execute("DROP TABLE IF EXISTS department")

cursor.execute("""
    CREATE TABLE department (
        id INTEGER PRIMARY KEY,
        name TEXT,
        location TEXT
    )
""")

cursor.execute("""
    CREATE TABLE employee (
        id INTEGER PRIMARY KEY,
        name TEXT,
        deptid INTEGER
    )
""")

# Insert exactly five department records.
departments = [
    (1, "Human Resources", "Mumbai"),
    (2, "Information Technology", "Bengaluru"),
    (3, "Sales", "Delhi"),
    (4, "Finance", "Hyderabad"),
    (5, "Operations", "Chennai")
]

cursor.executemany(
    "INSERT INTO department (id, name, location) VALUES (?, ?, ?)",
    departments
)

# Insert exactly five employee records.
# Employee 4 has deptid 99, which does not exist.
employees = [
    (1, "Asha Sharma", 1),
    (2, "Rahul Verma", 2),
    (3, "Priya Nair", 2),
    (4, "Vikram Singh", 99),
    (5, "Neha Patel", 1)
]

cursor.executemany(
    "INSERT INTO employee (id, name, deptid) VALUES (?, ?, ?)",
    employees
)

# Save the changes to the database.
connection.commit()

# Find and display employees who work in the Human Resources department.
cursor.execute("""
    SELECT employee.name
    FROM employee
    INNER JOIN department ON employee.deptid = department.id
    WHERE department.name = 'Human Resources'
""")
hr_employees = cursor.fetchall()

print("Employees in Human Resources:")
for employee in hr_employees:
    print(employee[0])

print()

# Fetch and display all employee records.
cursor.execute("SELECT id, name, deptid FROM employee")
employee_records = cursor.fetchall()

print("Employees:")
print("ID | Name         | DeptID")
print("--------------------------")

for employee in employee_records:
    print(f"{employee[0]}  | {employee[1]:12} | {employee[2]}")

print()

# Fetch and display all department records.
cursor.execute("SELECT id, name, location FROM department")
department_records = cursor.fetchall()

print("Departments:")
print("ID | Name                 | Location")
print("-------------------------------------")

for department in department_records:
    print(f"{department[0]}  | {department[1]:20} | {department[2]}")

# Close the cursor and database connection.
cursor.close()
connection.close()