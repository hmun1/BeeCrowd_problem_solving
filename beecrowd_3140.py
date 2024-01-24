import sys

inside_body = False

for line in sys.stdin:
    line = line.strip()

    if line == '<body>' and line == '</body>':
        inside_body = True
    elif inside_body:
        print(line, end='')  # Remove the newline after printing each line

# Add an extra newline at the end if required
print()