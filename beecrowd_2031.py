def rock_paper_scrissor(test_case):
    i = 0
    while i != test_case:
        player_1 = input()
        player_2 = input()
        if (player_1 == 'ataque' and player_2 == 'pedra'):
            print('Jogador 1 venceu')
        elif (player_1 == 'pedra' and player_2 == 'ataque'):
            print('Jogador 2 venceu')
        elif (player_1 == 'pedra' and player_2 == 'papel'):
            print('Jogador 1 venceu')
        elif player_1 == 'ataque' and player_2 == 'papel':
            print('Jogador 1 venceu')
        elif (player_1 == 'papel' and player_2 == 'pedra') :
            print('Jogador 2 venceu')
        elif (player_1 == 'papel' and player_2 == 'ataque'):
            print('Jogador 2 venceu')
        elif (player_1 == 'papel' and player_2 == 'papel'):
            print('Ambos venceram')
        elif (player_1 == 'pedra' and player_2 == 'pedra'):
            print('Sem ganhador')
        elif (player_1 == 'ataque' and player_2 == 'ataque'):
            print('Aniquilacao mutua')
        i += 1


#read input
test_case = int(input())
rock_paper_scrissor(test_case)