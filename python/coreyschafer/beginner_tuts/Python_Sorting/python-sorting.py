# # # li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# # # # s_li = sorted(li)
# # # # s_li = li.sort() # returns none
# # # s_li = sorted(li, reverse=True)

# # # print(f'Sorted Variable:\t {s_li}')

# # # ## Sorting data without creating new variables
# # # li.sort()
# # # li.sort(reverse=True)
# # # print(f'Original Variable:\t {li}')

# # # ## Sorted function returns a new sorted list that's why it can be assigned to a variable
# # # ## Sort function sorts the list in place and returns none


# # ### Tuple

# # tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# # # tup.sort()
# # # print(f'Tuple:\t') # AttributeError since tuple has no attribute sort

# # s_tup = sorted(tup)
# # print(f'Tuple:\t {s_tup}')

# # print()


# # ### Dictionary

# # di = {
# #     'name': 'Malcolm',
# #     'job': 'Software Engineer',
# #     'age': None,
# #     'os': 'Ubuntu'
# # }

# # # di.sort() # AttributeError since Dictionary has no attribute sort

# # s_di = sorted(di)
# # print(f'Dict:\t {s_di}') # Sorts keys


# ### Sorting values in a different criteria

# ## Sorting absolute value of a list
# li = [-6, -5, -4, 1, 2, 3]
# s_li = sorted(li, key=abs)

# print(s_li)


#########

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self): # __repr__ - tells python how we want this function represented
        return (f'{self.name}, {self.age}, ${self.salary}')


from operator import attrgetter

e1 = Employee('Malcolm', 30, 70000)
e2 = Employee('Joseph', 25, 80000)
e3 = Employee('Feucoco', 99, 90000)

employees = [e1, e2, e3]

# def e_sort(emp):
#     # return emp.name
#     # return emp.age
#     return emp.salary

# s_employees = sorted(employees, key=e_sort, reverse=True)

# ## Using Lambda
# s_employees = sorted(employees, key=lambda e: e.name)

## Using attrgetter
s_employees = sorted(employees, key=attrgetter('age'))

# print(s_employees) # TypeError if no key is presented

print(s_employees)