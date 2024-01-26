#read input
test_cases = int(input())
i = 0
while i != test_cases:
    string = input()
    length = len(string)
    if 0 < length <= 25:
        print('Y')
    i += 1