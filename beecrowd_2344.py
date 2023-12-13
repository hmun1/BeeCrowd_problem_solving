def numerical_system(number):

    # check grades 
    if number == 0:
        print('E')
    elif number >= 1 and number <= 35:
        print('D')
    elif number >= 36 and number <= 60:
        print('C')
    elif number >= 61 and number <= 85:
        print('B')
    elif number >= 86 and number <= 100:
        print('A')

# Read input
number = int(input())
if 0 <= number <= 100:  # input is valid or not
    numerical_system(number)   # call function