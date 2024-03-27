def expense(lst, student):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]
    avg = sum / student
    total_min = 0
    total_max = 0
    for expense in lst:
        if expense < avg:
            total_min += int((avg - expense)) / 100.0
        else:
            total_max += int((expense - avg)) / 100.0
    if total_max > total_min:
        print(f'${total_max:.2f}')
    else:
        print(f'${total_min:.2f}')

#read input
while True:
    student = int(input())
    if 1 <= student <= 1000:
        lst = []
        for i in range(student):
            dollar, cent = map(int, input().split('.'))
            lst.append((dollar*100)+cent)
        expense(lst, student)          
    else:
        break