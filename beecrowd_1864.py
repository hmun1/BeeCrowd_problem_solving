def kierkegaards_quote(index):
    quote = 'Life is not a problem to be solved, but a reality to be experienced.'
    for i in range(index):
        print(quote[i].upper(), end = '')
#read input
index = int(input())
if 1 <= index <= 34:    #check input valid or not
    kierkegaards_quote(index)      #call and execute the program
