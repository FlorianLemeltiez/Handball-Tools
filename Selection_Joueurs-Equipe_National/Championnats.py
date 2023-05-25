import sys 

class Championnats:
    def __init__(self, pays, divisions, nbr_equipes):
        self.pays = pays
        self.divisions = divisions
        self.nbr_equipes = nbr_equipes
        
    def infos_championnats(self):
        print(f"Pays : {self.pays}")
        print(f"Divisions : {self.divisions}")
        print(f"Nombres d'equipes : {self.nbr_equipes}")

if __name__ == "__main__":
    Championnat01 = Championnats("France", "Pre-nationale", 12)
    Championnat01.infos_championnats()