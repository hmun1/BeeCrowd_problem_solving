def ticket_price(a, b):
    price_difference = b / a
    updated_price_difference = price_difference - 1
    price = updated_price_difference * 100
    print(f'{price:.2f}%')


#read input
a, b = map(float, input().split())
if 0.00 <= a <= 1000.0 and 0.00 <= b <= 1000.00:
    ticket_price(a, b)