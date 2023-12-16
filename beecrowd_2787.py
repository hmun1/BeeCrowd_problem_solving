def chess_bord(line, column):
    if line % 2 == 1 and column % 2 == 1:
        print('1')
    elif line % 2 == 1 and column % 2 == 0:
        print('0')
    elif line % 2 == 0 and column % 2 == 1:
        print('0')
    else:
        print('1')

line = int(input())
column = int(input())
chess_bord(line, column)


    
