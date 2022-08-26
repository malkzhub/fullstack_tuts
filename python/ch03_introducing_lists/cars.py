#### Lists

## Sorting a List Permanently with the sort() Method

cars = [
    'bmw',
    'audi',
    'toyota',
    'subaru'
]

cars.sort()

print(cars)
#['audi', 'bmw', 'subaru', 'toyota']

print()

## Reverse
cars.sort(reverse=True)
print(cars)
['toyota', 'subaru', 'bmw', 'audi']

print()

## Sorting a List Temporarily with the sorted() Function

cars2 = [
    'bmw',
    'audi',
    'toyota',
    'subaru'
]
print("Here is the origianl list:")
print(cars2)
# Here is the origianl list:
# ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the sorted list:")
print(sorted(cars))
# Here is the sorted list:
# ['audi', 'bmw', 'subaru', 'toyota']

print("\nHere is the original list again:")
print(cars2)
# Here is the original list again:
# ['bmw', 'audi', 'toyota', 'subaru']