# ###### Import Modules and Exploring The Standard Library

# ## Location where it checks modules
# import sys

# ## Importing module from differen path
# # sys.path.append('/var/www/html/fullstack_tuts/python/coreyschafer/modules/')

# ## Setting up customized modules folder
# # Just be sure to setup depending on the OS

# # ## Importing Everything
# # from my_module import *

# # # ## Use my_module.py for importing module
# # # import my_module

# # # ## Name for imported module to avoid repetition
# # # import my_module as mm

# ## Importing the function itself
# # from my_module import find_index
# from my_module import find_index, test


# courses = ['History', 'Math', 'Physics', 'CompSci']

# ## module name first then grab whatever is in that module

# # # When using import my_module
# # index = my_module.find_index(courses, 'Math')


# # # When using import my_module as mm
# # index = mm.find_index(courses, 'Math')

# ## When Using from my_module import find_index
# index = find_index(courses, 'Math')

# # print(index)
# # print(test)

# ## Finding location of modules
# # print(sys.path)


######################

# ## Random Library
# import random

# courses = ['History', 'Math', 'Physics', 'CompSci']

# random_course = random.choice(courses)

# print(random_course)

# ## Math Module
# import math

# courses = ['History', 'Math', 'Physics', 'CompSci']

# rads = math.radians(90)

# print(rads)

# ## Sin Values
# print(math.sin(rads))

# ## Date and Time Modules
# import datetime
# import calendar

# courses = ['History', 'Math', 'Physics', 'CompSci']

# today = datetime.date.today()

# print(today)

# print(calendar.isleap(2020))

# ## OS Module
# import os

# courses = ['History', 'Math', 'Physics', 'CompSci']

# print(os.getcwd())

# # viewing location of a specific module

# print(os.__file__)


## Antigravity
import antigravity