def merry_christmas(number):
    phrase = 'Feliz nata'
    for i in range(0, number):
        if i  == number-1:
            phrase = phrase + 'l!'
        else:
            phrase = phrase + 'a'
    print(phrase)

# Read input
number = int(input())
if number > 0:      # input is valid or not
    merry_christmas(number)   # call christmas function