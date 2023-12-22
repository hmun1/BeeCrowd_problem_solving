def gdp_flactuation_calculation(f1, f2):
    f1_calculation = 100.00 +f1
    f2_calculation = f2/100.00 + 1
    calculation = f1_calculation * f2_calculation
    updated_calculation = calculation - 100.00
    print(f'{updated_calculation:.6f}')

f1,f2=map(float,input().split())
if -100.00 <= f1 <= 100.00 and -100.00 <= f1 <= 100.00:
    gdp_flactuation_calculation(f1, f2)