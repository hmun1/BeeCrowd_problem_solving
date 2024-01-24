def galopeira(test_cases):
    i = 0 
    while i != test_cases:   
        string_input = input()
        length = len(string_input)
        if 9 <= length <= 10000:
            counter = 0
            counter = length // 100
            length = length % 100
            if length > 9:
                print(f'{counter}.{length}')
            else:
                print(f'{counter}.0{length}')

        i += 1
#read input
test_cases = int(input())
galopeira(test_cases)