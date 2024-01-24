def album(total_stickers, sticker):
    total_card = set()
    j = 0
    while j != sticker:
        bought_sticker = int(input())
        total_card.add(bought_sticker)
        j += 1
    length = total_stickers - len(total_card)
    print(length)


total_stickers = int(input())
sticker = int(input())
album(total_stickers, sticker)
