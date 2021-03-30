x = int(input('Veuillez saisir un entier entre 1 et 10 : '))

if x < 1 or x > 10:
    while x < 1 or x > 10:
        x = int(input('Veuillez saisir un entier entre 1 et 10 : '))
    else: 
        print('x =', x)
else: 
    print('x =', x)