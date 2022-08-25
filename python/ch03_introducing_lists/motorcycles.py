#### Lists

## Modifying Elements in a list

motorcycles = [
    'honda',
    'yamaha',
    'suzuki'
]
print(motorcycles)
['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'
print(motorcycles)
# ['ducati', 'yamaha', 'suzuki']

print()

## Adding Elements to a List
motorcycles.append('shirabu')
print(motorcycles)
# ['ducati', 'yamaha', 'suzuki', 'shirabu']


motorcycles2 = []

motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')

print(motorcycles2)
# ['honda', 'yamaha', 'suzuki']

print()

## Inserting Elements into a List

# insert()

motorcycles2.insert(0, 'ducati')
print(motorcycles2)

# ['ducati', 'honda', 'yamaha', 'suzuki']

print()


## Removing Elements from a List

# using del

motorcycles3 = ['honda', 'yamaha', 'suzuki']
print(motorcycles3)
# ['honda', 'yamaha', 'suzuki']

del motorcycles3[0]
print(motorcycles3)
# ['yamaha', 'suzuki']

print()

# using pop() method

motorcycles4 = ['honda', 'yamaha', 'suzuki']
print(motorcycles4)
# ['honda', 'yamaha', 'suzuki']

popped_motorcycles = motorcycles4.pop()
print(motorcycles4) # ['honda', 'yamaha']
print(popped_motorcycles) # suzuki

print()

motorcycles5 = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles5.pop()

print(f"The last motorcycle I owned was a {last_owned.title()}")
# The last motorcycle I owned was a Suzuki

print()

## Popping Items from any Position in a List

first_owned = motorcycles5.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# The first motorcycle I owned was a Honda.

print()

## Removing an Item by Value
motorcycles6 = [
    'honda',
    'yamaha',
    'suzuki',
    'ducati'
]

print(motorcycles6)
# ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles6.remove('ducati')
print(motorcycles6)
# ['honda', 'yamaha', 'suzuki']

print()

motorcycles7 = [
    'honda',
    'yamaha',
    'suzuki',
    'ducati'
]

too_expensive = 'ducati'
motorcycles7.remove(too_expensive)

print(motorcycles7)
print(f"\nA {too_expensive.title()} is too expensive for me.")

########################
#### TRY IT YOURSELF ####
########################
