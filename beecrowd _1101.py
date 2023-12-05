while(True):
    m, n = map(int, input().split())
    sum = 0
    values = ''
    if  m > 0 and n > 0:
        if m > n :
            for i in range(n, m+1):
                sum = sum + i
                values += str(i)+' '
        else:
            for i in range(m, n+1):
                sum = sum + i
                values += str(i)+' '
        values = values+'Sum=%d'       
        print(''.join(map(str,values)) %sum)
    else:
        break