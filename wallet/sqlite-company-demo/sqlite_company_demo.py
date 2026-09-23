import sqlite3

# Connect to the SQLite database. If it doesn't exist, it will be created.
connection = sqlite3.connect("company.db")

# Create a cursor for executing SQL commands.
cursor = connection.cursor()

# Create the tables for departments and employees.
# First, drop the tables if they already exist to avoid conflicts.
cursor.execute("DROP TABLE IF EXISTS employee")
cursor.execute("DROP TABLE IF EXISTS department")

# Create the department table with id, name, and location fields.
cursor.execute("""
    CREATE TABLE department (
        id INTEGER PRIMARY KEY,
        name TEXT,
        location TEXT
    )
""")

# Create the employee table with id, name, and deptid fields.
cursor.execute("""
    CREATE TABLE employee (
        id INTEGER PRIMARY KEY,
        name TEXT,
        deptid INTEGER,
        FOREIGN KEY (deptid) REFERENCES department(id)
    )
""")

# Insert five department records into the department table.
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

# Insert five employee records into the employee table.
# Note: Employee 4 has deptid 99, which does not exist to demonstrate handling of foreign key constraints.
employees = [
    (1, "Asha Sharma", 1),
    (2, "Rahul Verma", 2),
    (3, "Priya Nair", 2),
    (4, "Vikram Singh", 99),  # This will cause a foreign key constraint error if enforced
    (5, "Neha Patel", 1)
]

cursor.executemany(
    "INSERT INTO employee (id, name, deptid) VALUES (?, ?, ?)",
    employees
)

# Save the changes to the database.
connection.commit()

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