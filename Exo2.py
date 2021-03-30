import math
from easygui import *

#cour 2 exo 1

'''entre = float(input("Votre chiffre ?"))
if entre >= 0:
    print(math.sqrt(entre))
else:
    print("Erreur ton chiffre est négatif")'''

#cour 2 exo 2

'''mot1 = input('premier mot ? ')
mot2 = input('deuxieme mot ? ')
if mot1 < mot2:
    print(mot1)
elif mot2< mot1:
    print(mot2)
else:
    print('meme mot')

res = mot1 if mot1 < mot2 else mot2 if mot2<mot1 else "meme mot"
print(res)'''

#cour 2 exo 3

'''pSeuil = 2.3
vSeuil = 7.41
vol = float(input('Le volume ? '))
pression = float(input('La pression ? '))
if vol > vSeuil and pression > pSeuil:
    print('Shutdown')
if vol < vSeuil and pression > pSeuil:
    print('Volume up')
if vol > vSeuil and pression < pSeuil:
    print('Volume Down')
if vol < vSeuil and pression < pSeuil:
    print('Fine')'''

#cour 2 exo 4

'''a = 0
b = 10

while a < b:
    a += 1
    print(a)

while b != 0:
    b -= 1
    if b%2 != 0:
        print(b)'''

#cour 2 exo 5

'''filtre=[1,2,3,4,5,6,7,8,9,10]
entre = int(input("Votre nombre ? "))
if entre in filtre:
    print(entre)
else:
    print("Pas dans la liste")'''

#cour 2 exo 6

'''chaine = input('votre chaine de caractere : ')
liste = ["coucou","la","zone","cest","cool"]

for i in range(len(chaine)):
    print(chaine[i])

for y in range(len(liste)):
    print(liste[y])'''

#cour 2 exo 7
'''for i in range(15):
    if (i %3) == 0:
        print(i)'''

#cour 2 exo 8
'''for i in range(1,11):
    if i == 5:
        break
    print(i)'''


#cour 2 exo 9
'''for i in range(1,11):
    if i ==5:
        continue
    print(i)'''

#cour 2 exo 10
'''for i in range(-3,4):
    if i != 0:
        print(math.sin(i)/i)'''

#cour 2 exo 11
liste_entier = [12,28,91,52,34]
entre = integerbox('Entrez votre nombre : ')
sauv = []
flag = False
isPrime = False
for i in range(len(
liste_entier)):
    if entre in liste_entier:
        sauv.append(entre)
        msgbox('Vous avez ajouté un nouveau nombre' + str(sauv))
        break
    else:
        msgbox('Ce nombre nest pas dans la liste' )
entre2 = integerbox('Entrez votre deuxieme nombre : ')

while isPrime != True:
    if entre2 > 1:
        for i in range(2,entre2):
            if (entre2 % i) == 0:
                flag = True
                diviseur = i
                break
    isPrime = True

if flag:
    msgbox('Ce nest pas un nombre premier et son premier diviseur est ' + str(diviseur))
else:
    msgbox('Cest un nombre premier')
