flag = 0
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
while True:
    try:
        a = input()
        lst1= []
        if a[0] == '0' and a[1] == 'x':
            number = a[2:]
            ln = len(number)-1
            sum = 0
            sum_1 = 1
            for i in range(0, ln+1):
                x = number[i]
                
                if x >= '0' and x <= '9':
                    y = int(x)
                    sum_1 = y * (16**(ln-i))
                    sum = sum + sum_1
                else:
                    if x == 'A' or x == 'a':
                        sum_1 = 10 * (16**(ln-i))
                        sum = sum + sum_1

                    elif x == 'B' or x == 'b':
                        sum_1 = 11 * (16**(ln-i))
                        sum = sum + sum_1

                    elif x == 'C' or x == 'c':
                        sum_1 = 12 * (16**(ln-i))
                        sum = sum + sum_1

                    elif x == 'D' or x == 'd':
                        sum_1 = 13 * (16**(ln-i))
                        sum = sum + sum_1

                    elif x == 'E' or x == 'e':
                        sum_1 = 14 * (16**(ln-i))
                        sum = sum + sum_1

                    elif x == 'F' or x == 'f':
                        sum_1 = 15 * (16**(ln-i))
                        sum = sum + sum_1

            print(sum)
        else:
            b = int(a)
            if b >= 0:
                div = b
                while div != 0:
                    rem = div % 16
                    x = lst[rem]
                    lst1.append(x)
                    div = div // 16
                lst2 = ['0x']
                ln2 = len(lst1)
                for i in range(ln2, 0, -1):
                    lst2.append(lst1[i-1])
                print(''.join(lst2))
                lst1.clear()
            else:
                flag = 1
    except EOFError:
        break
    if flag == 1:
        break