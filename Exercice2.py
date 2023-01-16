# Emilie Mancera
# 404

import random

a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)
d = random.randint(1,6)

def lancer_des():
    if a > b:
        eject = b
        if b > c:
            eject = c
            if c > d:
                eject = d
                if d > a:
                    eject = a

class NPC: # Création de la classe NPC
    def __int__(self):
        self.force = lancer_des()
        self.agilite = lancer_des()
        self.constitution = lancer_des()
        self.intelligence = lancer_des()
        self.sagesse = lancer_des()
        self.charisme = lancer_des() # Donner les attributs à la classe NPC