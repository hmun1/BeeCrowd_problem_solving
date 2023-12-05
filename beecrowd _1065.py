count = 0
for inpt in range(0, 5):
    values = int(input())
    if values % 2 == 0:
        count += 1
print(f'{count} valores pares')
