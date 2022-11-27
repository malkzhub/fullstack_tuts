# #### Conditionals and Booleans

# # # Comparisons:
# # Equal:              ==
# # Not Equal:          !=
# # Greater Than:       >
# # Less Than:          <
# # Greater or Equal:   >=
# # Less or Equal:      <=
# # Object Identity:    is

# #################


# # # if else
# # # language = 'Python'
# # language = 'Java'

# # if language == 'Python':
# #     print('Language is Python')
# # elif language == 'Java':
# #     print('Language is Java')
# # elif language == 'JavaScript':
# #     print('Language is JavaScript')
# # else:
# #     print('No match')



# #################

# # # Boolean
# # and
# # or
# # not



# # user = 'Admin'
# # logged_in = False

# # # if user == 'Admin' and logged_in:
# # #     print('Admin Page')
# # # else:
# # #     print('Bad Credentials')

# # # if user == 'Admin' or logged_in:
# # #     print('Admin Page')
# # # else:
# # #     print('Bad Credentials')

# # # if not logged_in:
# # #     print('Please Log In')
# # # else:
# # #     print('Welcome')


# ##################

# # # Object Identity - is
# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b) # True
# print()

# print(id(a))
# print(id(b))
# print(a is b) # False


# a = [1, 2, 3]
# b = a

# print()

# print(id(a))
# print(id(b))
# print(a is b) # True
# print(id(a) == id(b)) # True

####################################

# False Values:

    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), []
    # Any empty mapping. For example, {}


# condition = False
# condition = None
# condition = 0 # Evaluated to False
# condition = 10 # Evaluated to True
# condition = '' # Evaluated to False
# condition = () # Evaluated to False
# condition = [] # Evaluated to False
# condition = {} # Evaluated to False

condition = 'Test' # Evaluated to True

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

