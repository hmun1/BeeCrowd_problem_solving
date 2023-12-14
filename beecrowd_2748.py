for i in range(0, 39):
    print('-', end = '')
print()

words_and_numbers = ["Roberto", "", "5786","", "UNIFEI"]
c = 39
for i in range(0, 5):
    print('|',end = "")
    if i % 2 == 0:
       c = 39 - (len(words_and_numbers[i]))-1
    else:
       c = 39 - (len(words_and_numbers[i]))-2
    for j in range(0, c):
        if i == 0 and j == 10:
            print(words_and_numbers[i], end = '')
        elif i == 2 and j == 10:
            print(words_and_numbers[i], end = '')
        elif i == 4 and j == 10:
            print(words_and_numbers[i], end = '')
        else:
            print(' ', end = '')
    print('|')

for i in range(0, 39):
    print('-', end = '')
print()