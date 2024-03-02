flag = 0
while True:

    try:
        a, b = map(int,input().split())
        factorial_1 = 1
        factorial_2 = 1
        if a >= 0 and b >= 0:
            if a > 1:
                if b > 1:
                    i = 1
                    while i != (a+1):
                        factorial_1 = factorial_1 * i
                        i += 1
                    j =  1
                    while j != (b+1):
                        factorial_2 = factorial_2 * j
                        j += 1
                    sum = factorial_1 + factorial_2
                    print(sum)
                
                elif b < 1:
                    i = 1
                    while i != (a+1):
                        factorial_1 = factorial_1 * i
                        i += 1
                    sum = factorial_1 + factorial_2
                    print(sum)
                
                else:
                    i = 1
                    while i != (a+1):
                        factorial_1 = factorial_1 * i
                        i += 1
                    sum = factorial_1 + factorial_2
                    print(sum)

            elif a < 1:
                if b > 1:
                    j =  1
                    while j != (b+1):
                        factorial_1 = factorial_1 * j
                        j += 1
                    sum = factorial_1 + factorial_2
                    print(sum)
                elif b < 1:
                    sum = factorial_1 + factorial_2
                    print(sum)
                else:
                    sum = factorial_1 + factorial_2
                    print(sum)

            else:
                if b > 1:
                    j =  1
                    while j != (b+1):
                        factorial_2 = factorial_2 * j
                        j += 1
                    sum = factorial_1 + factorial_2
                    print(sum)  
                elif b < 1:
                    sum = factorial_1 + factorial_2
                    print(sum)
                
                else:
                    sum = factorial_1 + factorial_2
                    print(sum)
        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break

