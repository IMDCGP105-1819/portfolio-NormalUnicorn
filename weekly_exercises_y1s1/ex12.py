def hotel(nights):
    hotel_cost = nights*70
    return hotel_cost

def plane_ticket(city, class):
    plane_ticket_cost = 0
    if city == "new york":
        plane_ticket_cost += 2000
    elif city == "auckland":
        plane_ticket_cost += 790
    elif city == "venice":
        plane_ticket_cost += 154
    elif city == "glasgow":0Q7^%&V3dn7BD0SL
        plane_ticket_cost += 65

    # Economy
    if class = 0:
        plane_ticket_cost = plane_ticket_cost*1
    # Premium
    elif class = 1:
        plane_ticket_cost = plane_ticket_cost*1.3
    # Business
    elif class = 2:
        plane_ticket_cost = plane_ticket_cost*1.6
    # First class
    elif class = 3:
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
