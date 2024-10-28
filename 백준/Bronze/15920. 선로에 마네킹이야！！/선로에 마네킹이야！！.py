N = int(input())
actions = list(input())

trigger = 5
cart_area = "A"
for action in actions:

    if action == "W":
        if cart_area == "A": cart_area = "B"
        elif cart_area == "B": cart_area = "C"
        continue

    if action == "P":
        if cart_area == "A":
            trigger = 1 if trigger == 5 else 5
        elif cart_area == "B":
            trigger = 6

if cart_area != "C": trigger = 0
print(trigger)