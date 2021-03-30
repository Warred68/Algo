mot1 = input('Un mot : ')
mot2 = input('Un autre mot : ')

if len(mot1) > len(mot2):
    print('Le mot le plus court est :', mot2)
else: 
    print('Le mot le plus court est :', mot1)