def letters_index():
    while True:
  
        try:
            s = input()
            if s.isdigit():
               break
            index = 0
            letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            counter = 0
            updated_letters= letters.copy()
            for i in range(0, len(letters)):
                for j in range(0, len(letters)):
                    x = letters[i]+letters[j]
                    updated_letters.append(x)
            print(*updated_letters)
            print()
            for i in range(0, len(letters)):
                for j in range(0, len(letters)):
                    if counter == 1:
                        break
                    for k in range(0, len(letters)):
                        x = letters[i]+letters[j]+letters[k]
                        if x == 'XFD':
                            updated_letters.append(x)
                            counter = 1
                            break
                        else:
                            updated_letters.append(x)
            print(*updated_letters)
            for i in range(0, len(updated_letters)):
                if s == updated_letters[i]:
                    index = i+1
            if index >= 1:
                print(index)
            else:
                print("Essa coluna nao existe Tobias!")
        except EOFError:
            break

       
letters_index()