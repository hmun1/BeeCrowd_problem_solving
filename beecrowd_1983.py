def registration_number(test_case):
    lst = []
    index = 1
    i = 0
    while i != test_case:
        a, b = map(float, input().split())
        if b >= 8:
            lst.append(a)
            lst.append(b)
        i += 1
    if len(lst) == 0:
        print('Minimum note not reached')
    else:
        temp = lst[1]
        for i in range(3, len(lst), 2):
            if temp < lst[i]:
                temp = lst[i]
                index = i
        print(int(lst[index-1]))

    

#read number
test_case = int(input())
if 3 <= test_case <= 100:
    registration_number(test_case)