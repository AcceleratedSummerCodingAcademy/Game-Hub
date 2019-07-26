#ASCA 2019
import random
number = random.randint(1,100)

guess = int(input("Enter your guess: "))

while number != guess:
    if guess > number:
        guess = int(input("That's too big! Guess again: "))
    else:
        guess = int(input("That's too small! Guess again: "))

print("Nice job! You got it!")
