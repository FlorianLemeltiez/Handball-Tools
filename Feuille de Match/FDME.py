# Header Files

import sys 

valeur = 0
compteur = 0

nbr_but = 0
nbr_tir = 0
nbr_arret = 0
victoire = 1
defaite = 0

joueur = 12
officiel = 5

equipe_A = input("Veuillez inscrire le nom de l'equipe A : ")
print( equipe_A)

equipe_B = input("Veuillez inscrire le nom de l'equipe B : ")
print( equipe_B)


print("Veuillez saisir la liste de vos joueurs  \n")

while True :
    valeur = input("Joueur : ")
    print(valeur)
    compteur += 1
    
    if compteur > 2 or valeur == '' :
        break
