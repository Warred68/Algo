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