def alphabet(l):  
    index = 0    # index for storing index number of character
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(0,len(letter)):
        if l == letter[i]:
            index = index + 1
            print(index)
            break
        else:
            index += 1
l = input()     # Read input
alphabet(l)     # iterate the program
