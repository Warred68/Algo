#1-1
t = 6.892
d = 19.7

v = d/t
print('la vitesse =', round(v,1)) 

#1-2
nom = input('Votre nom : ')
age = int(input('Votre age : '))

print(nom, 'a', age, 'ans.')

#2-1
from math import *

x = float(input('Un chiffre : '))

if x >= 0: 
    print(sqrt(x))
else:
    print('Votre chiffre est négatif.')

#2-2
mot1 = input('Un mot : ')
mot2 = input('Un autre mot : ')

if len(mot1) > len(mot2):
    print('Le mot le plus court est :', mot2)
else: 
    print('Le mot le plus court est :', mot1)

#2-3    
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

#2-4
a = 0
b = 10

while b != 0:
    a += 1
    b -= 1
    while a < b: 
        print('a=', a)
        break
    if b%2 != 0:
        print('b=', b)

#2-5
x = int(input('Veuillez saisir un entier entre 1 et 10 : '))

if x < 1 or x > 10:
    while x < 1 or x > 10:
        x = int(input('Veuillez saisir un entier entre 1 et 10 : '))
    else: 
        print('x =', x)
else: 
    print('x =', x)

#2-6
mot = input('Un mot : ')
lst = []
n = int(input('Nb pour la liste : '))

for i in range(0,n): 
    ele = input('Pour la liste : ')
    lst.append(ele)

for i in range (0,len(mot)):
    print(mot[i])

for i in range (0, len(lst)):
    print(lst[i])

#2-7
for i in range(1,15,3):
    print(i)
