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

    def affecter_voiture(self, voiture):
        if self.voitureService is  not None:
            print("cet employe possede deja une voiture")
        elif voiture.chauffeur is not None:
            print("cette voiture est deja assigne a un autre employe")
        else:
            self.voitureService=voiture
            voiture.chauffeur= self
            print("voiture attribuee avec succes")

    def retirer_voiture(self):
        if self.voitureService is None:
            print("cet employe ne possede pas de voiture ")
        else:
            self.voitureService=None
            self.voitureService.chauffeur=None
            print("voiture retiree")



