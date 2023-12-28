def jumping_frog_game(height, pipe):
    counter = 0
    lst = list(map(int, input().split()))   # start game to take the pipe number
    for i in range(1, pipe):
        result = lst[i] - lst[i-1]
        if result < 0:
            result = result * (-1)
        if result > height:
            print('GAME OVER')
        else:
            counter += 1
    if counter == pipe-1:
        print('YOU WIN')

#read input
height, pipe = map(int,input().split())
if 1 <=height <= 5 and 2 <= pipe <= 100:    #check the input is valid or not
    jumping_frog_game(height, pipe)      # call the function and execute the program