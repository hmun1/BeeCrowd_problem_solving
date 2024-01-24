def palavrao_or_not(message):
    if length >= 10:
        print('palavrao')
    else:
        print('palavrinha')

message = input()
length = len(message)
if length < 20:
    palavrao_or_not(message)