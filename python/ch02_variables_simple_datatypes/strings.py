# ##### Strings

# # strings_name.py

# ## Changing Case in a String with Methods

# name = "ada lovelace"
# print(name.title()) # Ada Lovelace

# name = "Ada Lovelace"
# print(name.upper()) # ADA LOVELACE
# print(name.lower()) # ada lovelace

# print()

# # strings_fullname.py


# ## Using Variables in Strings
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# # print(full_name) # ada lovelace

# # print(f"Hello, {full_name.title()}!")
# # # Hello, Ada Lovelace!

# message = f"Hello, {full_name.title()}!"
# print(message) # Hello, Ada Lovelace!

# # F-strings were first introduced in Python 3.6
# # for Python 3.5 or earlier use the format() method

# full_name = "{} {}".format(first_name, last_name)
# print(f"Using format() method {full_name}")

# print()

# ## Adding Whitespace to Strings
# ## with Tabs or Newlines

# print("Python")
# print("\tPython") # indented

# print()

# print("Languages:\nPython\nC\nJavascript") # newline

# # combine \n\t

# print("Languages:\n\tPython\n\tC\n\tJavascript") # indented Newline

# ## Stripping Whitespaces
# favorite_language = 'python '
# print(favorite_language) # 'python '

# print(favorite_language.rstrip()) # 'python'

# favorite_language = ' python '
# print(favorite_language.rstrip()) # ' python'
# print(favorite_language.lstrip()) # 'python '
# print(favorite_language.strip()) # 'python'

# print()

# # strings_apostrophe.py

# #### Strings

# ## Avoiding Syntax Errors with Strings

# message = "One of Python's strengths is its divers community"
# print(message)

# # if using all single quotes
# # message = 'One of Pythons's  stengths is its divers community' # error


########################
#### TRY IT YOURSEF ####
########################


# 2-3. Personal Message: Use a variable to represent a person’s name, and print 
# a message to that person. Your message should be simple, such as, “Hello Eric, 
# would you like to learn some Python today?”

try_message = "Hello Malcolm, would you like to learn some python today?"
print(try_message)

print()

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print 
# that person’s name in lowercase, uppercase, and title case.

try_cases = "Malcolm Joseph"
print(try_cases.lower())
print(try_cases.upper())
print(try_cases.title())


print()

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the 
# quote and the name of its author. Your output should look something like the 
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a 
# mistake never tried anything new.”


print("Monkey D. Luffy said \"if you don't take risks, you can't create a future!\"")


print()

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the 
# famous person’s name using a variable called famous_person. Then compose 
# your message and represent it with a new variable called message. Print your 
# message.

famous_person = "Monkey D. Luffy"
message = " said \"if you don't take risks, you can't create a future!\" "

print(famous_person + message)

print()

# 2-7. Stripping Names: Use a variable to represent a person’s name, and include 
# some whitespace characters at the beginning and end of the name. Make sure 
# you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, lstrip(), 
# rstrip(), and strip()

try_name = " Malcolm "

print(f"\t{try_name}")
print(f"\n{try_name}")
print(try_name.strip())
print(try_name.lstrip())
print(try_name.rstrip())


