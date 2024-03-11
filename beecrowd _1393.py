while True:
    n = int(input())
    if n >= 1 and n <= 40:
        x = 0
        lst = []
        for i in range(0, 2):
            lst.append(i)
        x = lst[0] + lst[1]
        lst.append(x)
        for i in range(2, n+3):
            x = lst[i-1] + lst[i]
            lst.append(x)
        print(lst[n+1])
    else:
        break
