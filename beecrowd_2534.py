# read input
flag = 0
while True:
    try:
        lst1 = []
        lst2 = []
        sorted_list = [0]
        a, b = map(int, input().split())
        if 1 <= a <= 100 and 1 <= b <= 100:
            for i in range(0, a):
                x = int(input())
                lst1.append(x)
            for i in range(0, b):
                y = int(input())
                lst2.append(y)
            for i in range(len(lst1)):
                high = max(lst1)
                sorted_list.append(high)
                lst1.remove(high)
            for j in range(len(lst2)):
                z = lst2[j]
                print(sorted_list[z])

        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break