salida_vehicle = 0
vuelta_vehicle = 0

salida_passengers = 0
vuelta_passengers = 0

while True:
    # Read input
    park = input().split()

    if park[0] == "SALIDA" and len(park) >= 2:
        vehicle = park[0]
        passengers = int(park[1])
        salida_vehicle += 1
        salida_passengers += passengers
    elif park[0] == "VUELTA" and len(park) >= 2:
        vehicle = park[0]
        passengers = park[1]
        passengers = int(park[1])
        vuelta_vehicle += 1
        vuelta_passengers += passengers
    elif park[0] == "ABEND":
        return_jeep = abs(salida_vehicle-vuelta_vehicle)
        return_passenger = abs(salida_passengers-vuelta_passengers)
        print(return_passenger)
        print(return_jeep)
        break
