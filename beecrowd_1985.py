def MacPRONALTS(number):
    total_price = 0
    product_number = ['1001', '1002', '1003', '1004', '1005']
    price_list = ['1.50', '2.50', '3.50', '4.50', '5.50']
    for i in range(0, number):
        c = 0
        product_n, quantity = map(int, input().split())
        for j in range(0, len(product_number)):
            if product_n == int(product_number[j]):
                total_price = total_price + quantity * (float(price_list[j]))
    return total_price
        

number = int(input())
if 1<=number<=5:
    return_value = MacPRONALTS(number)
    print(f'{return_value:.2f}')
