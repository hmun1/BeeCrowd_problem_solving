def parity(x):
    counter = 0
    for i in range(0, len(x)):
        if x[i] == '1':
            counter += 1
    if counter % 2 == 0:
        print(f'{x}0')
    else:
        print(f'{x}1')
    
# read input
x = input()
parity(x)

