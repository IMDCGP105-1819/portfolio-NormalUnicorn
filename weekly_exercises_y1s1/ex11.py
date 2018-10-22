import random

def guesses(random_int):
    '''
    Asks the user to guess a number, it then compares if the number is the
    same as the random number, if not it then sees if the number is greater than
    or less than the user guess and will let the user know, and also add the guess
    to a list
    '''
    past_guesses = []
    guess = 0
    while guess != random_int:
        guess = int(input("Please enter a number to guess"))
        if guess != random_int:
            past_guesses.append(guess)

        if guess < random_int:
            print("That guess is too low!")

        if guess > random_int:
            print("That guess is too high")

    print("It took you ", len(past_guesses), " guess(es) to guess the number")
    print("Your previous guess(es) were: ", past_guesses)

def values():
    ''' This function asks for inputs to then use to generate a random number from'''
    low_val = int(input("Please enter a lower value"))
    high_val = int(input("Please enter a higher value"))
    random_int = random.randint(low_val, high_val)
    guesses(random_int)

values()
