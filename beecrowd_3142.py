def letters_index():
    letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    while True:
        try:
            s = input()
            if s.isdigit():
                break

            index = letters.index(s) + 1 if s in letters else 0

            if index >= 1:
                print(index)
            else:
                print("Essa coluna nao existe Tobias!")

        except EOFError:
            break

letters_index()
