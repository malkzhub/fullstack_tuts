
# class Employee:

#     ## Class Variable
    
#     raise_amount = 1.04

#     ## Initialize or Constructor
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = f'{first}.{last}@company.com'


#     def fullname(self):
#         return f'{self.first} {self.last}'

#     def apply_raise(self):
#         # self.pay = int(self.pay * Employee.raise_amount) # or
#         self.pay = int(self.pay * self.raise_amount)

# emp_1 = Employee('Malcolm', 'Abiad', 50000)
# emp_2 = Employee('Test', 'User', 60000)

# # print(emp_1.__dict__)
# # ## {'first': 'Malcolm', 'last': 'Abiad', 'pay': 50000, 'email': 'Malcolm.Abiad@company.com'}

# # print(Employee.__dict__) # displays value with raise amount

# # # print(Employee.raise_amount) # 1.04
# # # print(emp_1.raise_amount) # 1.04
# # # print(emp_2.raise_amount) # 1.04


# ## Changing value

# # Employee.raise_amount = 1.05
# # print(Employee.raise_amount) # 1.05
# # print(emp_1.raise_amount) # 1.05
# # print(emp_2.raise_amount) # 1.05


# emp_1.raise_amount = 1.05

# print(emp_1.__dict__)

# print()

# print(Employee.raise_amount) # 1.04
# print(emp_1.raise_amount) # 1.05
# print(emp_2.raise_amount) # 1.04



################# Update


class Employee:

    ## Class Variable
    num_of_emps = 0
    raise_amount = 1.04

    ## Initialize or Constructor
    def __init__(self, first, last, pay):
        self.first = first # <-- Instance Variable
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount) # or
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps) # 0 employees initialization

emp_1 = Employee('Malcolm', 'Abiad', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps) # 2 employees