import sys 

class Statistiques:
    def __init__(self, tirs, buts, passes, contres, temps_de_jeu):
        self.tirs = tirs
        self.buts = buts
        self.passes = passes
        self.contres = contres
        self.temps_de_jeu = temps_de_jeu
        
    def infos_statistiques(self):
        print(f"Tirs : {self.tirs}")
        print(f"Buts : {self.buts}")
        print(f"Passes : {self.passes}")
        print(f"Contres : {self.contres}")
        print(f"Temps de jeu : {self.temps_de_jeu}")

if __name__ == "__main__":
    Statistiques01 = Statistiques(12,9,18,3,48)
    Statistiques01.infos_statistiques()