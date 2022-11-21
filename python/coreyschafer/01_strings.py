message = 'Hello World'

print(message)

# length of message
print(len(message)) # 11

print()

# Indexing
print(message[0]) # H

print()

# Slicing

print(message[0:5]) # Hello
print(message[:5]) # Hello
print(message[6:]) # World

print()

### String Methods 
print(message.lower()) # hello world
print(message.upper()) # Hello World

print()

# Count Method - count()
print(message.count('l')) # 3

print()

# Find Method - find()
print(message.find('World')) # 6
print(message.find('Universe')) # -1

print()

# # Replace Method - replace()
# message = message.replace('World', 'Universe')
# print(message) # Hello Universe

print()

# Combining variables
greeting = 'Hello'
name = 'Michael'

# message = greeting + ', ' + name + '. Welcome!'

# Formatted String
# message = '{}, {}. Welcome!'.format(greeting, name)
message = f'{greeting}, {name.upper()}. Welcome!'

print(message)

print()

print(dir(name))

print()

print(help(str))
