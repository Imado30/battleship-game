import requests

name=input("Gib deinen Namen ein: ")
r=requests.get("http://127.0.0.1:8000/lobby/%s" %name)

r_json=r.json()
my_id=r_json['user_id']

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
Schiffgrößen=[1,2,3,4,5]

# Dieser Block dient zum Testen
re=requests.get("http://127.0.0.1:8000/spiele")
re_json=re.json()
spielesize=re_json['s_size']
print(spielesize)

# Game Id wird an Client übergeben
r=requests.get("http://127.0.0.1:8000/%s" %my_id)
r_json=r.json()
my_game_id=r_json['current_game']

print(my_game_id)



running=True
printed=False
while running:
    r=requests.get("http://127.0.0.1:8000/%s/turn" %my_game_id)
    r_json=r.json()
    turn=r_json['current_turn']

    if turn == my_id:
        if not printed:
            print("Feuer frei!")
            printed=True
        """
        x=input
        y=input
        requests.get("http://127.0.0.1:8000/shoot/{x}/{y}")
        #requests an Koordinaten.size(), wenn 0, dann spiel vorbei
        """
