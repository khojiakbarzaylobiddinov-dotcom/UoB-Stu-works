

name1, name2, name3 = input("Enter three Names: ").split()
print(f"Name1: {name1}\nName2: {name2}\nName3: {name3}")

import datetime
import random

# ==========================================
# 5. Get the first character from the sentence
# ==========================================
sentence_5 = "I have bought 3 footballs for 450.00 £, in the year 2023."
first_char = sentence_5[0]
print(f"5. First character: '{first_char}'")

# ==========================================
# 6. Get the length of the sentence
# ==========================================
sentence_6 = "I have bought 3 footballs."
sentence_length = len(sentence_6)
print(f"6. Length of the sentence: {sentence_length}")

# ==========================================
# 7. Get the current date using today()
# ==========================================
current_date = datetime.date.today()
print(f"7. Current date: {current_date}")

# ==========================================
# 8. Generate a random number between 1 and 100
# ==========================================
random_num = random.randint(1, 100)
print(f"8. Random number (1-100): {random_num}")



# ==========================================
# 9. Program: Random number between two user inputs
# ==========================================
print("\n--- Task 9: Random Number Generator ---")
try:
    # Эти строки ОБЯЗАТЕЛЬНО должны быть с отступом (4 пробела)
    num1 = int(input("Enter the lower bound number: "))
    num2 = int(input("Enter the upper bound number: "))

    lower = min(num1, num2)
    upper = max(num1, num2)

    user_random = random.randint(lower, upper)
    print(f"Random number between {lower} and {upper}: {user_random}")
except ValueError:
    # Эта строка тоже должна быть с отступом
    print("Please enter valid integers.")
