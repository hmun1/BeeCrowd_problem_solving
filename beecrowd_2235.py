def time_travel_machine(credit_1, credit_2, credit_3):
    if credit_1 - credit_2 == 0:  # check if time travel is possible
        print('S')
    elif credit_1 - credit_3 == 0:   # check if time travel is possible
        print('S')
    elif credit_2 - credit_3 == 0:    # check if time travel is possible
        print('S')
    elif credit_1+credit_2-credit_3 == 0:    # check if time travel is possible
        print('S')
    elif credit_1+credit_3-credit_2 == 0:     # check if time travel is possible
        print('S')
    elif credit_2+credit_3-credit_1 == 0:      # check if time travel is possible
        print('S')
    else:
        print('N')

# Read input
credit_1, credit_2, credit_3 = map(int, input().split())
# call the function time_travel
if 1 <= credit_1 <= 1000 and 1 <= credit_2 <= 1000 and 1 <= credit_3 <= 1000:
    time_travel_machine(credit_1, credit_2, credit_3)