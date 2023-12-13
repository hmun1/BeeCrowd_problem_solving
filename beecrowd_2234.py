def competition(hot_dog, participant):
    average = hot_dog/participant
    print(f'{average:.2f}')

# Read input
hot_dog, participant = map(int, input().split())
if 1 <= hot_dog <= 1000 and 1 <= participant <= 1000:  # check the input is valid?
    competition(hot_dog, participant)   # call the function 
