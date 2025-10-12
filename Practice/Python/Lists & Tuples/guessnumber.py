import random

num = random.randint(1, 10)

while True:
    guess = int(input("Guess A Number Between 1 to 10: "))
    if guess == num:
        print("You Guessed A Correct Number")
        break
    elif guess > num:
        print("You Guessed Greater Number")
    elif guess < num:
        print("You Guessed Smaller Number")