tst_cases = int(input())
j = 0
while j != tst_cases:
    number = int(input())
    counter = 0
    for i in range(1, number+1):
        if number % i == 0:
            counter += 1
    if counter == 2:
        print('Prime')
    else:
        print('Not Prime')
    j += 1
