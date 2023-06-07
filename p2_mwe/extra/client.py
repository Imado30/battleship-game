import requests

name=input("Gib deinen Namen ein: ")
r=requests.get("http://127.0.0.1:8000/lobby/%s" %name)

r_json=r.json()
print(r.text)

my_id=r_json['user_id']

print("Geduld")

waiting=True
while waiting:
    resp=requests.get("http://127.0.0.1:8000/lobby")
    resp_json=resp.json()
    a=resp_json['player1']
    if a!=my_id:
        waiting=False
        print("Spiel startet")    

Schiffgrößen=[1,2,3,4,5]


"""
running=True

while running:
    if requests.get("http://127.0.0.1:8000/turn") == my_id:
        x=input
        y=input
        requests.get("http://127.0.0.1:8000/shoot/{x}/{y}")
        #requests an Koordinaten.size(), wenn 0, dann spiel vorbei
        
"""