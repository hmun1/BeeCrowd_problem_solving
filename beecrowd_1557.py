while True:
    flag = 0
    x = input()
    x = int(x)
    if x > 0:
        def matrix_print(n):
            if n <= 2:
                for i in range(0, n):
                    row = []
                    for j in range(i, n+i):
                        row.append(f'{2**j}')
                    print(" ".join(row))
                print()
            else:
                    for i in range(0, n):
                        row = []
                        for j in range(i, n+i):
                            row.append(f'{2**j: >{len(str(2**(2*n-2)))}}')
                        print(" ".join(row))
                    print()
    
        
    elif x == 0:
        flag = 1
    if flag == 1:
        break
    matrix_print(x)