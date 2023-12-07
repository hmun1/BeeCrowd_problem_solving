def circle():
    n = int(input())
    for i in range(0, n):
        r1, r2 = map(int, input().split())
        sum = 0
        sum = r1+r2
        print(sum)

circle()