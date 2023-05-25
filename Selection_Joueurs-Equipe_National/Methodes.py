import sys 

class Methodes:
    
    def trier_par_nationalite(joueurs):
        return sorted(joueurs, key=lambda joueur: joueur.nationalite)
    
    def trier_IMC(joueurs):
        return sorted(joueurs, key=lambda joueur: joueur.calcul_IMC(), reverse=True)