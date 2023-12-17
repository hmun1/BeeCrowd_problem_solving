def cassava():
    total_gram = 0
    for i in range(0, 5):
        dona_chica = int(input())
        if i == 0:
            total_gram = total_gram + (dona_chica * 300)
        elif i == 1:
            total_gram = total_gram + (dona_chica * 1500)
        elif i == 2:
            total_gram = total_gram + (dona_chica * 600)
        elif i == 3:
            total_gram = total_gram + (dona_chica * 1000)
        elif i == 4:
            total_gram = total_gram + (dona_chica * 150)
    total_gram = total_gram + 225
    print(total_gram)

cassava()