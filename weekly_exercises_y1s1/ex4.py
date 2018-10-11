my_name = 'Jordan'
my_age =  1 # maybe
my_height = 1 # inches
my_weight = 1 # pounds
my_eyes = 'Green'
my_hair = 'Brown'
is_heavy = my_weight > 3000
total = my_age + my_height + my_weight
height_cm = 2.54*my_height
weight_kg = 0.45359237*my_weight

print("Let's talk about {}".format(my_name)) # swap in your preferred pronoun.
print("He is {} inches tall".format(my_height))
print("He's {} pounds heavy".format(my_weight))
print("It is {} that he's overweight".format(is_heavy))
print("He's got {} eyes and {} hair".format(my_eyes, my_hair))
print("If I add {}, {} and {} I get {}".format(my_age, my_height, my_weight, total))
print("In proper units, that's {} centimeters tall, and {} kilograms".format(height_cm, weight_kg))
