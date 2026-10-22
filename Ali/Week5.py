list = [3, 7, 2, 9, 4, 1, 8]
list.append(5)
list.remove(9)
list.sort()
list.sort(reverse=True)
list[2] = 6

print(list)
print(list[4])

my_tuple = (15, "Python", 3.14, True, 42, False)
print(my_tuple[1])
my_tuple.count(True)
print(my_tuple[0:4])

studentscore = {
    "Jimmy": 60,
    "Alice": 85,
    "Bob": 72,
    "Jim": 60,
    "Ali": 85,
    "Bo": 72,
    "immy": 60,
    "Alce": 85,
    "B": 72,
    "kjjhh": 60,
    "wsedrftgyhujiko": 85,
    "huiiy": 72,
    "student": 12,
    "sturent": 15,
    "OyeComoVa": 22,
}

studentscore["Frank"] = 60

print(studentscore)

# A mutable and immutable are info storing types in python, however, the difference between the two of them is that mutable can have data types overwritten after it's been created, immutable cannot. lists, sets, and dictionaries are mutable, while tuples are immutable.
# Local variables are variables that are defined and only useable within a function or single data storage, global variables are variables that are stored globally in python and can be used anywhere within the code.