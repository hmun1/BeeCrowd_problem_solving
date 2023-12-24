def arabic_to_roman(n):
    # Define the Roman numeral symbols and their corresponding values
    roman_symbols = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    # Initialize an empty string to store the Roman numeral representation
    roman_numeral = ''

    # Iterate through the symbols and append the corresponding Roman numeral to the result
    for value, symbol in roman_symbols.items():
        while n >= value:
            roman_numeral += symbol
            n -= value

    return roman_numeral

# Read input
n = int(input())

# Check if the input is within the valid range
if 0 < n < 1000:
    # Convert the Arabic number to Roman numerals and print the result
    result = arabic_to_roman(n)
    print(result)
else:
    print("Invalid input. Please enter a positive integer between 1 and 999.")
