def sum(test_cases):
    i = 0
    while i != test_cases:
        try:
            number = int(input())
            summation = 0
            if number >=1 and number <= 1000: 
                for i in range(1, number+1):
                    if i%2 != 0:
                        summation += 1
                    else:
                        summation -= 1
                print(summation)
        except EOFError:
            pass
        i += 1
test_cases = int(input())
sum(test_cases)