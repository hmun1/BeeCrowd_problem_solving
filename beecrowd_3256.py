def soldiers(n, m):
    even_list = set()      # even list to store even number
    odd_list = set()        # odd list to store odd number
    counter_even_list = 0
    counter_odd_list = 0

    for i in range(m):
        a, b = map(int, input().split())    #read soldiers number
        if 1 <= a <= n and 1 <= b <= n:      # input is valid or not
            if a % 2 == 0:
                even_list.add(a)
            else:
                odd_list.add(a)
            if b % 2 == 0:
                even_list.add(b)
            else:
                odd_list.add(b)
    counter_even_list = len(even_list)
    counter_odd_list =  len(odd_list)
    if counter_even_list > counter_odd_list:
        print(counter_odd_list)
    elif counter_even_list < counter_odd_list:
        print(counter_even_list)
    else:
        print(counter_even_list)
    print(*odd_list)
    print(*even_list)


#read input
n, m = map(int, input().split())
soldiers(n, m)    #iterate the program