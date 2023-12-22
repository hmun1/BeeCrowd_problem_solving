flag = 0
while True:
    try:
        time = int(input())
        if 0 <= time <= 360:
            if time >= 90 and time < 180:
                print('Boa Tarde!!')
            elif time >= 180 and time < 270:
                print('Boa Noite!!')
            elif time >= 270 and time < 360:
                print('De Madrugada!!')
            else:
                print('Bom Dia!!')
        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break