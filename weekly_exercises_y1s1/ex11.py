import random

def guesses(random_int):
    past_guesses = []
    guess = 0
    while guess != random_int:
        guess = int(input("Please enter a number to guess"))
        if guess != random_int:
            past_guesses.extend(str(guess))

        if guess < random_int:
            print("That guess is too low!")

        if guess > random_int:
            print("That guess is too high")
            

def values():
    low_val = int(input("Please enter a lower value"))
    high_val = int(input("Please enter a higher value"))
    random_int = random.randint(low_val, high_val)
    guesses(random_int)

values()
