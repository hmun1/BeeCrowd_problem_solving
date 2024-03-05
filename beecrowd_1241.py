test_cases = int(input())
i = 0
while i != test_cases:
    lst = list(map(int,input().split()))
    temp = 0
    lngth =  len(lst)
    sm = 0
    counter = 0
    avg = 0
    for j in range(1, lngth):
        sm = sm + lst[j]
        counter += 1
    avg = sm / counter
    for j in range(1, lngth):
        if avg < lst[j]:
            temp += 1
    percentage = 100 * (temp / counter)
    print(f'{percentage:.3f}%')
    i += 1
