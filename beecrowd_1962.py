def passed_year(x, test_case):
    i = 0
    while i != test_case:
        year = int(input())
        if year >= 2015:
            print(f'{year - 2014} A.C.')
        else:
            print(f'{2015-year} D.C.')
        i += 1
x = 2014
test_case = int(input())
if 1 <= test_case <= 100000:
    passed_year(x,test_case)