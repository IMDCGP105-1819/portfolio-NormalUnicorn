class car:
    def __init__(self, colour, maker, doors, model):
        self.colour = colour
        self.maker = maker
        self.doors = doors
        self.model = model


def choice(user_car):
    user_input = int(input("What do you want to do? \n0-Create a new car\n1-Find out the maker of your car\n2-Find out how many doors your car has\n3-Find out the model of your car\n4-Find out the colour of your car\n5-quit\n6-Change car colour"))
    if user_input == 0:
        user_car.colour = input("Please enter the colour of your car")
        user_car.maker = maker = input("Please enter the maker of your car")
        user_car.doors = input("Please enter how many doors your car has")
        user_car.model = input("Please enter the model of your car")

    elif user_input == 1:
        print("Your car is made by ", user_car.maker)

    elif user_input == 2:
        print("Your car has ", user_car.doors, "doors")

    elif user_input == 3:
        print("Your car is model ", user_car.model)

    elif user_input == 4:
        print("Your car is ", user_car.colour)

    elif user_input == 5:
        quit()
    elif user_input == 6:
        new_col = input("Please enter a new colour for your car")
        user_car.colour = new_col

    choice(user_car)

user_car = car(None, None, None, None)
choice(user_car)
