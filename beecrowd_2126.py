def find_subsequence(str1, str2):
    counter = str2.count(str1)
    position = 0
    if counter == 0:
        print('Nao existe subsequencia')
    else:
        print(f'Qtd.Subsequencias: {counter}')
        position = str2.rfind(str1)
        print(f'Pos: {int(position)+1}')
    print()

# read input
    
flag = 0
caso = 1
while True:
    try:
        str1 = input()

        if int(str1) <= 0:
            flag = 1
        else:
            str2 = input()
            print(f'Caso #{caso}:')
            caso += 1
            find_subsequence(str1, str2)
    except EOFError:
        break
    if flag == 1:
        break