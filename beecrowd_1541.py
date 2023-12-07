import math
while True:
    flag = 0
    try:
        x, y, z = map(int, input().split())
        if x>0 and y>0 and z>0:
            area = (x*y)/(z/100)
            best_size = math.sqrt(area)
            best_size = int(best_size)
            print(best_size)
        else:
            flag = 1
    except ValueError:
        break
    if flag == 1:
        break
