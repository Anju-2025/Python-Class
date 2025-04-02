# # 1. Generate 50 random ages between 18 and 60 and pick 5 people to send an invitation

import random
ages = [random.randint(18, 60) for _ in range(50)]
invites = random.sample(ages, 5)
print("People selected for invitation:", invites)

# # 2. Generate 10 random numbers between 1 and 100, and calculate their sum and average

# import random
# numbers = [random.randint(1, 100) for _ in range(10)]
# total_sum = sum(numbers)
# average = total_sum / len(numbers)
# print("Numbers:", numbers)
# print("Sum:", total_sum)
# print("Average:", average)
# # 3. Pick 4 random students from a class of 30 and assign them tasks

# import random
# students = [f"Student_{i}" for i in range(1, 31)]
# tasks_assigned = random.sample(students, 4)
# print("Students selected for tasks:", tasks_assigned)
# # 4. Generate 10 random float numbers between 10 and 50 and pick the top 3 highest numbers

# import random
# numbers = [random.uniform(10, 50) for _ in range(10)]
# top_3 = sorted(numbers, reverse=True)[:3]
# print("Generated numbers:", numbers)
# print("Top 3 highest numbers:", top_3)
# # 5. Generate a random 4-digit PIN code

# import random
# pin_code = random.randint(1000, 9999)
# print("Your generated PIN code is:", pin_code)
# # 6. Simulate a dice roll (rolling a dice 5 times) and print each outcome

# import random
# dice_rolls = [random.randint(1, 6) for _ in range(5)]
# print("Dice roll outcomes:", dice_rolls)
# # 7. Generate a random password of 8 characters containing letters and numbers

# import random
# import string
# password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
# print("Generated password:", password)
# # 8. Pick a random day of the week

# import random
# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# random_day = random.choice(days_of_week)
# print("Random day of the week:", random_day)
# # 9. Generate a list of 15 random numbers between 100 and 500, and find the maximum value

# import random
# numbers = [random.randint(100, 500) for _ in range(15)]
# max_value = max(numbers)
# print("Generated numbers:", numbers)
# print("Maximum value:", max_value)
# # 10. Simulate a coin flip 10 times and count the number of heads and tails

# import random
# coin_flip = [random.choice(['Heads', 'Tails']) for _ in range(10)]
# heads_count = coin_flip.count('Heads')
# tails_count = coin_flip.count('Tails')
# print("Coin flip outcomes:", coin_flip)
# print("Heads count:", heads_count)
# print("Tails count:", tails_count)

# import random
# import string

# Function to generate a random password
# def generate_password():
#     all_chars = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choices(all_chars, k=12))
#     return password

# # Generate and print the password
# password = generate_password()
# print("Generated password:", password)


# inbuilt libraries
import math
from math import factorial

# print(math.factorial(5))
# print(factorial(5))
# print(math.pow())
# print(math.lcm())
# print(math.floor(2.5))
# print(math.ceil(2.5))


import random

d=[10,20,30,40,50]
# random.shuffle(d)
# print(d)
# print(random.sample(d,2))
# print(random.choices(d))

# print(random.randint(1,10))
# print(random.randrange(1,10,3))
# 

