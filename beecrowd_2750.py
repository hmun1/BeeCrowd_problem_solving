# Function to print a formatted line
def print_line():
    print('-' * 39)


# Function to print table headers
def print_headers():
    print_line()
    print('| decimal   |  octal  |  Hexadecimal  |')
    print_line()

# Print the second set of headers
print_headers()

# Function to print values in different bases for a given variable
for i in range(16):
    decimal_value = i
    octal_value = f"{i:o}"
    hexadecimal_value = f"{i:X}"
    
    # Adjust spacing for the first column
    print(f"|{decimal_value: ^11}|{octal_value: ^8} |{hexadecimal_value: ^15}|")
print_line()