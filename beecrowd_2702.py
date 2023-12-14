chicken_a, beef_a, pasta_a = map(int, input().split())
chicken_r, beef_r, pasta_r = map(int, input().split())
chicken = 0
beef = 0
pasta = 0
if chicken_a < chicken_r:
    chicken = chicken_r - chicken_a
if beef_a < beef_r:
    beef = beef_r - beef_a
if pasta_a < pasta_r:
    pasta = pasta_r - pasta_a
total = chicken + beef + pasta
print(total)

    