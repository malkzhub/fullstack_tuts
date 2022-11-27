# ### Dictionaries

# # {key: value}

# student = {
#         'name': 'John', 
#         'age': 25, 
#         'courses': ['Math', 'CompSci']
#         }

# print(student)
# print(student['courses'])

# print()

# # print(student['phome']) # KeyError
# print(student.get('phone')) # None
# print(student.get('phone', 'Not Found')) # Customizing default values

# print()

# # Adding key and values
# student['phone'] = '555-5555'


# print(student)

# # Modifying value of key
# student['name'] = 'Jane'
# print(student)

# print()

# # Using update method - update()
# student.update({
#         'name': 'Malcolm',
#         'age': 30,
#         'phone': '09494361755'
#         })

# print(student)

# print()

# # # Deleting key and value

# # del student['age']

# # print(student)

# print()

# # Using pop method

# age = student.pop('age')

# print(student)
# print(age)


# Looping Keys and values

student = {
        'name': 'John', 
        'age': 25, 
        'courses': ['Math', 'CompSci']
        }

print(len(student))

# listing keys
print(student.keys())
# listing values
print(student.values())
# listing keys and values
print(student.items())

print()

# Looping keys

for key in student:
    print(key)

print()

# Looping keys and values

for key, value in student.items():
    print(key + ":", value)