import math

tst_cases = int(input())

for j in range(tst_cases):
    number = int(input())
    counter = 0
    value = int(math.sqrt(number))
    if number == 0 or number == 1:
        print("Not Prime")
        continue
    if number == 2:
        print("Prime")
        continue

    for i in range(2, value + 1):
        if number % i == 0:
            counter += 1
        if counter == 2:
            break

    if counter >= 1:
        print('Not Prime')
    else:
        print("Prime")
