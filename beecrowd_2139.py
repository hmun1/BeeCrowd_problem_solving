while True:
    flag = 0
    try:
       #read input
        x, y = map(int, input().split())
        month_days = [31, 29, 31, 30,31, 30, 31, 31, 30, 31, 30, 31]
        total_days = 360
        days = 0
        if 1 < x > 12:
            flag = 1
        elif x == 1:
            day = total_days - y
            print(f'Faltam {day} dias para o natal!')
        elif 2 <= x <= 12:
            days = y
            for i in range(0, x-1):
                days += month_days[i]
                print(days)
            if days == total_days:
                print('E natal!')
            elif days == (total_days-1):
                print('E vespera de natal!')
            elif days > total_days:
                print('Ja passou!')
            else:
                left = total_days - days
                print(f'Faltam {left} dias para o natal!')
    except EOFError:
        break
    if flag == 1:
        break
