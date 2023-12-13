def safety(number):
    x = []
    i = 0
    while i != (number+1):
        row = list(map(int, input().split()))
        x.append(row)
        i += 1
    
    for row in range(0, number):
        for column in range(0, number):
            if x[row][column]+x[row][column+1]+x[row+1][column]+x[row+1][column+1]>=2:
                print('S', end = '')
            else:
                print('U', end = '')
        print()  # Move to the next line after each row


# Read input
number = int(input())
# check input and call the safety function
if 1 <= number <= 100: 
    safety(number)