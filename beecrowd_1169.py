def calculate_wheat(squares):
    grains = 0
    for sq in range(1, x+1):
        grains = grains + ((2) ** (sq -1))
    wheat = grains // 12
    wheat_kg = wheat // 1000
    return wheat_kg

#read input
test_cases = int(input())
for i in range(test_cases):
    x = int(input())
    print(f'{calculate_wheat(x)} kg')