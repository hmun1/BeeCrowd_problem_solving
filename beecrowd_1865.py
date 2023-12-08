def thunder_hummer(test_cases):
    i = 0
    while i != test_cases:
        counter = input().split(' ')
        number = counter[1]
        number = int(number)
        if number >= 1 and number <= 25000:
            if counter[0] == 'Thor':
                print('Y')
            else:
                print('N')
        i += 1
test_cases = int(input())
thunder_hummer(test_cases)
