flag = 0
while True:
    try:
        v, t = map(int, input().split())
        if v < -100 or t < 0:
            flag = 1
        else:
            if -100 <= v <= 100 and 0 <= t <= 200:
                displacement = 2 * (v * t)
                print(displacement)
    except EOFError:
        break
    if flag == 1:
        break