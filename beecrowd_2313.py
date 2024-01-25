def rectangular(a, b, c):
    a = a * a
    b = b * b
    c = c * c
    if (a+b == c) or (b+c == a) or (a+c == b):
        print('Retangulo: S')
    else:
        print('Retangulo: N') 


#read input
a, b, c = map(int, input().split())
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print('Valido-Equilatero')
        rectangular(a, b, c)
    elif a == b or b == c or a == c:
        print('Valido-Isoceles')    
        rectangular(a, b, c) 
    else:
        print('Valido-Escaleno')
        rectangular(a, b, c)

else:
    print('Invalido')