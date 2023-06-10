import requests
from schiffeversenken import Schiffe

s = Schiffe()
Schiffgrößen=[2,3,4,5,6]

while len(Schiffgrößen) != 0:

    print("Es stehen dir folgende Schiffgrößen zur Verfügung: ", Schiffgrößen, "\n" , "Gebe eine Schiffgröße ein")
    schiffgröße = int(input())
    if schiffgröße in Schiffgrößen:

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



        if richtung == "h":
            tupelarray = []
            for i in range(0,schiffgröße):
                tupel = ((int(x_koordinate)+i, int(y_koordinate)))
                tupelarray.append(tupel)

                for i in range(0,s.get_size()):
                    for j in tupelarray:

                        while j == s.get_tupel(i):
                            tupelarray.clear()

                            print("Du kannst das Schiff leider nicht platzieren, da das Schiff sonst ein anderes Schiff überschneidet. Gebe neue Koordinaten an", "\n")

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

                            for i in range(0,schiffgröße):
                                tupel = ((int(x_koordinate)+i, int(y_koordinate)))
                                tupelarray.append(tupel)

                                for i in range(0,s.get_size()):
                                    for j in tupelarray:
                                        
                                        if j == s.get_tupel(i):
                                            break
                            

            while (int(x_koordinate) + int(schiffgröße)) > 9:
                print("Du kannst das Schiff leider nicht horizontal platzieren, da das Schiff sonst das Spielfeld überschreitet. Gebe neue Koordinaten an", "\n")

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
            


        if richtung == "v":
            tupelarray = []
            for i in range(0,schiffgröße):
                tupel = (int(x_koordinate)+i, int(y_koordinate))
                tupelarray.append(tupel)

                for i in range(0,s.get_size()):
                    for j in tupelarray:
                        while j == s.get_tupel(i):
                            tupelarray.clear()
                            print("Du kannst das Schiff leider nicht platzieren, da das Schiff sonst ein anderes Schiff überschneidet. Gebe neue Koordinaten an", "\n")

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

                            for i in range(0,schiffgröße):
                                tupel = ((int(x_koordinate)+i, int(y_koordinate)))
                                tupelarray.append(tupel)

                                for i in range(0,s.get_size()):
                                    for j in tupelarray:
                                        
                                        if j == s.get_tupel(i):
                                            break


            while (int(y_koordinate) + int(schiffgröße)) > 9:
                print("Du kannst das Schiff leider nicht vertikal platzieren, da das Schiff sonst das Spielfeld überschreitet. Gebe neue Koordinaten an")

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

        Schiffgrößen.remove(schiffgröße)
        s.koordinaten_einfügen(schiffgröße, int(x_koordinate), int(y_koordinate), richtung)
        print(s.get_size())
        print(s.get_koordinaten())

    else:
        print("Element ist nicht in den Schiffgrößen. Wähle eine der folgenden Schiffgrößen", Schiffgrößen)


for i in s.get_koordinaten():
    x_koordinate = i[0]
    y_koordinate = i[1]
    resp = requests.get("http://127.0.0.1:8000/postkoordinaten/%s/%s"%(x_koordinate, y_koordinate))
