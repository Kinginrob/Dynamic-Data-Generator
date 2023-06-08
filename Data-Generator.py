import csv
import datetime
import logging

logging.basicConfig(filename='employee_data.log', 
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class Employee:
    def __init__(self, first_name, last_name, id, dept_id, manager_name, join_date, dob, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.dept_id = dept_id
        self.manager_name = manager_name
        self.join_date = join_date
        self.dob = dob
        self.age = age
        self.salary = salary


class Department:
    def __init__(self, name, id):
        self.name = name
        self.id = id


def generate_data():
    try:
        employees = []
        departments = []

        # Generate department data
        for i in range(1, 11):
            departments.append(Department(f'Department_{i}', i))
        # Generate employee data
        for i in range(1, 1001):
            dept = departments[i % 10]
            dob_year = max(1963, 2023 - (i % 50))
            dob = datetime.date(dob_year, (i % 12) + 1, (i % 28) + 1)
            join_year = max(1995, 2023 - ((i // 10) % 29))
            join_date = datetime.date(join_year, ((i+6) % 12) + 1, ((i+15) % 28) + 1)
            age = 2023 - dob_year
            employees.append(Employee(f'First_{i}', f'Last_{i}', i, dept.id, f'Manager_{i}', join_date, dob, age, 10000 + (i % 90000)))

        # Write to CSV
        write_to_csv('departments.csv', departments, ["dept_name", "dept_id"])
        write_to_csv('employees.csv', employees, ["emp_first_name", "emp_last_name", "emp_id", "dept_id", "emp_manager_name", "date_of_joining", "dob", "emp_age", "emp_salary"])

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)


def write_to_csv(filename, data, headers):
    try:
        with open(filename, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for item in data:
                writer.writerow([attr for attr in vars(item).values()])
    except Exception as e:
        logging.error(f"Error writing to file {filename}", exc_info=True)


generate_data()
