n = int(input())
parking = [input() for _ in range(n)]
parking_lot_data = set()

for car in parking:
    command, plate = car.split(", ")

    if command == "IN":
        parking_lot_data.add(plate)
    elif command == "OUT":
        parking_lot_data.remove(plate)


if len(parking_lot_data) != 0:
    for car in parking_lot_data:
        print(car)
else:
    print("Parking Lot is Empty")