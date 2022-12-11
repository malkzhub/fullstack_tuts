## Python Object-Oriented Programming

class Employee:

    ## Initialize or Constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'
        # return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Malcolm', 'Abiad', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
# print(emp_2.fullname())

## Run using class name
emp_1.fullname()
print(Employee.fullname(emp_1))

