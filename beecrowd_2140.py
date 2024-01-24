while True:
    lst = [2, 5, 10, 20, 50, 100]
    x, y = map(int, input().split())
    counter = 0
    if x == 0 and y == 0:
        break
    else:
        receive = y - x
        print(receive)
        for i in range(0, len(lst)):
            if counter == 1:
                break
            for j in range(0, len(lst)):
                sum = lst[i]+lst[j]
                if sum == receive:
                    print('Sum = ', sum)
                    counter += 1
                    break
        if counter == 1:
            print('possible')
        else:
            print('impossible')

        