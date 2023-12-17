def offer(test_cases):
    i = 0
    exchange_bottle = 0
    while i != test_cases:
        soft_drinks, empty_bottles = map(int, input().split())
        exchange_bottle = (soft_drinks % empty_bottles) + (soft_drinks // empty_bottles)
        print(exchange_bottle)
        i += 1


test_cases = int(input())
if 1 <= test_cases <= 10000:
    offer(test_cases)