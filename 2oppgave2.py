import random
import matplotlib.pyplot as plt
import numpy as np

class Terning:
    def __init__(self, antall_ganger):
        self.antall_ganger = antall_ganger
        self.liste_med_terningkast = []

    def trille_terning(self):
        self.liste_med_terningkast = np.random.randint(1,7,self.antall_ganger)
        print(type(list(self.liste_med_terningkast)))

    def utprint(self):
        plt.hist(self.liste_med_terningkast, [1,2,3,4,5,6,7],align = "left", rwidth=0.5)
        plt.show()

antall_ganger = int(input("Hvor mange ganger skal terningen trilles? "))
diagram = Terning(antall_ganger)
diagram.trille_terning()
diagram.utprint()