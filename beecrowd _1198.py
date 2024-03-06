
while True:
    try:
        a, b = map(int, input().split())
        y = abs (a - b)
        print(y)
    except EOFError:
        break
        