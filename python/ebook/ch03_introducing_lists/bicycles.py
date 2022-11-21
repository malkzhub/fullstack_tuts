# #### Lists
# ## A list is a collection of items in a particular order.
# ## square brackets([]) indicate a list

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
# # ['trek', 'cannondale', 'redline', 'specialized']

# print()

# ## Accessing Elements in a List
# print(bicycles[0]) # trek

# print()

# ## Accessing Elements and adding string methods
# print(bicycles[0].title()) # Trek

# print()

# ## Index positioning start at 0, not 1
# print(bicycles[1]) # cannondale 
# print(bicycles[3]) # specialized
# print(bicycles[-1]) # specialized

# print()


# ## Using Individual Values from a List
# message = f"My first bicycle was a {bicycles[0].title()}."
# print(message)
# # My first bicycle was a Trek.

# print()

########################
#### TRY IT YOURSELF ####
########################


# 3-1. Names: Store the names of a few of your friends in a list called names. Print 
# each person’s name by accessing each element in the list, one at a time.
names = [
    'Kreme',
    'Kratos',
    'Hera',
    'Hercules',
    'Achilles',
    'Athena'
]
print(names[0].upper())
print(names[1].upper())
print(names[2].lower())
print(names[3].lower())
print(names[4].title())
print(names[5].title())

print()

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
# printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the 
# person’s name.

dog_message1 = f"Hi {names[0]}, how are you doing with Mavis and Ken today?"
dog_message2 = f"{names[1]}, I am so proud of you as the big brother of the pack."
dog_message3 = f"Hey {names[2]}, always be good like you always do."
dog_message4 = f"Mr. Energetic {names[3]}, buddy always be active."
dog_message5 = f"Hey there {names[4]}, please be a good boy and do not bite your siblings"
dog_message6 = f"{names[5]}, be proud of who you are."

print(dog_message1)
print(dog_message2)
print(dog_message3)
print(dog_message4)
print(dog_message5)
print(dog_message6)

print()

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a 
# motorcycle or a car, and make a list that stores several examples. Use your list 
# to print a series of statements about these items, such as “I would like to own a 
# Honda motorcycle.”

car = [
    'Ford',
    'Toyota',
    'Honda',
    'GMC'
]

car_message = f"I would like to own a {car[0]} Mustang!"
print(car_message)