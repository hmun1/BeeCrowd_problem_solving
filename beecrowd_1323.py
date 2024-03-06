def fenyman(a):
    sq = 0
    for i in range(a+1):
        y = i **2
        sq = sq + y
    print(sq)
while True:
    a = int(input())
    if a >= 1:
        fenyman(a)
    else:
        break
