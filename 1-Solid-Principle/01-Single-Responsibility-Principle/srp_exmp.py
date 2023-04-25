'''
Single Responsibility Principle (SRP): Each class should have only one responsibility or reason to change.
'''

# Bad example: A class with multiple responsibilities


class Employee:
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    def calculate_salary(self):
        # logic to calculate salary
        print('Salary is ', self.salary)
        pass

    def save_employee(self):
        # logic to save employee to database
        print(self.name, ' Saved employee details to db')
        pass

    def send_email(self):
        # logic to send email to employee
        print('Email sent to ', self.email)
        pass


'''
In this example, the Employee class has multiple responsibilities: calculating an employee's salary, saving an employee's information to a database, and sending 
an email to the employee. This violates the Single Responsibility Principle because the class has more than one reason to change.
'''


# Good example: Separate classes with single responsibilities
class SalaryCalculator:
    def calculate_salary(self, employee):
        # logic to calculate salary
        print('Salary is', employee.salary)
        pass


class EmployeeDatabase:
    def save_employee(self, employee):
        # logic to save employee to database
        print(employee.name, 'details saved to db')
        pass


class EmailSender:
    def send_email(self, employee):
        # logic to send email to employee
        print('Email sent to', employee.email)
        pass


# Client code
employee = Employee("Keshav Vikas", "keshav@email.com", 150000)
calculator = SalaryCalculator()
database = EmployeeDatabase()
sender = EmailSender()

calculator.calculate_salary(employee)
database.save_employee(employee)
sender.send_email(employee)

'''
In this example, the responsibilities are separated into three different classes: SalaryCalculator, EmployeeDatabase, and EmailSender. Each class has a single
responsibility, which makes the code more modular and easier to maintain. The client code can then create instances of each class and call their respective
methods to perform the desired actions.
'''
