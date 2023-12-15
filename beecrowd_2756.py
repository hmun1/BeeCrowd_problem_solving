def shape(n):
    lst = ['A', 'B', 'C', 'D', 'E']   # list for character
    length = len(lst)-1
    updated_length = len(lst)
    for i in range(n-2):                               # first triangle loop
        for j in range(i, n):                          # space printing from 0 to 7
            print(' ', end = '')
        if i <= length:
            if i == 1:   
                for k in range(i, i+1):
                    print(lst[k], lst[k])
            else:
                for k in range(i, i+1):                 # character printing as per the index
                    if i < 2:
                        print(lst[k])
                    else:
                        if i == 2: 
                            print(lst[i], end = '')    
                            for x in range(0, i+1):     # 3 spaces printing after character
                                print(' ', end = '')
                            for y in range(i, i+1):     # last character print in each line
                                print(lst[y])
                        elif i == 3:
                            print(lst[i], end = '')     # 5 spaces printing after character
                            for x in range(0, i+2): 
                               print(' ', end = '')
                            for y in range(i, i+1):     # last character print in each line
                               print(lst[y])
                        else:
                            print(lst[i], end = '')     # 7 spaces printing after character
                            for x in range(0, i+3):
                               print(' ', end = '')
                            for y in range(i, i+1):     # last character print in each line
                               print(lst[y])
                            
        else:
            break
    for i in range(3, n):                               # second triangle loop
        for j in range(0, i+1):
            print(' ', end = '')
        for k in range(i, i+1):
            x = updated_length -k+1
            if x == 1:
                print(lst[x], lst[x])
            elif x == 0:
                print(lst[x])
            elif x == 3:
                print(lst[x], end = '')
                for n in range(0, 5):                   # 5 spaces printing after character
                    print(' ', end = '')
                for o in range (x, x+1):                # last character print in each line
                    print(lst[x])
            elif x == 2:
                print(lst[x], end = '')
                for n in range(0, 3):                   # 3 spaces printing after character
                    print(' ', end = '')
                for o in range (x, x+1):                # last character print in each line
                    print(lst[x])
# Read input
n = 7
shape(n)   # call shape function to execute the program