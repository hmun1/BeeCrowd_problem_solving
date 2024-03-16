def days(food, counter):
    flag = 0
    while True:
        if 0 < food <= 1:
            flag = 1
        else:
            counter += 1
            food = food / 2
        if flag == 1:
            print(f'{counter} dias')
            break

#read input
test_cases = int(input())
for i in range(test_cases):
    food = float(input())
    counter = 0
    if 1 <= food <= 1000:
        days(food, counter)         # iterate the function