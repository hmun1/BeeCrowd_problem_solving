#read input
flag = 0
while True:
    try:
        summation2 = 0
        summation1 = 0
        test_case = int(input())
        if 1 <= test_case <= 40:
            i = 0
            while i != test_case:
                
                n, c = map(int, input().split())
                multiplication = n * c
                summation1 = summation1 + multiplication
                temp = c * 100
                summation2 = summation2 + c
                i += 1
            result = summation1 /(summation2 * 100)
            print(f'{result:.4f}')
        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break


