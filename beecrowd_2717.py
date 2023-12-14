def statement(timer, x, y):
    total_time = x+y
    if timer >= total_time:
        print('Farei hoje!')
    else:
        print('Deixa para amanha!')


timer = int(input())
x, y = map(int, input().split())
if 2<=timer<=100 and 1<=x<=100 and 1<=y<=100:
    statement(timer, x, y)