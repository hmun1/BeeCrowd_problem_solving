#read input
test_cases = int(input())
lst = list(map(int, input().split()))
x = lst[0]
index = 0
for i in range(1, len(lst)):
    if x > lst[i]:
        index = i + 1
        break
    else:
        x = lst[i]
print(index)

