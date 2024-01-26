#read input

flag = 0
while True:
    total_vitamin = 0
    
    test_cases = int(input())
    if test_cases == 0:
        flag = 1
    else:
        i = 0
        while i != test_cases:
            food = input().split()
            quantity = int(food[0])
            food.remove(food[0])
            name = ' '.join(food)
            vitamin = 0
            if name == "suco de laranja":
                vitamin = vitamin +(quantity * 120)

            elif name == "morango fresco":
                vitamin = vitamin +(quantity * 85)

            elif name == "mamao":
                vitamin = vitamin +(quantity * 85)

            elif name == "goiaba vermelha":
                vitamin = vitamin +(quantity * 70)

            elif name == "manga":
                vitamin = vitamin +(quantity * 56)

            elif name == "laranja":
                vitamin = vitamin +(quantity * 50)

            elif name == "brocolis":
                vitamin = vitamin +(quantity * 34)

            total_vitamin = total_vitamin + vitamin
            i += 1
            

        if total_vitamin > 130:
            print(f'Menos {total_vitamin - 130} mg')
        elif total_vitamin < 110:
            print(f'Mais {110 - total_vitamin} mg')
        else:
            print(f'{total_vitamin} mg')
        
    if flag == 1:
        break
        
    





