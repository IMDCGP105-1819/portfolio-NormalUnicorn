# This code should start printing out messages
def messages(name, age, height, weight, eyes, hair):
    if age < 10:
        print("Hi there youn'un")
    elif age >= 10 and age < 20:
        print("Hi there!")
    elif age >= 20:
        print("Hi there grandpa!")

    if height < 147:
        print("You're a bit of a dwarf aren't you?")
    elif height >= 147 and height < 180:
        print("You're somewhat of a decent height")
    elif height >= 180:
        print("How's the weather up there?")

    if weight < 50:
        print("Are you eating ok?")
    elif weight >= 50 and weight < 3000:
        print("You're a healty weight I guess")
    elif weight >= 3000:
        print("You're a bit overweight")


# Saves me retying inputs all the time
def dev_mode():
    name = "Jordan"
    age = 15
    height = 150
    weight = 90
    eyes = "Green"
    hair = "Brown"
    messages(name, age, height, weight, eyes, hair)

# This asks the user all the inputs
def user_input():
    name = str(input("Please enter your name: "))
    age = int(input("Please enter how old you are (in years): "))
    height = int(input("Please enter your height (to the nearest cm): "))
    weight = int(input("Please enter your weight (to the nearest kg): "))
    eyes = str(input("Please enter your eye colour: "))
    hair = str(input("Please enter your hair colour: "))
    messages(name, age, height, weight, eyes, hair)

# If satement/variable to save me time from entering in the inputs
dev = 1

if dev == 0:
    user_input()
else:
    dev_mode()
