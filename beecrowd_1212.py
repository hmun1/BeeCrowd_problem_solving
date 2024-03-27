def carrie(x, y, lnx, lny):
    counter = 0
    sum = 0
    temp = 0
    if lnx >= lny:
        i = lnx-1
        ln = lny-1
        while i != -1:
            if ln >= 0:
                sum = int(x[i]) + int(y[ln]) + temp
                if sum > 9:
                    counter += 1
                    temp = 1
                else:
                    temp = 0
            else:
                sum = int(x[i]) + temp
                if  sum > 9:
                    counter += 1
                    temp = 1
                else:
                    temp = 0
            ln -= 1
            i -= 1
    elif lnx <= lny:
        i = lny-1
        ln = lnx-1
        while i != -1:
            if ln >= 0:
                sum = int(y[i]) + int(x[ln]) + temp
                if sum > 9:
                    counter += 1
                    temp = 1
                else:
                    temp = 0
            else:
                sum = int(y[i]) + temp
                if  sum > 9:
                    counter += 1
                    temp = 1
                else:
                    temp = 0
            ln -= 1
            i -= 1
    if counter == 0:
        print("No carry operation.")
    elif counter == 1:
        print(f'{counter} carry operation.')
    else:
        print(f'{counter} carry operations.')

#read number
flag = 0
while True:
    try:
        num1, num2 = map(int, input().split())
        x = str(num1)
        y = str(num2)
        ln_x = len(x)
        ln_y = len(y)
        if (num1 >= 1 and num2 >= 0) or (num1 >= 0 and num2 >= 1) or (num1 >= 1 and num2 >= 1):
            if ln_x <= 10 and ln_y <= 10:
                carrie(x, y, ln_x, ln_y)
        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break

