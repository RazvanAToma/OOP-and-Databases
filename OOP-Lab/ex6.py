
class Employee:

    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def emp_assign_department(self, department):
        self.emp_department = department


    def calculate_emp_salary(self, salary, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (salary / 50))
            self.emp_salary = salary + overtime_amount


    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")


employee = Employee('E7876', 'ADAMS', 50000, 'ACCOUNTING')

employee.calculate_emp_salary(employee.emp_salary, 61)

employee.print_employee_details()