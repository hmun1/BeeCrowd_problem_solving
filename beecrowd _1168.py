test_cases = int(input())
j = 0
while j != test_cases:
    number = input()
    sm = 0
    ln = len(number)
    for i in range(ln):
        if number[i] == '1':
            sm = sm + 2
        elif number[i] == '2':
            sm = sm + 5
        elif number[i] == '3':
            sm = sm + 5
        elif number[i] == '4':
            sm = sm + 4
        elif number[i] == '5':
            sm = sm + 5
        elif number[i] == '6':
            sm = sm + 6
        elif number[i] == '7':
            sm = sm + 3
        elif number[i] == '8':
            sm = sm + 7
        elif number[i] == '9':
            sm = sm + 6
        else:
            sm = sm + 6
    print(f'{sm} leds')
    j += 1