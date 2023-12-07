def nephew(h, z, l):
    if (h>z and h<l) or (h<z and h>l) :
        print('huguinho')
    elif (z>h and z<l) or (z<h and z>l):
        print('zezinho')
    elif (l>h and l<z) or (l<h and l>z):
        print('luisinho')

h, z, l = map(int, input().split(' '))
nephew(h, z, l)