def dices(number):
    result = ((number + 1) * (number + 2)) / 2
    print(f'{result:.0f}')

# Read input
number = int(input())
if 0 <= number <= 10000:      # input is valid or not
    dices(number)        # iterate the program