
def song(a, b):
    summ = a + b
    if summ == 0:
        print('PROXYCITY')

    elif summ == 1:
        print('P.Y.N.G.')

    elif summ == 2:
        print('DNSUEY!')

    elif summ == 3:
        print('SERVERS')
    
    elif summ == 4:
        print('HOST!')

    elif summ == 5:
        print('CRIPTONIZE')

    elif summ == 6:
        print('OFFLINE DAY')

    elif summ == 7:
        print('SALT')

    elif summ == 8:
        print('ANSWER!')

    elif summ == 9:
        print('RAR?')

    else:
        print('WIFI ANTENNAS')

#read input
test_cases = int(input())
i = 0
while i != test_cases:
    a, b = map(int, input().split())
    song(a, b)
    i += 1