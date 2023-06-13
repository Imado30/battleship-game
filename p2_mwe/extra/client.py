#uvicorn server:rest_api --port 8000 --reload
import requests
from schiffeversenken import Schiffe

name=input("Gib deinen Namen ein: ")
r=requests.get("http://127.0.0.1:8000/lobby/%s" %name)

r_json=r.json()
my_id=r_json['user_id']
print(my_id)

print("Suche nach Spiel...")

# Queue
waiting=True
while waiting:
    resp=requests.get("http://127.0.0.1:8000/lobby")
    resp_json=resp.json()
    a=resp_json['q_size']

    if a==0:
        waiting=False
    
           
print("Spiel startet")

# Dieser Block dient zum Testen
re=requests.get("http://127.0.0.1:8000/spiele")
re_json=re.json()
spielesize=re_json['s_size']
print(spielesize)

# Game Id wird an Client übergeben
r=requests.get("http://127.0.0.1:8000/%s" %my_id)
r_json=r.json()
my_game_id=r_json['current_game']

# In Gid wird die Gegner ID gespeichert
print(my_game_id)
r = requests.get("http://127.0.0.1:8000/get_gid/%s" %my_id)
r_json= r.json()
gid = r_json["gid"]

#Schiffe werden platziert
s=Schiffe()
Schiffgrößen=[2]

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
    resp = requests.get("http://127.0.0.1:8000/postkoordinaten/%s/%s/%s/%s"%(my_game_id, my_id, x_koordinate, y_koordinate))
    requests.get("http://127.0.0.1:8000/t/%s/%s/%s"%(my_game_id, x_koordinate, y_koordinate))
    requests.get("http://127.0.0.1:8000/add_to_array/%s/%s/%s"%(my_id,x_koordinate,y_koordinate))
    rj=resp.json()
    print(rj['Status'])

    t=requests.get("http://127.0.0.1:8000/test/%s"%my_game_id)
    t_js=t.json()
    print("Koordinate:", t_js['test'])


resp=requests.get("http://127.0.0.1:8000/array_by_id/%s"%my_id)
resp_j=resp.json()
print(resp_j['size'])

"""
print("x-Wert ist:")
rr=requests.get("http://127.0.0.1:8000/getx/%s"%my_game_id)
rr_json=rr.json()
print(rr_json['x'])
"""

running=True
printed=False
gegner_print=False
while running:
    r=requests.get("http://127.0.0.1:8000/%s/turn" %my_game_id)
    r_json=r.json()
    turn=r_json['current_turn']

    if turn == my_id:
        gegner_print=False
        if not printed:
            print("Feuer frei!")
            printed=True
        
        x=input("Wähle x-Koordinate: ")
        while True:
            try:
                int_x=int(x)
                while int_x<0 or int_x>9:
                    x=input("Die x-Koordinate muss zwischen 0 und 9 liegen. Bitte wähle erneut: ")
                break
            except:
                x=input("Eingabe muss ein Integer Wert sein")

        y=input("Wähle y-Koordinate: ")
        while True:
            try:
                int_y=int(y)
                while int_y<0 or int_y>9:
                    y=input("Die y-Koordinate muss zwischen 0 und 9 liegen. Bitte wähle erneut: ")
                break

            except:
                y=input("Eingabe muss ein Integer Wert sein")


        r=requests.get("http://127.0.0.1:8000/shoot/%s/%s/%s"%(gid,x,y))
        r_json= r.json()
        
        if r_json['Hit']:
            print("Volltreffer!")

        else:
            print("leider daneben")
            #turn auf gegner ändern
        #requests an Koordinaten.size(), wenn 0, dann spiel vorbei
        

    else:
        if not gegner_print:
            print("Der Gegner ist am Zug")
            gegner_print=True
