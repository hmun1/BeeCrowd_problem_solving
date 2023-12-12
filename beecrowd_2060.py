def multiple(number, binos_list):
    multiple_list = [2, 3, 4, 5]
    for j in range(0, len(multiple_list)):
        counter = 0
        for k in range(0, len(binos_list)):
            if binos_list[k] % multiple_list[j] == 0:
                counter += 1
        print(f'{counter} Multiplo(s) de {(multiple_list[j])}')

        

number = int(input())
if 1<=number<=1000:
    binos_list = list(map(int, input().split()))
    multiple(number, binos_list)