def sequence(x, counter):
    lst = []
    temp = 0
    for i in range(0, x+1):
        if i >= 1:
            for j in range(0, i):
                lst.append(i)
        else:
            for j in range(0, i+1):
                lst.append(i)

    ln = len(lst)
    if ln > 1:
        print(f'Caso {counter}: {ln} numeros')
        print(*lst)
        print()
    else:
        print(f'Caso {counter}: {ln} numero')
        print(*lst)
        print()
#read input
flag = 0
counter = 0
while True:
    try:
        x = int(input())
        if 0 <= x <= 200:
            counter += 1
            sequence(x, counter)
        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break