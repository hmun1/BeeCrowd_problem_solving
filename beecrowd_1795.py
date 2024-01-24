def triangle_sum(row):
    summation = 3 ** row
    print(summation)
     
#read input
row = int(input())
if 0 <= row <= 20:    # input valid or not
    triangle_sum(row)    #call and execute the program