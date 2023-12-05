count_positive = 0
count_negative = 0
count_even = 0
count_odd = 0
for inpt in range(0, 5):
    values = int(input())
    if values >= 0:
        if values > 0:
            count_positive += 1
        if values % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    else:
        count_negative += 1
        if values % 2 == 0:
            count_even += 1
        else:
            count_odd += 1        
print(f'{count_even} valor(es) par(es)')
print(f'{count_odd} valor(es) impar(es)')
print(f'{count_positive} valor(es) positivo(s)')
print(f'{count_negative} valor(es) negativo(s)')
