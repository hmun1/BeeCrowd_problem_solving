def guess_bean(counter):
    numbers = list(map(int, input().split()))
    for i in range(0, 4):
        if numbers[i] == 1:
            counter = i+1
    print(counter)
counter = 0
guess_bean(counter)