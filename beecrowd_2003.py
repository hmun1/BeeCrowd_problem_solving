while True:
    flag = 0
    try:
        time = input()
        h = int(time[0])
        m = int(time[2:4])
        if 5 <= h <= 9: 
            if h == 8:
                print(f'Atraso maximo: {60+m}')
            elif h == 7:
                print(f'Atraso maximo: {m}')
            elif h == 9:
                print(f'Atraso maximo: {60+60+m}')
            else:
                print(f'Atraso maximo: 0')   
        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break