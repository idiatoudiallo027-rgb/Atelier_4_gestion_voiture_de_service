#creation de la classe Employer ainsi que ses attributs
class Employe:
    def __init__(self, numeroPermis, Nom, Prenom):
        self.numeroPermis = numeroPermis
        self.Nom = Nom
        self.Prenom = Prenom
        self.voitureService=None

#implementer les methodes de la classe employer(afficher, affecter et retirer)
    def afficher_informations(self):
        print(f"employe: {self.numeroPermis},{self.Nom},{self.Prenom}")
        if self.voitureService is None:
            print("aucune voiture de service attribuee")
        else:
            print("voiture service")
            self.voitureService.afficher_informations()

