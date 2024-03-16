import sys

def multiple(number):
    if number % 2 != 0 and number % 5 != 0:
        x = 1
        while x % number != 0:
            x = (x * 10) + 1
        ln = len(str(x))
        return ln
    else:
        return -1


# Set the maximum number of digits for integer string conversion
sys.set_int_max_str_digits(10000)

# Read input
flag = 0
while True:
    try:
        number = int(input())
        if 1 <= number <= 10000:
            print(multiple(number))
        else:
            flag = 1

    except EOFError:
        break
    if flag == 1:
        break
