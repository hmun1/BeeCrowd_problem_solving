while True:
    flag = 0
    x = input()
    x = int(x)
    if x > 0:
        def matrix_print(n):
            for i in range(1, n + 1):
                row = []
                if i == 1:
                    for j in range(i, n+1):
                        row.append(f'{j: >3}')
                else:
                    if n<=2:
                        for j in range(i, 0, -1):
                           row.append(f'{j: >3}')
                    else:
                        for j in range(i, 0, -1):
                            s = i
                            if j == 1:
                                row.append(f'{j: >3}')
                                for k in range(2, (n-s)+2):
                                    row.append(f'{k: >3}')
                            else:
                                row.append(f'{j: >3}')

                print(" ".join(row))
            print()
        
    elif x == 0:
        flag = 1
    if flag == 1:
        break
    matrix_print(x)