def guessing_game(test_case):
    index = 0 
    guess = list(map(int, input().split()))
    x = guess[0]
    for j in range(len(guess)):
        if x > guess [j]:
          x = guess[j]
          index = j
    print(index+1)
        
# read input
test_case = int(input())
if 1 <= test_case <= 100: # check input valid or not  
    guessing_game(test_case)    # call and execute the program