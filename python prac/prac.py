

def lift_move(current_floor, destination_floor):
    print("Lift at floor:", current_floor)

    if current_floor == destination_floor:
        print("Destination reached!")
        return

    if current_floor < destination_floor:
        lift_move(current_floor + 1, destination_floor)

    
    elif current_floor > destination_floor:
        lift_move(current_floor - 1, destination_floor)


current = int(input("Enter current floor: "))
destination = int(input("Enter destination floor: "))

lift_move(current, destination)