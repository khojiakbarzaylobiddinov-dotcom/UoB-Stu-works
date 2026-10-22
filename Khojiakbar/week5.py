list = [3, 7, 2, 9, 4, 1, 8]
list.append(5)
list.remove(9)
list.sort()
list.reverse()
list.insert(2, 6)
print(list.index(4))

my_tuple = (15, "Python", 3.14, True, 42, False)

# I. Print the index of "Python"
print(my_tuple.index("Python"))

# II. Count how many times True appears
print(my_tuple.count(True))

# III. Print elements from index 1 to index 4
print(my_tuple[1:5])



marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 68,
    "Emma": 77,
    "George": 83,
    "Hannah": 95,
    "Ivan": 64,
    "Jack": 71,
    "Kate": 88,
    "Liam": 79,
    "Mia": 92,
    "Noah": 75,
    "Olivia": 81,
    "Peter": 69
}

# I. Add Frank with a mark of 60
marks["Frank"] = 60

# II. Print all student names and their marks
print(marks)