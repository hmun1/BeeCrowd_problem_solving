def days(dwarves, distance):
    dwarves_and_man = dwarves + 2
    day = distance / dwarves_and_man
    print(f'{day:.2f}')


dwarves, distance = map(int, input().split())
days(dwarves, distance)