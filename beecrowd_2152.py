def log_program(test_cases):
    i = 0
    while i != test_cases:
        h, m, o = map(int, input().split())
        if o == 1:
            if h > 9:
                if m > 9:
                    print(f'{h}:{m} - A porta abriu!')
                elif m <= 9:
                    print(f'{h}:0{m} - A porta abriu!')
            elif h <= 9:
                if m > 9:
                    print(f'0{h}:{m} - A porta abriu!')
                elif m <= 9:
                    print(f'0{h}:0{m} - A porta abriu!')

        elif o == 0:
            if h > 9:
                if m > 9:
                    print(f'{h}:{m} - A porta fechou!')
                elif m <= 9:
                    print(f'{h}:0{m} - A porta fechou!')
            elif h <= 9:
                if m > 9:
                    print(f'0{h}:{m} - A porta fechou!')
                elif m <= 9:
                    print(f'0{h}:0{m} - A porta fechou!')
        i += 1

test_cases = int(input())
log_program(test_cases)