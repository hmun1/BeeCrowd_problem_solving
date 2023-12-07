while True:
    try:
        flag = 0
        n = int(input())
        if n>=3 and n<70:
            x = n-1
            for row in range(0, n):
                try:
                    for column in range(0, n):
                            if column == x:
                                print('2', end = '')
                            elif column == row:
                                print('1', end = '')
                            else:
                                print('3', end = '')
                    print('\n' ,end = '')
                    x -= 1

                except IndexError:
                    pass
        elif n == 0:
            flag = 1 
    except EOFError:   
        break
    if flag == 1:
            break
                                          
