number = int(input())
j = 0
while j != number:
    lst = list(input())
    updated_list = []
    for i in range(len(lst)):   
        if (lst[i] >= 'a' and lst[i] <= 'z') or (lst[i] >= 'A' and lst[i] <= 'Z'):
            x = chr(ord(lst[i])+3)
            updated_list.append(x)
        else:
            updated_list.append(lst[i])
    riverse_updated_list = []
    for i in range(len(updated_list)-1, -1, -1):
        riverse_updated_list.append(updated_list[i])
    print(*riverse_updated_list)

    length = (len(riverse_updated_list)) // 2
    new_lst = []
    for i in range(0, len(riverse_updated_list)):
        if i < length:
            new_lst.append(riverse_updated_list[i])
        else:
            new_lst.append(chr(ord(riverse_updated_list[i])-1))
    print(*new_lst)
    j += 1

