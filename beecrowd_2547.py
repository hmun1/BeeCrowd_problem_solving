flag = 0
while True:
    try:
        #read input
        test_cases, mini, maxi = map(int, input().split())
        if 1 <= test_cases <= 100:
            counter = 0
            i = 0
            while i != test_cases:
                x = int(input())
                if mini <= x <= maxi:
                    counter += 1
                i += 1
            print(counter)
        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break