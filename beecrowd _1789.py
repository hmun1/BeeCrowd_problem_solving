def faster_slug(lst):
    max = lst[0]
    for i in range(len(lst)):
        if max < lst[i]:
            max = lst[i]
        else:
            continue
    if max < 10:
        print('1')
    elif 10 <= max < 20:
        print('2')
    else:
        print('3')

#read input
while True:
    flag = 0
    try:
        number = int(input())
        if 1 <= number <= 500:
            lst = list(map(int, input().split()))
            faster_slug(lst)
        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break