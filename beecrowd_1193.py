def binary(number, c):

    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    lst_1 = []
    print (f'Case {c}:')
    bin_number = number[0]
    ln_bin = len(bin_number)-1

    # binary to decimal
    sum_bin = 0
    f_sum_bin = 0
    for i in range(ln_bin+1):
        x = int(bin_number[ln_bin-i])
        sum_bin = x * (2 ** (i))
        f_sum_bin = f_sum_bin + sum_bin
    print(f'{f_sum_bin} dec')

    # decimal to hexadecimal
    div = f_sum_bin
    lst2 = []
    while div != 0:
        reminder = div % 16
        x = lst[reminder]
        lst_1.append(x)
        div = div // 16
    ln_lst = len(lst_1)
    for i in range(ln_lst, 0, -1):
        lst2.append(lst_1[i-1])
    print(''.join(lst2), 'hex')
    print()

def decimal(number, c):
    print(f'Case {c}:')

    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    lst1 = []
    lst2 = []
    lst3 = []
    lst4 = []

    di = number[0]
    div = int(di)
    div_2 = div

    # decimal to hexadecimal
    while div != 0:
        reminder = div % 16
        x = lst[reminder]
        lst3.append(x)
        div = div // 16
    ln_lst3 = len(lst3)
    for i in range(ln_lst3, 0, -1):
        lst4.append(lst3[i-1])
    print(''.join(lst4), 'hex')

    # decimal to binary
    while div_2 != 0:
        reminder = div_2 % 2
        lst1.append(reminder)
        div_2 = div_2 // 2
    ln_lst2 = len(lst1)
    for i in range(ln_lst2, 0, -1):
        lst2.append(lst1[i-1])
    results = [str(x) for x in lst2]
    print(''.join(results), 'bin')
    print()

def hexadecimal(number, c):
    print(f'Case {c}:')

    # hexadecimal to binary
    dc = number [0]
    ln = len(dc)-1
    sum_1 = 0
    sum = 0
    for i in range (ln+1):
        x = dc[i]
        if x >= '0' and x <= '9':
            y = int(x)
            sum_1 = y * (16**(ln-i))
            sum = sum + sum_1
        else:
            if x == 'a' or x == 'A':
                sum_1 = 10 * (16**(ln-i))
                sum = sum + sum_1

            elif x == 'b'or x == 'B':
                sum_1 = 11 * (16**(ln-i))
                sum = sum + sum_1

            elif x == 'c' or x == 'C':
                sum_1 = 12 * (16**(ln-i))
                sum = sum + sum_1

            elif x == 'd' or x == 'D':
                sum_1 = 13 * (16**(ln-i))
                sum = sum + sum_1

            elif x == 'e' or x == 'E':
                sum_1 = 14 * (16**(ln-i))
                sum = sum + sum_1

            elif x == 'f' or x == 'F':
                sum_1 = 15 * (16**(ln-i))
                sum = sum + sum_1
    print(f'{sum} dec')

    # decimal to binary
    div = sum
    lst1 = []
    lst2 = []

    while div != 0:
        reminder = div % 2
        lst1.append(reminder)
        div = div // 2
    ln_lst1 = len(lst1)
    for i in range(ln_lst1, 0, -1):
        lst2.append(lst1[i-1])
    results = [str(x) for x in lst2]
    print(''.join(results),'bin')
    print()

t_cases = int(input())
c = 1
i = 0
while i != t_cases:
    number = input().split()

    if number[1] == 'bin':
        binary(number, c)

    elif number[1] == 'dec':
        decimal(number, c)

    elif number[1] == 'hex':
        hexadecimal(number, c)

    c += 1
    i += 1

