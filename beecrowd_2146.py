def password(number):
     
    formula = number-1
    print(formula)

while True:
    flag = 0
    try:
        number = int(input())
        if 1001<=number<=9999:
                password(number)
        else:
            flag  = 1
    except EOFError:
        break
    if flag == 1:
        break
