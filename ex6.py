def user_input():
    name = str(input("Please enter your name: "))
    age = int(input("Please enter how old you are (in years): "))
    height = int(input("Please enter your height (to the nearest cm): "))
    weight = int(input("Please enter your weight (to the nearest kg): "))
    eyes = str(input("Please enter your eye colour: "))
    hair = str(input("Please enter your hair colour: "))
    print(str(name), str(age), str(height), str(weight), str(eyes), str(hair))



user_input()
