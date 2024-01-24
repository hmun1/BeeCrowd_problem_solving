def elivator_test(floor, start, goal, up, down):
    pushes = 2 # for starting the elevator 1st push, and push 2 is pushing the floor button
    if start < goal:
        start = up
        while start < goal:
            if start > goal:
                break
            else:
                start = start + up
                pushes = pushes + 1
        print(pushes)
    else:
        print('use the stairs')

floor, start, goal, up, down = map(int, input().split())
if (goal <= floor<= 1000000 and 1 <= start) and (0 <= up and down <= 1000000):
    elivator_test(floor, start, goal, up, down)