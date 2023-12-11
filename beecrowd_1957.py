def converst_hexadecimal(decimal_number):
    if decimal_number == 0:
        return '0'
    
    numbers = '0123456789ABCDEF'
    result = ''

    while decimal_number > 0:
        reminder = decimal_number % 16
        result = numbers[reminder] + result
        decimal_number = decimal_number // 16
    return result

decimal_number = int(input())

decimal_to_hexadecimal = converst_hexadecimal(decimal_number)
print(f'{decimal_to_hexadecimal}')

