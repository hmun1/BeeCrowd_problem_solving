def resposta(test_cases):
    i = 1
    while i != test_cases+1:
        answer = int(input())
        print(f'resposta {i}: {answer}')
        i += 1


test_cases = int(input())
resposta(test_cases)