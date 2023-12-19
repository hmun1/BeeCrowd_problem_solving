def earth_safety(human, elves, dwarves, orcs, wargs, eagles):
    good_side = human + elves + dwarves + eagles
    bad_side = orcs + wargs
    if good_side > bad_side:
        print('Middle-earth is safe.')
    else:
        print('Sauron has returned.')
human, elves, dwarves, orcs, wargs, eagles = map(int, input().split())
earth_safety(human, elves, dwarves, orcs, wargs, eagles)