#### Strings

## Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
# print(full_name) # ada lovelace

# print(f"Hello, {full_name.title()}!")
# # Hello, Ada Lovelace!

message = f"Hello, {full_name.title()}!"
print(message) # Hello, Ada Lovelace!

# F-strings were first introduced in Python 3.6
# for Python 3.5 or earlier use the format() method

full_name = "{} {}".format(first_name, last_name)
print(f"Using format() method {full_name}")

print()

## Adding Whitespace to Strings
## with Tabs or Newlines

print("Python")
print("\tPython") # indented

print()

print("Languages:\nPython\nC\nJavascript") # newline

# combine \n\t

print("Languages:\n\tPython\n\tC\n\tJavascript") # indented Newline

## Stripping Whitespaces
favorite_language = 'python '
print(favorite_language) # 'python '

print(favorite_language.rstrip()) # 'python'

favorite_language = ' python '
print(favorite_language.rstrip()) # ' python'
print(favorite_language.lstrip()) # 'python '
print(favorite_language.strip()) # 'python'