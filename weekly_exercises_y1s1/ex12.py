def hotel(nights):
    hotel_cost = nights*70
    return hotel_cost

def plane_ticket(city, travel_class):
    plane_ticket_cost = 0
    if city == "new york":
        plane_ticket_cost += 2000
    elif city == "auckland":
        plane_ticket_cost += 790
    elif city == "venice":
        plane_ticket_cost += 154
    elif city == "glasgow":
        plane_ticket_cost += 65

    # Economy
    if travel_class == 0:
        plane_ticket_cost = plane_ticket_cost*1
    # Premium
    elif travel_class == 1:
        plane_ticket_cost = plane_ticket_cost*1.3
    # Business
    elif travel_class == 2:
        plane_ticket_cost = plane_ticket_cost*1.6
    # First class
    elif travel_class == 3:
        plane_ticket_cost = plane_ticket_cost*1.9

    return plane_ticket_cost

def rental_car(days):
    rental_car_cost = 0
    if days < 3:
        rental_car_cost = 30*days

    elif days > 2 and days < 7:
        rental_car_cost = (30*days) - 30

    elif days > 6:
        rental_car_cost = (30*days) - 50

    return rental_car_cost

def total_cost():
    total = 0
    night = int(input("Please enter how many nights you will be staying for"))
    car_rent = int(input("Please enter how many days you want to rent a car for"))
    city = input("Please enter which city you wish to visit, New York, Auckland, Venice, or Glasgow").lower()
    plane_class = int(input("Please enter which plane ticket you would like \n0 - Economy \n1 - Premium \n2 - Business \n3 -First Class"))
    total += hotel(night)
    total += plane_ticket(city, plane_class)
    total += rental_car(car_rent)
    print("The total cost of your holiday is ", total)
    print("The cost of your hotel is", str(hotel(night)))
    print("The cost of your plane travel is", str(plane_ticket(city, plane_class)))
    print("The cost of your car rental is", rental_car(car_rent))


total_cost()
