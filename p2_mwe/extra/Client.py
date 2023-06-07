import requests
from schiffeversenken import Schiffe

#r = requests.get("http://127.0.0.1:8000/")

s = Schiffe()
Schiffgrößen=[2,3,4,5,6]

while len(Schiffgrößen) != 0:

    print("Es stehen dir folgende Schiffgrößen zur Verfügung: ", Schiffgrößen, "\n" , "Gebe eine Schiffgröe ein")
    schiffgröße = int(input())
    if schiffgröße in Schiffgrößen:

        print("Gebe die x-Koordinate an für die Schiffgröße: ", schiffgröße)
        x_koordinate = int(input())
        while x_koordinate < 0 or x_koordinate > 9:
            print("Das eingegebene Element ist keine Zahl von 1 - 9. Gebe eine Zahl an von 1 - 9")
            x_koordinate = int(input())

        print("Gebe die y-Koordinate an für die Schiffgröße: ", schiffgröße)
        y_koordinate = int(input())
        while y_koordinate < 0 or y_koordinate > 9:
            print("Das eingegebene Element ist keine Zahl von 1 - 9. Gebe eine Zahl an von 1 - 9")
            y_koordinate = int(input())

        print("Gebe v (vertikal) oder h (horizontal) für die Richtung der Schiffgröße: ", schiffgröße, " an")
        richtung = input()
        while richtung != "v" and richtung != "h":
            print("Das eingegebene Element ist weder v (vertikal) noch h (horizontal). Gebe entweder v oder h ein")
            richtung = input()


        if richtung == "h":
            while (x_koordinate + schiffgröße) > 9:
                print("Du kannst das Schiff leider nicht horizontal platzieren, da das Schiff sonst das Spielfeld überschreitet. Gebe neue Koordinaten an", "\n")

                print("Gebe die x-Koordinate an für die Schiffgröße: ", schiffgröße)
                x_koordinate = int(input())
                while x_koordinate < 0 or x_koordinate > 9:
                    print("Das eingegebene Element ist keine Zahl von 1 - 9. Gebe eine Zahl an von 1 - 9")
                    x_koordinate = int(input())


                print("Gebe die y-Koordinate an für die Schiffgröße: ", schiffgröße)
                y_koordinate = int(input())
                while y_koordinate < 0 or y_koordinate > 9:
                    print("Das eingegebene Element ist keine Zahl von 1 - 9. Gebe eine Zahl an von 1 - 9")
                    y_koordinate = int(input())

                print("Gebe v (vertikal) oder h (horizontal) für die Richtung der Schiffgröße: ", schiffgröße, " an")
                richtung = input()
                while richtung != "v" and richtung != "h":
                    print("Das eingegebene Element ist weder v (vertikal) noch h (horizontal). Gebe entweder v oder h ein")
                    richtung = input()


        if richtung == "v":
            while (y_koordinate + schiffgröße) > 9:
                print("Du kannst das Schiff leider nicht vertikal platzieren, da das Schiff sonst das Spielfeld überschreitet. Gebe neue Koordinaten an")


                print("Gebe die x-Koordinate an für die Schiffgröße: ", schiffgröße)
                x_koordinate = int(input())
                while x_koordinate < 0 or x_koordinate > 9:
                    print("Das eingegebene Element ist keine Zahl von 1 - 9. Gebe eine Zahl an von 1 - 9")
                    x_koordinate = int(input())


                print("Gebe die y-Koordinate an für die Schiffgröße: ", schiffgröße)
                y_koordinate = int(input())
                while y_koordinate < 0 or y_koordinate > 9:
                    print("Das eingegebene Element ist keine Zahl von 1 - 9. Gebe eine Zahl an von 1 - 9")
                    y_koordinate = int(input())

                print("Gebe v (vertikal) oder h (horizontal) für die Richtung der Schiffgröße: ", schiffgröße, " an")
                richtung = input()
                while richtung != "v" and richtung != "h":
                    print("Das eingegebene Element ist weder v (vertikal) noch h (horizontal). Gebe entweder v oder h ein")
                    richtung = input()

        Schiffgrößen.remove(schiffgröße)

        resp = requests.get("http://127.0.0.1:8000/schiffe")
        resp_json = resp.json()

    else:
        print("Element ist nicht in den Schiffgrößen. Wähle eine der folgenden Schiffgrößen", Schiffgrößen)
