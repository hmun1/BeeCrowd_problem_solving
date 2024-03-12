test_cases = int(input())
i = 0
while i != test_cases:
    a, b = map(int, input().split())
    lst_a = []
    lst_b = []
    for x in range(2, a):
        y = int(a / x)
        lst_a.append(y)
    for x in range(2, b):
        y = int(a / x)
        lst_b.append(y)
    max_a = lst_a[0]
    max_b = lst_b[0]
    for x in range(len(lst_a)):
        if max_a < lst_a[x]:
            max_a = lst_a[x]
    for x in range(len(lst_b)):
        if max_b < lst_b[x]:
            max_b = lst_b[x]
    if max_a > max_b:
        print(max_a)
    else:
        print(max_b)
    i += 1