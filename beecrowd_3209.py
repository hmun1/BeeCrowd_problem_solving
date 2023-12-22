def power_strip(test_cases):
    i = 0
    while i != test_cases:
        sum = 0
        o = list(map(int, input().split(' ')))
        k = o.pop(0)
        for i in range(0, k):
            sum = sum + o[i]
        sum = sum - (k-1)
        print(sum)
        i += 1



test_cases = int(input())
if 1 <= test_cases <= 20:
    power_strip(test_cases)