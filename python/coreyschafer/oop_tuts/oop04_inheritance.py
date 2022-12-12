
# class Employee:

#     raise_amt = 1.04

#     ## Initialize or Constructor
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = f'{first}.{last}@company.com'

#     def fullname(self):
#         return f'{self.first} {self.last}'

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)


# class Developer(Employee):
#     raise_amt = 1.10

#     def __init__(self, first, last, pay, prog_lang):
#         ## To handle the init variables from the parent class
#         super().__init__(first, last, pay) # or 
#         # Employee.__init__(self, first, last, pay) # Good for multiple inheritance
#         self.prog_lang = prog_lang


# class Manager(Employee):

#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay) 
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees

#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)

#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())


# dev_1 = Developer('Malcolm', 'Abiad', 50000, 'Python')
# dev_2 = Developer('Test', 'User', 60000, 'JavaScript')

# # ## Help Function
# # print(help(Developer))

# # print(dev_1.email)
# # print(dev_2.email)

# # print(dev_1.pay)
# # dev_1.apply_raise()
# # print(dev_1.pay)

# # print(dev_1.email)
# # print(dev_1.prog_lang)


# ## Manager

# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)

# mgr_1.print_emps()


############ Update


class Employee:

    raise_amt = 1.04

    ## Initialize or Constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay) 
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Malcolm', 'Abiad', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'JavaScript')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

## isinstance() - tells an object if it is an instance of a class
print(isinstance(mgr_1, Manager)) ## True
print(isinstance(mgr_1, Employee)) ## True
print(isinstance(mgr_1, Developer)) ## False

print()

print(issubclass(Developer, Employee)) ## True
print(issubclass(Manager, Employee)) ## True
print(issubclass(Manager, False)) ## False

