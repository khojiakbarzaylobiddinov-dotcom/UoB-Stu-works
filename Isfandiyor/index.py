#Second task

numbers = [3,7,2,9,4,1,8]

numbers.append(5)
numbers.remove(9)

numbers.sort()

numbers.sort(reverse=True)

numbers[2] = 6

print(numbers)
print(numbers.index(4))

#Third task
my_tuple = (15, "Python", 3.14, True, 42, False)
print("The index of 'Python' is:", my_tuple.index("Python"), 'True counter:',my_tuple.count(True),"Elements from 1 to 4", my_tuple[1:5])

#Fourth task

student_dictionary = {"George":75,
    "Tom":78,
    "Anne":99,
    "Twain":65,
    "Guy":14,
    "Theo":45,
    "Noah":24,
    "Lee":33,
    "Privald":45,
    "Baptist":95,
    "Batistuta":65,
    "Ilon":71,
    "Jean":87,
    "Johnny":65,
    "Trax":71,
}

student_dictionary['Frank'] = 60

print(student_dictionary)