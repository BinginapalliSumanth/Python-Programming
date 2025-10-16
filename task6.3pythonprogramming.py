def write_employee_report(filename):
    employees = [
        {"name": "Alice", "department": "HR"},
        {"name": "Bob", "department": "Engineering"},
        {"name": "Charlie", "department": "Finance"}
    ]

    with open(filename, "w") as file:
        for employee in employees:
            line = f"Name: {employee['name']}, Department: {employee['department']}\n"
            file.write(line)

def read_employee_report(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)

# Write to file
write_employee_report("employee_report.txt")

# Read from file and print
read_employee_report("employee_report.txt")

