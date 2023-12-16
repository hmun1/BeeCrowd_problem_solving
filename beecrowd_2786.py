def tiles(x, y):
    type_1_quantity = (x*y) + ((x-1) * (y-1))
    type_2_quantity = ((x-1) + (x-1)) + ((y-1) + (y-1))
    print(type_1_quantity)
    print(type_2_quantity)
x = int(input())
y = int(input())
tiles(x, y)