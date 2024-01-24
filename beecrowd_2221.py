def compitetion(test_cases):
    i = 0
    while i != test_cases:

        bonus = int(input())
        attack_dabriel, defense_dabriel, level_dabriel = map(int, input().split())
        attack_guarte, defense_guarte, level_guarte = map(int, input().split())

        if level_dabriel % 2 == 0:
            value_dabriel = ((attack_dabriel+defense_dabriel)/2) + bonus
        else:
            value_dabriel = ((attack_dabriel+defense_dabriel)/2)

        if level_guarte % 2 == 0:
            value_guarte = ((attack_guarte+defense_guarte)/2) + bonus
        else:
            value_guarte = ((attack_guarte+defense_guarte)/2)
        
        if value_dabriel > value_guarte:
            print('Dabriel')
        elif value_guarte > value_dabriel:
            print('Guarte')
        else:
            print('Empate')
        i += 1

#read input
test_cases = int(input())
compitetion(test_cases)