#read input
test_cases = int(input())
sum_s1 = 0
sum_b1 = 0
sum_a1 = 0 
sum_s2 = 0
sum_b2 = 0
sum_a2 = 0

# read input for each test cases
i = 0
while i != test_cases:
    name = input()
    s1, b1, a1 = map(int, input().split())
    s2, b2, a2 =  map(int, input().split())
    sum_s1 = sum_s1 + s1
    sum_s2 = sum_s2 + s2
    sum_b1 = sum_b1 + b1
    sum_b2 = sum_b2 + b2
    sum_a1 = sum_a1 + a1
    sum_a2 = sum_a2 + a2
    i += 1
percentage_service = (sum_s2 / sum_s1) * 100
percentage_block = (sum_b2 / sum_b1) * 100
percentage_attack = (sum_a2 / sum_a1) * 100
print(f'Pontos de Saque: {percentage_service:.2f} %.')
print(f'Pontos de Bloqueio: {percentage_block:.2f} %.')
print(f'Pontos de Ataque: {percentage_attack:.2f} %.')

