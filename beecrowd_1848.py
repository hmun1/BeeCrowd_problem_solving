sum = 0
counter = 0
while True:
    if counter == 3:
        break
    else:
        x = list(input().split(' '))
        print(x)
        for i in range(0, len(x)):
            if x[i] == 'caw' and x[i+1] == 'caw':
                print(sum)
                counter += 1
                sum = 0
                break
            elif x[i] == '---':
                sum += 0
            elif x[i] == '--*':
                sum += 1
            elif x[i] == '-*-':
                sum += 2
            elif x[i] == '-**':
                sum += 3
            elif x[i] == '*--':
                sum += 4
            elif x[i] == '*-*':
                sum += 5
            elif x[i] == '**-':
                sum += 6
            elif x[i] == '***':
                sum += 7
