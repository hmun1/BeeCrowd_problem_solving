flag = 0
while True:
    def summation(test_cases):
        i = 0
        while i != test_cases:
            x = int(input())
            if x % 2 == 0:
                y = x - 1
                summ = y + y
                print(summ)
            else:
                y = x - 1
                summ = x + y
                print(summ)
            i += 1

    #read input
    test_cases = int(input())
    if 1 <= test_cases <= 100:
        summation(test_cases)
    else:
        flag = 1
    if flag == 1:
        break