number = input()
string = ''
for i in range(len(number)-1, -1, -1):
    string += number[i]
print(''.join(string), '\n')
