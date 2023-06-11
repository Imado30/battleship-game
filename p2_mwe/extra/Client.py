# uvicorn Server:rest_api --port 8000 --reload
# cmake -S . -B build && cmake --build build && cmake --install build
# python3 -m uvicorn Server:rest_api --port 8000 --reload

import requests
from schiffeversenken import Schiffe

s = Schiffe()
Schiffgrößen=[2,3,4,5,6]


def eingaben_loop(schiffgröße : int) -> list:
    print("Gebe die x-Koordinate an für die Schiffgröße: ", schiffgröße)
    x_koordinate = input()
    while True:
        try:
            while int(x_koordinate) < 0 or int(x_koordinate) > 9:
                print("Das eingegebene Element ist keine Zahl von 1 - 9. Gebe eine Zahl an von 1 - 9")
                x_koordinate = int(input())
            break
        except:
            x_koordinate = input("Es wurde kein Integer Wert übergeben. Gebe eine Zahl von 1 - 9 an! \n")

    print("Gebe die y-Koordinate an für die Schiffgröße: ", schiffgröße)
    y_koordinate = input()
    while True:
        try:
            while int(y_koordinate) < 0 or int(y_koordinate) > 9:
                print("Das eingegebene Element ist keine Zahl von 1 - 9. Gebe eine Zahl an von 1 - 9")
                y_koordinate = int(input())
            break
        except:
            y_koordinate = input("Es wurde kein Integer Wert übergeben. Gebe eine Zahl von 1 - 9 an! \n")

    print("Gebe v (vertikal) oder h (horizontal) für die Richtung der Schiffgröße: ", schiffgröße, " an")
    richtung = input()
    while richtung != "v" and richtung != "h":
        print("Das eingegebene Element ist weder v (vertikal) noch h (horizontal). Gebe entweder v oder h ein")
        richtung = input()

    eingaben = [x_koordinate, y_koordinate, richtung]
    return eingaben



def eingabe_überprüfen(schiffgröße : int, x_koordinate : int, y_koordinate : int, richtung : str) -> list:
    tupelarray = []

    if richtung == "h":
        for i in range(0,schiffgröße):
            tupel = (int(x_koordinate) + i, int(y_koordinate))
            tupelarray.append(tupel)
            for i in range(0,s.get_size()):
                for j in tupelarray:

                    if j == s.get_tupel(i):

                        tupelarray.clear()
                        print("Du kannst das Schiff leider nicht platzieren, da das Schiff sonst ein anderes Schiff überschneidet. Gebe neue Koordinaten an \n")
                        ergebnis_eingaben = eingaben_loop(schiffgröße)
                        x_koordinate1 = ergebnis_eingaben[0]
                        y_koordinate1 = ergebnis_eingaben[1]
                        richtung1 = ergebnis_eingaben[2]
                        return eingabe_überprüfen(schiffgröße, x_koordinate1, y_koordinate1, richtung1)
                        
                        
        if (int(x_koordinate) + int(schiffgröße)) > 9:
            print("Du kannst das Schiff leider nicht horizontal platzieren, da das Schiff sonst das Spielfeld überschreitet. Gebe neue Koordinaten an", "\n")
            ergebnis_eingaben = eingaben_loop(schiffgröße)
            x_koordinate2 = ergebnis_eingaben[0]
            y_koordinate2 = ergebnis_eingaben[1]
            richtung2 = ergebnis_eingaben[2]
            return eingabe_überprüfen(schiffgröße, x_koordinate2, y_koordinate2, richtung2)

        

    if richtung == "v":
        for i in range(0,schiffgröße):
            tupel = (int(x_koordinate)+i, int(y_koordinate))
            tupelarray.append(tupel)

            for i in range(0,s.get_size()):
                for j in tupelarray:

                    if j == s.get_tupel(i):

                        tupelarray.clear()
                        print("Du kannst das Schiff leider nicht platzieren, da das Schiff sonst ein anderes Schiff überschneidet. Gebe neue Koordinaten an", "\n")
                        ergebnis_eingaben = eingaben_loop(schiffgröße)
                        x_koordinate3 = ergebnis_eingaben[0]
                        y_koordinate3 = ergebnis_eingaben[1]
                        richtung3 = ergebnis_eingaben[2]
                        return eingabe_überprüfen(schiffgröße, x_koordinate3, y_koordinate3, richtung3)


        if (int(y_koordinate) + int(schiffgröße)) > 9:
            print("Du kannst das Schiff leider nicht vertikal platzieren, da das Schiff sonst das Spielfeld überschreitet. Gebe neue Koordinaten an")
            ergebnis_eingaben = eingaben_loop(schiffgröße)
            x_koordinate4 = ergebnis_eingaben[0]
            y_koordinate4 = ergebnis_eingaben[1]
            richtung4 = ergebnis_eingaben[2]
            return eingabe_überprüfen(schiffgröße, x_koordinate4, y_koordinate4, richtung4)


    meine_Liste = [int(x_koordinate), int(y_koordinate), richtung]
    return meine_Liste



while len(Schiffgrößen) != 0:

    print("Es stehen dir folgende Schiffgrößen zur Verfügung: ", Schiffgrößen, "                 'reset' = Schiffe neu anordnen \n" , "Gebe eine Schiffgröße ein")
    schiffgröße = input()

    while True:
        try: 
            if schiffgröße == "reset":
                Schiffgrößen.clear()
                s.koordinaten_löschen()
                Schiffgrößen = [2,3,4,5,6]
                print("Du kannst deine Schiffe nun nochmal neu anordnen")
                break

            if int(schiffgröße) in Schiffgrößen:

                ergebnis_eingaben = eingaben_loop(int(schiffgröße))
                x_koordinate_er = ergebnis_eingaben[0]
                y_koordinate_er = ergebnis_eingaben[1]
                richtung_er = ergebnis_eingaben[2]

                ergebnis = eingabe_überprüfen(int(schiffgröße), x_koordinate_er, y_koordinate_er, richtung_er)
                x_koordinate = ergebnis[0]
                y_koordinate = ergebnis[1]
                richtung = ergebnis[2]

                Schiffgrößen.remove(int(schiffgröße))
                s.koordinaten_einfügen(int(schiffgröße), int(x_koordinate), int(y_koordinate), richtung)
                print(s.get_size())
                print(s.get_koordinaten())
            break

        except:
            print("Element ist nicht in den Schiffgrößen. Wähle eine der folgenden Schiffgrößen", Schiffgrößen, "\n")
            schiffgröße = input()
        


for i in s.get_koordinaten():
    x_koordinate = i[0]
    y_koordinate = i[1]
    resp = requests.get("http://127.0.0.1:8000/postkoordinaten/%s/%s"%(x_koordinate, y_koordinate))