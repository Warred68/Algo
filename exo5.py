pSeuil = 2.3
vSeuil = 7.41

p = float(input('Saisissez la pression actuelle : '))
v = float(input('Saisissez le volume actuel : '))

if v > vSeuil and p > pSeuil:
    print('Arrêt immédiat')
elif v > vSeuil and p < pSeuil:
    print('Diminuez le volume')
elif v < vSeuil and p > pSeuil:
    print('Augmentez le volume')
else:
    print('Eveything ok')