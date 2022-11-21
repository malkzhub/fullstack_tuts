# # #### Lists

# # ## Modifying Elements in a list

# # motorcycles = [
# #     'honda',
# #     'yamaha',
# #     'suzuki'
# # ]
# # print(motorcycles)
# # ['honda', 'yamaha', 'suzuki']

# # motorcycles[0] = 'ducati'
# # print(motorcycles)
# # # ['ducati', 'yamaha', 'suzuki']

# # print()

# # ## Adding Elements to a List
# # motorcycles.append('shirabu')
# # print(motorcycles)
# # # ['ducati', 'yamaha', 'suzuki', 'shirabu']


# # motorcycles2 = []

# # motorcycles2.append('honda')
# # motorcycles2.append('yamaha')
# # motorcycles2.append('suzuki')

# # print(motorcycles2)
# # # ['honda', 'yamaha', 'suzuki']

# # print()

# # ## Inserting Elements into a List

# # # insert()

# # motorcycles2.insert(0, 'ducati')
# # print(motorcycles2)

# # # ['ducati', 'honda', 'yamaha', 'suzuki']

# # print()


# # ## Removing Elements from a List

# # # using del

# # motorcycles3 = ['honda', 'yamaha', 'suzuki']
# # print(motorcycles3)
# # # ['honda', 'yamaha', 'suzuki']

# # del motorcycles3[0]
# # print(motorcycles3)
# # # ['yamaha', 'suzuki']

# # print()

# # # using pop() method

# # motorcycles4 = ['honda', 'yamaha', 'suzuki']
# # print(motorcycles4)
# # # ['honda', 'yamaha', 'suzuki']

# # popped_motorcycles = motorcycles4.pop()
# # print(motorcycles4) # ['honda', 'yamaha']
# # print(popped_motorcycles) # suzuki

# # print()

# # motorcycles5 = ['honda', 'yamaha', 'suzuki']

# # last_owned = motorcycles5.pop()

# # print(f"The last motorcycle I owned was a {last_owned.title()}")
# # # The last motorcycle I owned was a Suzuki

# # print()

# # ## Popping Items from any Position in a List

# # first_owned = motorcycles5.pop(0)
# # print(f"The first motorcycle I owned was a {first_owned.title()}.")

# # # The first motorcycle I owned was a Honda.

# # print()

# # ## Removing an Item by Value
# # motorcycles6 = [
# #     'honda',
# #     'yamaha',
# #     'suzuki',
# #     'ducati'
# # ]

# # print(motorcycles6)
# # # ['honda', 'yamaha', 'suzuki', 'ducati']

# # motorcycles6.remove('ducati')
# # print(motorcycles6)
# # # ['honda', 'yamaha', 'suzuki']

# # print()

# # motorcycles7 = [
# #     'honda',
# #     'yamaha',
# #     'suzuki',
# #     'ducati'
# # ]

# # too_expensive = 'ducati'
# # motorcycles7.remove(too_expensive)

# # print(motorcycles7)
# # print(f"\nA {too_expensive.title()} is too expensive for me.")

# ########################
# #### TRY IT YOURSELF ####
# ########################



# # 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
# # would you invite? Make a list that includes at least three people you’d like to 
# # invite to dinner. Then use your list to print a message to each person, inviting 
# # them to dinner.

# guest_list = [
#     'Mavis',
#     'Ken',
#     'Ma. Camilla',
#     'Lolo Homer',
#     'Lola Laleng',
#     'Lolo Balayan',
#     'Lola Balayan'
# ]


# print(f"Hello {guest_list[0]}, would you like to join dinner?")
# print(f"Hello {guest_list[1]}, would you like to join dinner?")
# print(f"Hello {guest_list[2]}, would you like to join dinner?")
# print(f"Hello {guest_list[3]}, would you like to join dinner?")
# print(f"Hello {guest_list[4]}, would you like to join dinner?")
# print(f"Hello {guest_list[5]}, would you like to join dinner?")
# print(f"Hello {guest_list[6]}, would you like to join dinner?")

# print()

# # 3-5. Changing Guest List: You just heard that one of your guests can’t make the 
# # dinner, so you need to send out a new set of invitations. You’ll have to think of 
# # someone else to invite.

# # •	 Start with your program from Exercise 3-4. Add a print() call at the end 
# # of your program stating the name of the guest who can’t make it.
# # •	 Modify your list, replacing the name of the guest who can’t make it with 
# # the name of the new person you are inviting.
# # •	 Print a second set of invitation messages, one for each person who is still 
# # in your list.

# guest_list.pop(1)

# guest_list.insert(4, 'Steve Irwin')

# print(f"Hello {guest_list[0]}, would you like to join dinner?")
# print(f"Hello {guest_list[1]}, would you like to join dinner?")
# print(f"Hello {guest_list[2]}, would you like to join dinner?")
# print(f"Hello {guest_list[3]}, would you like to join dinner?")
# print(f"Hello {guest_list[4]}, would you like to join dinner?")
# print(f"Hello {guest_list[5]}, would you like to join dinner?")
# print(f"Hello {guest_list[6]}, would you like to join dinner?")


# print()

# # 3-6. More Guests: You just found a bigger dinner table, so now more space is 
# # available. Think of three more guests to invite to dinner.
# # •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# # call to the end of your program informing people that you found a bigger 
# # dinner table.
# # •	 Use insert() to add one new guest to the beginning of your list.
# # •	 Use insert() to add one new guest to the middle of your list.
# # •	 Use append() to add one new guest to the end of your list.
# # •	 Print a new set of invitation messages, one for each person in your list.


# guest_list.insert(0, 'Ken')
# guest_list.insert(4, 'Snoopy')
# guest_list.append('Kreme')

# print(f"Hello {guest_list[0]}, would you like to join dinner?")
# print(f"Hello {guest_list[1]}, would you like to join dinner?")
# print(f"Hello {guest_list[2]}, would you like to join dinner?")
# print(f"Hello {guest_list[3]}, would you like to join dinner?")
# print(f"Hello {guest_list[4]}, would you like to join dinner?")
# print(f"Hello {guest_list[5]}, would you like to join dinner?")
# print(f"Hello {guest_list[6]}, would you like to join dinner?")
# print(f"Hello {guest_list[7]}, would you like to join dinner?")
# print(f"Hello {guest_list[8]}, would you like to join dinner?")
# print(f"Hello {guest_list[9]}, would you like to join dinner?")

# print() 

# # 3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
# # arrive in time for the dinner, and you have space for only two guests.
# # •	 Start with your program from Exercise 3-6. Add a new line that prints a 
# # message saying that you can invite only two people for dinner.
# # •	 Use pop() to remove guests from your list one at a time until only two 
# # names remain in your list. Each time you pop a name from your list, print 
# # a message to that person letting them know you’re sorry you can’t invite 
# # them to dinner.
# # •	 Print a message to each of the two people still on your list, letting them 
# # know they’re still invited.
# # •	 Use del to remove the last two names from your list, so you have an empty 
# # list. Print your list to make sure you actually have an empty list at the end 
# # of your program.

# guest_list.pop()
# guest_list.pop()
# guest_list.pop()
# guest_list.pop()
# guest_list.pop()
# guest_list.pop()
# guest_list.pop()
# guest_list.pop()


# print(f"Hello {guest_list[0]}, would you like to join dinner?")
# print(f"Hello {guest_list[1]}, would you like to join dinner?")

# del guest_list[0]
# del guest_list[0]

# print(guest_list)



## Avoiding Index Errors When WOrking with lists

# motorcycles8 = ['honda', 'yamaha', 'suzuki']
# # print(motorcycles8[3])
# # # will produce an error: IndexError: list index out of range

# print(motorcycles8[-1]) # 'suzuki'

# motorcycles9 = []
# print(motorcycles9[-1])
# # Error list index out of range

# ########################
# #### TRY IT YOURSELF ####
# ########################

# 3-11. Intentional Error: If you haven’t received an index error in one of your 
# programs yet, try to make one happen. Change an index in one of your programs to produce an 
# index error. Make sure you correct the error before closing the program.



