while True:
    flag = 0
    try:
        n = int(input())
        if n >= 5 and n <= 101 and n % 2 == 1:
            x = n // 2  # Divided to find the middle point
            z = n // 3
            k = n - z
            temp = n-1
            for row in range(0, n):
                for column in range(0, n):
                    if row == column:
                        print('2', end='')
                    elif column == temp:
                        print('3', end='')
                    elif row == z:
                        for i in range(row, k):
                                    print('0', end='')
                                elif j > z and j < n:
                                    print('0', end='')
                                else:
                                    for c in range(j, n-z):
                                        if i == x and c == x:
                                            print('4', end='')
                                        else:
                                            print('1', end='')
                            print()  # Print a newline after each row
                        break  # Exit the loop after printing the central part
                    else:
                        print('0', end='')
                temp -= 1
                print()  # Print a newline after each row
        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break
