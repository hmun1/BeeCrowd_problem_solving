def fibo(x):
    fb = [0] * 2000
    fb[1] = fb[2] = 1
    for i in range(3, 1510):
        fb[i] = (fb[i - 1] + fb[i - 2]) % 1000
    return fb[x]

def exp(x, y):
    p = 1
    while y != 0:
        if y % 2 == 1:
            p = (p * x) % 1500
            y -= 1
        x = (x * x) % 1500
        y //= 2
    return p

n = int(input())
for _ in range(n):
    s1 = input().strip()
    d = l = 0
    for i in range(len(s1) - 1, -1, -1):
        if s1[i] == '1':
            d = (d + exp(2, l)) % 1500
        l += 1
    d = fibo(d)

    if d < 10:
        print("00" + str(d))
    elif d < 100:
        print("0" + str(d))
    else:
        print(d)
