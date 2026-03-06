#creation de la classe Employer ainsi que ses attributs
class Employe:
    def __init__(self, numeroPermis, Nom, Prenom):
        self.numeroPermis = numeroPermis
        self.Nom = Nom
        self.Prenom = Prenom
        self.voitureService=None
