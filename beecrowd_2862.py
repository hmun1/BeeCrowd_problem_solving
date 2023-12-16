def insect(test_cases):
    i = 0
    while i != test_cases:          # take input to check energy level
        energy_level = int(input())
        if 100 <= energy_level <= 100000:
            if energy_level <= 8000:
                print('Inseto!')
            else:
                print('Mais de 8000!')
        i += 1
# Read input
test_cases = int(input())
insect(test_cases)          # call the function