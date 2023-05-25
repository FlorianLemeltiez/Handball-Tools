import sys 

class Joueurs:
    def __init__(self, nom, poste, age, nationalite, taille, poid, tir, passe ):
        self.nom = nom
        self.poste = poste
        self.age = age
        self.nationalite = nationalite
        self.taille = taille
        self.poid = poid
        self.tir = tir
        self.passe = passe
        
    def infos_joueur(self):
        print(f"Nom : {self.nom}")
        print(f"Poste : {self.poste}")
        print(f"Age : {self.age}")
        print(f"Nationalite : {self.nationalite}")
        print(f"Taille : {self.taille}")
        print(f"Poid : {self.poid}")
        print(f"Tirs : {self.tir}")
        print(f"Passes : {self.passe}")
        
    def calcul_IMC(self):
        imc = self.poid / (self.taille ** 2)
        return imc
    
    def majeur(self):
        if self.age >= 18:
            return True
        else:
            return False
    
    def nom_et_nationalite(self):
        print(f"- {self.nationalite} : {self.nom}")
        


if __name__ == "__main__":
    Joueur01 = Joueurs("Florian", "Pivot", 24, "Francaise", 1.94, 89, "88/100", "98/100")
    Joueur02 = Joueurs("Raouf", "Arriere", 24, "Algerien", 1.94, 89, "88/100", "98/100")
    Joueur03 = Joueurs("Erwann", "Ailier", 24, "Kabile", 1.94, 89, "88/100", "98/100")
    Joueur04 = Joueurs("Capucin", "Gardien", 24, "Francaise", 1.94, 89, "88/100", "98/100")
    Joueur01.infos_joueur()
    print(Joueur01.majeur())
    print(Joueur01.calcul_IMC())