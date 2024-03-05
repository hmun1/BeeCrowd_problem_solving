flag = 0
while True:
    try:
        year=int(input())
        if year < 2000:
            flag=1
        else:
            leap_year=(year % 4==0 and year % 100!=0) or (year % 400==0)
            h_festve=(year % 15==0)
            b_festive=(year % 55==0) 
            if leap_year and h_festve and b_festive:
                print("This is leap year.")
                print("This is huluculu festival year.")
                print("This is bulukulu festival year.")
                print()
            elif leap_year and h_festve:
                print("This is leap year.")
                print("This is huluculu festival year.")
                print()
            elif leap_year and b_festive:
                print("This is leap year.")
                print("This is bulukulu festival year.")
                print()
            elif h_festve:
                print("This is huluculu festival year.")
                print()
            elif leap_year:
                print("This is leap year.")
                print()
            else:
                print("This is an ordinary year.")
                print()

    except EOFError:
        break
    if flag==1:
        break