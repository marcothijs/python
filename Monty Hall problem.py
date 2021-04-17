import numpy as np
from random import randint
import matplotlib.pyplot as plt

class SimulatieBlijfBijKeuze:
    def __init__(self):
        pogingen = -1
        while(pogingen <1):
                pogingen = GeefInteger("Hoeveel pogingen? ")
                print("")
                print("Poging #      Prijs in   Gekozen   Resultaat     ")  
        self.pogingen = pogingen
        self.gemScores = []
        self.count = []
        
    def Simuleer(self):
        # Initialiseer score array
        scores = []
        # Loop over de gevraagde aantal pogingen
        for i in range(1,self.pogingen+1):
            print("Poging",str(i).ljust(4), end=": ")
            scores.append(self.Ronde())
            #Voeg data toe om grafiek te tonen
            self.gemScores.append(np.mean(scores))
            self.count.append(i)
        print("")
        print("Aantal keer gewonnen: ", sum(scores),"/",i)
        #print("scores = ",scores)
        #print("gemScores = ",self.gemScores)
        print("Gemiddelde score : ",np.mean(scores))
        

        #Toon graph met de resultaten
#        self.ToonResultaten()
                      
    def Ronde(self):
        # Kies de prijsDeur en de keuzeDeur
        prijsDeur = randint(1,3)
        keuzeDeur = randint(1,3)
        print("     ",prijsDeur,"      ",keuzeDeur, end=" -> ")
        
        # win als keuze de prijs bevat
        if prijsDeur == keuzeDeur:
            return 1
        else:
            return 0

#    def ToonResultaten(self):
        # Plot de pogingen op een x-as en de gemiddelde score op de y-as
#        plt.plot(self.count, self.gemScores)
#        plt.show()


class SimulatieVeranderKeuze(SimulatieBlijfBijKeuze):
     def Ronde(self):
        # Kies de prijsDeur en de keuzeDeur
        prijsDeur = ahll  randint(1,3)
        keuzeDeur = randint(1,3)
        print("    ",prijsDeur,"    ",keuzeDeur, end=" -> ")
        
        # Maak lijst met all mogelijke keuzes, verwijder de gekozen deur
        nieuweKeuzes = [1, 2, 3]
        nieuweKeuzes.remove(keuzeDeur)

        # Open een lege deur
        if nieuweKeuzes[0] == prijsDeur:
            del nieuweKeuzes[1]
        elif nieuweKeuzes[1] == prijsDeur:
            del nieuweKeuzes[0]
        else:
            del nieuweKeuzes[randint(0,1)]

        # Verander keuze van kandidaat
        keuzeDeur = nieuweKeuzes[0]
        print(keuzeDeur, end=": ")
        # Win als keuze juist is
        if prijsDeur == keuzeDeur:
            print("Gewonnen :-)")
            return 1
        else:
            print("Verloren :-(")
            return 0  


def GeefInteger(message):
    while True:
        try:
            keuze = int(input(message))
        except ValueError:
            print("Dit is geen geldige optie!")
            continue
        else:
            return keuze
                    
            

def Menu():
    print("")
    print("*********************************************")
    print(" Kies hoe je de simulatie wil laten lopen: ")
    print(" (1) Blijf bij je keuze")
    print(" (2) Wissel van deur")
    print(" (3) Eindig de simulatie")
    print("*********************************************")
    print("")


    # Definieer de mogelijke opties
    menuKeuzes = [1,2,3]


    # Neem menu input
    keuze = -1
    while(keuze not in menuKeuzes):
        keuze = GeefInteger("Geef je keuze in: ")
        if keuze not in menuKeuzes:
            print("Dit is geen geldige optie!")

    # Maak de juiste simulatie of verlaat het programma
    if keuze == 1:
        simulatie = SimulatieBlijfBijKeuze()
    elif keuze == 2:
        simulatie = SimulatieVeranderKeuze()
    elif keuze == 3:
        exit()
    
    # Simuleer het gekozen scenario
    simulatie.Simuleer()


    # Ga terug naar de menu
    Menu()

#if __name__ == "__main__":


print("")
print("************************************************")
print(" Welkom op de simulator van het 3 deuren")
print(" probleem, a.k.a. The Monty Hall Problem.")
print("************************************************")
print("")
detail = input(" Alle afzonderlijke pogingen weergeven? (y/n): ")
grafiek = input(" Grafiek tonen? (y/n): ")

Menu()
