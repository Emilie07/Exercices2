# Emilie Mancera
# 404

import random # On amène la librairie random

a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)
d = random.randint(1,6)

def d12():
    random.randint(1,12) # On créé un dé à 12 faces

def d20():
    random.randint(1,20) # On créé un dé à 20 faces

def d6():
    random.randint(1,6) # On créé un dé à 6 faces

def lancer_des():
    if a > b:
        eject = b
        if b > c:
            eject = c
            if c > d:
                eject = d
                if d > a:
                    eject = a # On roule 4 dés à 6 faces et on retire la valeur la plus petite


class NPC: # Création de la classe NPC
    def __init__(self):
        self.force = lancer_des()
        self.agilite = lancer_des()
        self.constitution = lancer_des()
        self.intelligence = lancer_des()
        self.sagesse = lancer_des()
        self.charisme = lancer_des() # On donne les attributs à la classe NPC

        self.classarmure = d12()
        self.pdv = d20() # On roule les dés pour déterminer la valeur des attributs

        self.nom = " "
        self.race = " "
        self.espece = " "
        print(self)
        class Kobold(NPC): # Création de la classe Kobold qui hérite des attributs de NPC
            def __init__(self):
                super().__init__() # On donne les attributs de classe(NPC) à classe(Kobold)
                self.subir_dommage = d6() # On roue le dé à 6 faces pour déterminer la valeur de l'attribut

        class Hero(NPC): # Création de la classe Héro qui hérite des attributs de NPC
            def __init__(self):
                super().__init__() # On donne les attributs de classe(NPC) à classe(Héro)
                self.subir_dommage = d6() # On roue le dé à 6 faces pour déterminer la valeur de l'attribut