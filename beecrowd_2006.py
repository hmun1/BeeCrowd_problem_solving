def tea_test(tea):
    counter = 0
    x = list(map(int, input().split()))
    for i in range(0, len(x)):
        if tea == int(x[i]):
            counter += 1
    print(counter)

tea_type = int(input())
tea_test(tea_type)