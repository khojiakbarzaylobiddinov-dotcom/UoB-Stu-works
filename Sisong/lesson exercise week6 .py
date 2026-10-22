numbers = [3,7,2,9,4,1,8]
numbers.append(5)
print(numbers)
numbers.remove(9)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.insert(2,6)
print(numbers.index(4))
print(numbers)
my_tuple = (15, "Python", 3.14, True, 42, False)
print(my_tuple[1])
print(my_tuple[1:4])
print(my_tuple.count(True))

dictionary = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "Diana": 78,
    "Ethan": 88,
    "Fiona": 95,
    "George": 67,
    "Hannah": 83,
    "Ian": 74,
    "Julia": 90,
    "Kevin": 69,
    "Lily": 87,
    "Michael": 76,
    "Nora": 92,
    "Oliver": 81,
}
dictionary["Frank"] = 60
for student, mark in dictionary.items():
    print(f"{student}: {mark}")
#Mutable objects can be changed after they are created. Lists and dictionaries are mutable
#Immutable objects cannot be changed after they are created. Strings, integers, and tuples are immutable
#A local variable is created inside a function and is generally available only there
#A global variable is created outside functions and can be read inside them
