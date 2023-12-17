def communication(n, x, y):
    result = n / (x + y )
    print(f'{result:.2f}')

# Read input
n, x, y = map(int, input().split())
if 0 < n < 10000 and 0 < x < 10000 and 0 < y < 1000:     # check input is valid or not
    communication(n, x, y)  # iterate the program