import sys 
             
class Salles:
    def __init__(self, nom, pays, villes, equipes, capacites):
        self.nom = nom
        self.pays = pays
        self.villes = villes
        self.equipes = equipes
        self.capacites = capacites
        
    def infos_salles(self):
        print(f"Nom : {self.nom}")
        print(f"Pays : {self.pays}")
        print(f"Ville : {self.villes}")
        print(f"Equipe : {self.equipes}")
        print(f"Capacites : {self.capacites}")
        
if __name__ == "__main__":
    Salle01 = Salles("Rousseau", "France", "Malakoff", "USMM Handball", 2500)
    Salle01.infos_salles()
