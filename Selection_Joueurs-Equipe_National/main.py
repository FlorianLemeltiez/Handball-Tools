import sys

from Joueurs import Joueurs
from Methodes import Methodes

if __name__ == "__main__":
    Joueur01 = Joueurs("Florian", "Pivot", "24", "France", 1.94, 89, "88/100", "98/100")
    Joueur02 = Joueurs("Raouf", "Ailier", "22", "Algerie", 1.81, 72, "90/100", "85/100")
    Joueur03 = Joueurs("Erwan", "Arriere", "26", "Espagne", 1.87, 95, "75/100", "95/100")
    Joueur04 = Joueurs("Saadi", "Gardien", "31", "Algerie", 1.91, 84, "10/100", "70/100")
    
    liste_joueurs = [Joueur01, Joueur02, Joueur03, Joueur04]
   
    
    print("+------------------------------------+\n|  Trie des joueurs par nationalite  |\n+------------------------------------+")
    
    joueurs_tries = Methodes.trier_par_nationalite(liste_joueurs)
    
    for joueur in joueurs_tries:
        joueur.nom_et_nationalite()    
     
        
    print("\n+----------------------------+\n|  Trie des joueurs par IMC  |\n+----------------------------+")
    
    tries_IMC = Methodes.trier_IMC(liste_joueurs)
    
    for joueur in tries_IMC:
        print("-", joueur.nom, " : ", joueur.calcul_IMC())
     
    