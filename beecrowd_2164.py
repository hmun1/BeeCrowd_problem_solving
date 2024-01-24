import math
def fibonacci(n):
    x = ((1+(math.sqrt(5)))/2)**n
    y = ((1-(math.sqrt(5)))/2)**n
    z = x - y
    solution = z/math.sqrt(5)
    print(f'{solution:.1f}')
#read input
n = int(input())
if 0 < n <= 50:
    fibonacci(n)
