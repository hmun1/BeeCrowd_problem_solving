import math

def pizza_fit(radius, lst, counter):
    diameter = 2 * radius
    ab = lst[1] ** 2
    bc = lst[2] ** 2
    ac = math.sqrt(ab + bc)

    if diameter >= ac:
        print(f'Pizza {counter} fits on the table.')
    else:
        print(f'Pizza {counter} does not fit on the table.')

counter = 0
while True:
    # read input
    lst = list(map(int,input().split()))
    counter += 1
    radius = lst[0]
    #check input valid or not
    if 1 <= radius <= 1000:
        pizza_fit(radius, lst, counter)
    else:
        break