import math
def prime_number(x):
    if x >= 17:
        minimum_number = x / (math.log(x))
        maximum_number = 1.25506 * minimum_number
        print(f'{minimum_number:.1f} {maximum_number:.1f}')

x = int(input())
flag = 0
prime_number(x)
