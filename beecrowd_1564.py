while True:
    flag = 0
    try:
        complaints = int(input())
        if complaints >= 0 and complaints <= 100:
            if complaints == 0:
                print('vai ter copa!')
            else:
                print('vai ter duas!')
        else:
            flag = 1
    
    except EOFError:
        break
    if flag == 1:
        break