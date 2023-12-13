def fraction(x):
    if 0<=x<=100:
        sum = 3
        fraction_value = 0
        for i in range(x):
            fraction_value += 6
            fraction_value = 1/fraction_value
        sum = sum + fraction_value
        print(f'{sum:.10f}')

x = int(input())
fraction(x)