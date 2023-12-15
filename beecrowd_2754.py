def scienctific_notation(x, y):
    print(f'{x:.6f} - {y:.6f}')
    print(f'{x:.0f} - {y:.0f}')
    print(f'{x:.1f} - {y:.1f}')
    print(f'{x:.2f} - {y:.2f}')
    print(f'{x:.3f} - {y:.3f}')
    print(f'{x:.6e} - {y:.6e}')
    print(f'{x:.6E} - {y:.6E}')
    print(f'{x:.3f} - {y:.3f}')
    print(f'{x:.3f} - {y:.3f}')

# Read input
x, y = 234.345, 45.698
scienctific_notation(x, y)
