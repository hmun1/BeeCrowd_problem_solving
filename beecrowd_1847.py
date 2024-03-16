def welcome_winter(a, b, c):
    if a > b and b <= c:
        print(':)')
    elif a < b and b >= c:
        print(':(')
    elif a < b < c and (b - a) > (c - b):
        print(':(')
    elif a < b < c and (a - b) < (c - b):
        print(':)')
    elif a > b > c and (b - c) < (a - b):
        print(':)')
    elif a > b > c and (b - c) > (a - b):
        print(':(')
    elif a == b and b < c:
        print(':)')
    else:
        print(':(')


#read input
a, b, c = map(int, input().split())
if -100 <= a <= 100 and -100 <= b <= 100 and -100 <= c <= 100:
    welcome_winter(a, b, c)