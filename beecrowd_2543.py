while True:
    flag = 0
    try:
        def published_video(gameplays, id):
            counter = 0
            for i in range(gameplays):
                player_id, one = map(int, input().split())
                if player_id == id and one == 0:
                    counter += 1
            print(counter)

        # Read input
        gameplays, id = map(int, input().split())
        if 1 <= gameplays <= 10000 and  1000 <= id <= 9999:   # input is valid or not, call function
            published_video(gameplays, id)
        else:
            flag = 1
    
    except EOFError:
        break
    if flag == 1:
        break
