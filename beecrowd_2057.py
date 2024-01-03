def time_calculation(sum):
    time = 0
    if sum > 24:
        time = sum - 24
        print(time)
    elif sum == 24:
        print('0')
    else:
        print(sum)

    

#read input
s, t, f = map(int, input().split())
sum = 0
if 0 <= s <= 23 and 1 <= t <= 12 and -5 <= f <= 5:
    if s == 0:
        sum = 24 + t + f
        time_calculation(sum)
    else:
        sum = s + t + f
        time_calculation(sum)
        