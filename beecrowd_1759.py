def santa_laguh(n):
    for i in range(1, n+1):
        if i == n:
            print('Ho!')
        else:
            print('Ho', end = ' ')

n = int(input())
santa_laguh(n)