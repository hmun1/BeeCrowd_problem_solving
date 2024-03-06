def bazinga(raj, sheldon, counter):
    if (raj == 'tesoura' and sheldon == 'papel') or (raj == 'papel' and sheldon == 'pedra') or (raj == 'pedra' and sheldon == 'lagarto') or  (raj == 'lagarto' and sheldon == 'Spock') or (raj == 'Spock' and sheldon =='tesoura') or (raj == 'tesoura' and sheldon =='lagarto') or (raj == 'lagarto' and sheldon =='papel') or (raj == 'papel' and sheldon =='Spock') or (raj == 'Spock' and sheldon =='pedra') or (raj == 'pedra' and sheldon =='tesoura'):
        print(f'Caso #{counter}: Bazinga!')
    elif raj == sheldon:
        print(f'Caso #{counter}: De novo!')
    else:
        print(f'Caso #{counter}: Raj trapaceou!')

    
#read input
t_cases = int(input())
counter = 0
i = 0
while i != t_cases:
    raj, sheldon = input().split()
    counter += 1
    bazinga(raj, sheldon, counter)
    i += 1