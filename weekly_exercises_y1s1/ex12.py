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
    elif city == "glasgow":
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












def total_cost():
