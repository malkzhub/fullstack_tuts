# #### Lists

# ## Sorting a List Permanently with the sort() Method

# cars = [
#     'bmw',
#     'audi',
#     'toyota',
#     'subaru'
# ]

# cars.sort()

# print(cars)
# #['audi', 'bmw', 'subaru', 'toyota']

# print()

# ## Reverse
# cars.sort(reverse=True)
# print(cars)
# ['toyota', 'subaru', 'bmw', 'audi']

# print()

# ## Sorting a List Temporarily with the sorted() Function

# cars2 = [
#     'bmw',
#     'audi',
#     'toyota',
#     'subaru'
# ]
# print("Here is the origianl list:")
# print(cars2)
# # Here is the origianl list:
# # ['bmw', 'audi', 'toyota', 'subaru']

# print("\nHere is the sorted list:")
# print(sorted(cars))
# # Here is the sorted list:
# # ['audi', 'bmw', 'subaru', 'toyota']

# print("\nHere is the original list again:")
# print(cars2)
# # Here is the original list again:
# # ['bmw', 'audi', 'toyota', 'subaru']

# print()

# ## Printing a List in Reverse Order
# cars3 = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars3)
# # ['bmw', 'audi', 'toyota', 'subaru']

# cars3.reverse()
# print(cars3)
# # ['subaru', 'toyota', 'audi', 'bmw']

# print()

# ## Finding the Length of a List
# cars4 = ['bmw', 'audi', 'toyota', 'subaru']
# print(len(cars4)) # 4

print()

########################
#### TRY IT YOURSELF ####
########################

# 3-8. Seeing the World: Think of at least five places in the world you’d like to 
# visit.
# •	 Store the locations in a list. Make sure the list is not in alphabetical order.
# •	 Print your list in its original order. Don’t worry about printing the list neatly, 
# just print it as a raw Python list.
# •	 Use sorted() to print your list in alphabetical order without modifying the 
# actual list.
# •	 Show that your list is still in its original order by printing it.
# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# •	 Show that your list is still in its original order by printing it again.
# •	 Use reverse() to change the order of your list. Print the list to show that its 
# order has changed.
# •	 Use reverse() to change the order of your list again. Print the list to show 
# it’s back to its original order.
# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the 
# list to show that its order has been changed.
# •	 Use sort() to change your list so it’s stored in reverse alphabetical order. 
# Print the list to show that its order has changed.

see_world = ['Europe', 'Hawaii', 'Antarctica', 'South America', 'Florida']

# Raw Python List
print(see_world)

print()

# Sorted
print(see_world)
print(sorted(see_world))

print()

# Reverse
print(see_world)

see_world.reverse()
print(see_world)

print()

# Reverse to original order
see_world.reverse()
print(see_world)

print()

# Sort
see_world.sort()
print(see_world)

print()

see_world.sort(reverse=True)
print(see_world)

print()

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
# through 3-7 (page 42), use len() to print a message indicating the number 
# of people you are inviting to dinner.

guest_list = [
    'Mavis',
    'Ken',
    'Ma. Camilla',
    'Lolo Homer',
    'Lola Laleng',
    'Lolo Balayan',
    'Lola Balayan'
]

print(f"I have invited {len(guest_list)} people for dinner later this evening.")

print()

# 3-10. Every Function: Think of something you could store in a list. For example, 
# you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items 
# and then uses each function introduced in this chapter at least once

manga = ['One Piece', 'Naruto', 'Bleach', 'Boku No Hero Academia', 'Black Clover', 'Fairy Tail']

print(manga)
print(manga[5])
print(manga[3].upper())
print(manga[-2].lower())

print(f"{manga[0]} has been going on since 1997")

manga[4] = 'Diamond No Ace'
print(manga)

manga.append('Fire Force')
print(manga)

manga.insert(4, 'Black Clover')
print(manga)

del manga[1]
print(manga)

manga.pop()
print(manga)

manga.pop(3)
print(manga)

manga.remove('Bleach')
print(manga)

manga.sort()
print(manga)

manga.sort(reverse=True)
print(manga)


print(sorted(manga))
manga.reverse()
print(manga)
