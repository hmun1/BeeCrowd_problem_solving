while True:
    flag = 0
    try:
        def height_area(x, y):
            pi = 3.14
            area = y * y * pi
            height_x = x / area
            print(f'ALTURA = {height_x:.2f}')
            print(f'AREA = {area:.2f}')

        height = float(input())
        diameter = float(input())
        radius = diameter / 2
        if height > 0 and diameter > 0:
            height_area(height, radius)
        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break