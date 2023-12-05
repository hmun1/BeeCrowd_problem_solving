sum = 0
count = 0
for inpt in range(0, 6):
    values = float(input())
    if values > 0:
        count += 1
        sum = sum + values
avg = sum / count
print(f'{count} valores positivos')
print(f'{avg:.1f}')