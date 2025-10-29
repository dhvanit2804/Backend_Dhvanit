'Write a Python program to generate random numbers using the random module. '

import random

random_int = random.randint(1, 100)

random_float = random.random()

numbers = [10, 20, 30, 40, 50]
random_choice = random.choice(numbers)

print(f"Random Integer (1–100): {random_int}")
print(f"Random Float (0–1): {random_float}")
print(f"Random Choice from list: {random_choice}")