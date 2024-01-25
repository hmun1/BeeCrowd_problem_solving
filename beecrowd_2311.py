# read input
test_cases = int(input())
i = 0
while i != test_cases:
    name = input()
    degree = float(input())
    lst = list(map(float, input().split(' ')))
    mx = lst[0]
    mn = lst[0]
    summation = 0
    for j in range(1, len(lst)):
        if mx < lst[j]:
            mx = lst[j]
        if mn > lst[j]:
            mn = lst[j]
    lst.remove(mx)
    lst.remove(mn)
    for j in range(0, len(lst)):
        summation = summation + lst[j]
    score = summation * degree
    print(f'{name} {score:.2f}')
    i += 1


