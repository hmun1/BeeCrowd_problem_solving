def winner(test_cases):
    if 1 <= test_cases <= 100:
        i = 0
        while i != test_cases:
            try:
                sum = 0
                first_line = input().split(' ')
                number1, number2 = map(int, input().split())
                sum =  number1+number2
                if sum % 2 == 0:
                    if first_line[1] == 'PAR':
                        print(first_line[0])
                    elif first_line[3] == 'PAR':
                        print(first_line[2])
                else:
                    if first_line[1] == 'IMPAR':
                        print(first_line[0])
                    elif first_line[3] == 'IMPAR':
                        print(first_line[2])
            except EOFError:
                pass
            i += 1
test_cases = int(input())
winner(test_cases)