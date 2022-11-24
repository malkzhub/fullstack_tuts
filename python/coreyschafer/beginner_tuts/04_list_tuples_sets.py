# # # ### Lists - []

# # # # courses = ['History', 'Math', 'Physics', 'CompSci']

# # # # print(len(courses)) # 4
# # # # print(courses)
# # # # # ['History', 'Math', 'Physics', 'CompSci']

# # # # print()

# # # # print(courses[0]) # History
# # # # print(courses[3]) # CompSci
# # # # print(courses[-1]) # Compsci
# # # # # print(courses[4]) # IndexError

# # # # print()

# # # # print(courses[0:2]) # ['History', 'Math']
# # # # print(courses[:2]) # ['History', 'Math']
# # # # print(courses[2:]) # ['Physics', 'CompSci']

# # # # print()

# # # # # Append Method - append()
# # # # # Insert Method - append()
# # # # # Extend Method - extend()
# # # # # Remove Method - remove()
# # # # # Pop Method - pop() - filo


# # # # courses_2 = ['Art', 'Education']

# # # # # courses.append('Art')
# # # # # courses.insert(0, 'Art')
# # # # # courses.extend(courses_2)
# # # # # courses.remove('Math')
# # # # # courses.pop()

# # # # # print(courses) 
# # # # # ['History', 'Math', 'Physics', 'CompSci', 'Art']
# # # # # ['Art', 'History', 'Math', 'Physics', 'CompSci', 'Art']
# # # # # ['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']
# # # # # ['History', 'Physics', 'CompSci']
# # # # # ['History', 'Math', 'Physics']

# # # # print()

# # # # # Sorting Lists

# # # # nums = [1, 5, 2, 4, 3]

# # # # # Reverse method - reverse()
# # # # # Sort method - sort()
# # # # # Sorted method - sorted()

# # # # # courses.reverse()
# # # # # courses.sort()
# # # # # courses.sort(reverse=True)
# # # # # nums.sort(reverse=True)

# # # # sorted_courses = sorted(courses)

# # # # # print(courses)
# # # # # print(sorted_courses)
# # # # print(nums)

# # # # print(min(nums)) # 1
# # # # print(max(nums)) # 5
# # # # print(sum(nums)) # 15

# # # # print()


# # # # Finding Values

# # # courses = ['History', 'Math', 'Physics', 'CompSci']

# # # # print(courses.index('CompSci')) # 3
# # # # print(courses.index('Art')) # ValueError

# # # # print('Art' in courses) # False
# # # # print('Math' in courses) # True


# # # # Looping Values

# # # # for course in courses:
# # # #     print(course)



# # # # for index, course in enumerate(courses):
# # # #     print(index, course) # prints out index value 

# # # # print()

# # # # for index, course in enumerate(courses, start=1):
# # # #     print(index, course) # prints out index value 


# # # # Join Method

# # # course_str = ' - '.join(courses)

# # # # Spliting Values

# # # new_list = course_str.split(' - ')

# # # print(course_str)
# # # print(new_list)


# # ### Tuples - Cannot modify tupples (immutable) - ()

# # # # Mutable
# # # list_1 = ['History', 'Math', 'Physic', 'CompSci']
# # # list_2 = list_1

# # # print(list_1)
# # # print(list_2)

# # # print()

# # # list_1[0] = 'Art'

# # # print(list_1)
# # # print(list_2)


# # # print()

# # # Immutable

# # tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# # tuple_2 = tuple_1

# # print(tuple_1)
# # print(tuple_2)

# # print()

# # # tuple_1[0] = 'Art' # TypeError

# # # print(tuple_1)
# # # print(tuple_2)


# ### Sets -  Unordered and No Duplicates - {}

# cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
# art_courses = {'History', 'Math', 'Art', 'Design'}

# # print(cs_courses)
# # print('Math' in cs_courses) # True

# print(cs_courses.intersection(art_courses)) # Same Values
# print(cs_courses.difference(art_courses)) # Different values
# print(cs_courses.union(art_courses)) # All Values


### Empty Lists, Tuples, Sets

# Empty Lists
empty_lists = [] # or
empty_lists = list()

# Empty Tuples
empty_tuples = () # or
empty_tuples = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()



