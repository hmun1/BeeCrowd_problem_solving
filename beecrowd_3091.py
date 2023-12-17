def reminder(a, b):
    remind = 0
    if a > b :
        remind = a%b
        print(remind)
    else:
        print(a)


a = int(input())
b = int(input())
if 1 <= a <= 100000 and 1 <= b <= 100000:
    reminder(a, b)



