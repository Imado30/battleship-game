import requests

r=requests.get("http://127.0.0.1:8000/lobby/Christoph")

print(r.text)

my_id=r["user_id"]


waiting=True
while waiting:
    q=requests.get("http://127.0.0.1:8000/lobby")
    a=q.text()["player1"]
    print("geduld")
    if a!=my_id:
        waiting=False
        print("Spiel startet")    

SChiffgrößen=[1,2,3,4,5]



running=True

while running:
    if requests.get("http://127.0.0.1:8000/turn") == my_id:
        x=input
        y=input
        requests.get("http://127.0.0.1:8000/shoot/x/y")