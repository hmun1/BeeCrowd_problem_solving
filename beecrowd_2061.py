def browser_tab(x, y):
    current_tab = x
    for i in range(y):
        click = input()
        if click == 'fechou':
            current_tab += 1
        elif click == 'clicou':
            current_tab -= 1
    print(current_tab)
x, y = map(int, input().split())
browser_tab(x, y)
