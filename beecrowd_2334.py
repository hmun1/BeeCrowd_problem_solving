#read input
flag = 0
while True:
    a = int(input())
    if a < 0:
        flag = 1
    elif a == 0:
        print('0')
    else:
        print(a-1)
    if flag == 1:
        break