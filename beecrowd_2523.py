#read input
temp = ''
flag = 0
while True:
    try:
        alphabet = input()
        if alphabet >= "A" and alphabet <= "Z":
            n = int(input())
            lst = list(map(int, input().split()))
            for i in range(0, len(lst)):
                x = lst[i]
                temp = temp+alphabet[x-1]
            print(temp)
            temp = ''
        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break