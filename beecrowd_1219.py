import math

def roses(area, triangle, radius):
    circle = area - triangle
    sunflowers(area, triangle, circle, radius)

def sunflowers(area, triangle, circle, radius):
    pi = 3.1415926535897
    Circle = (pi * radius * radius) - area

    print(f'{Circle:.4f} {circle:.4f} {triangle:.4f}')


def violates(a, b, c, pi):
    per = (a + b + c) / 2
    area = math.sqrt(per * (per - a) * (per - b) * (per - c))
    radius = (a * b * c) / (4 * area)
    x = area / per
    triangle = pi * x * x
    roses(area, triangle, radius)



#read input
pi = 3.1415926535897
flag = 0
while True:
    try:
        a, b, c = map(int, input().split())
        if 1<=a<=1000 and 1<=b<=1000 and 1<=c<=1000:
            violates(a, b, c, pi)
        else:
            flag = 1
    except EOFError:
        break
    if flag == 1:
        break
