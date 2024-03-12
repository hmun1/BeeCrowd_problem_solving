flag = 0
while True:
    try:
        dollar = input()
        cents = int(input())
        x = int(dollar)
        lst = []
        rev = ""
        if x >= 0 and 0 <= cents <= 99:
            ln = len(dollar)
            for index in range(ln-1, -1, -1):
                rev += dollar[index]
            # Group the digits into groups of three
            for i in range(0, len(rev), 3):
                group = rev[i:i+3]
                lst.append(group)
                formatted_integer_part = ",".join(lst)[::-1]
            if cents < 10:
                print(f'${formatted_integer_part}.0{cents}')
            else:
                print(f'${formatted_integer_part}.{cents}')

        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break
