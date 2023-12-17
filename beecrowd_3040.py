def christmas_tree(number):
    i = 0
    while i != number:
        height, width, branch = map(int, input().split())    # Read input
        if 200 <= height <= 300 and width >= 50 and branch >= 150:
            print('Sim')
        else:
            print('Nao')
        i += 1

# Read input
test_cases = int(input())
if 0 < test_cases <= 10000:   # check input is valid or not
    christmas_tree(test_cases)    # iterate the program