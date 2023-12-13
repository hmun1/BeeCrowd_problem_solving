while True:
    flag = 0
    def event(values, monsters):
        exp_value = monsters * values
        print(exp_value)

    values, monsters = map(int, input().split())
    if 0 < values <= 3:
        event(values, monsters)
    elif values == 0 and monsters == 0:
        flag = 1
    if flag == 1:
        break
