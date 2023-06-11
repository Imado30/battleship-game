from fastapi import FastAPI

try:
    import schiffeversenken
except ImportError as e:
  print(f"Importing the shared library 'schiffeversenken' did not work.")
  print(f"Is (a link to) the shared library 'schiffeversenken.____.so' in the same directory as this python script?")
  print(f"The import caused the following exception '{e}'")
  print(f"Exiting")
  exit(1)

from schiffeversenken import Lobby,Schiffe
import os
from fastapi import FastAPI
import uvicorn

from typing import List,Tuple

#cmake -S . -B build && cmake --build build && cmake --install build

lob = Lobby()

rest_api= FastAPI()

@rest_api.get("/")
async def wurzel_pfad():
    return{"coole_nachricht" : "Fast API funktioniert"}


@rest_api.get("/user/{uid}")
async def get_user_by_id(uid: int):
    return{"user_id" : uid}

@rest_api.get("/lobby/{name}")
async def create_player(name: str):
    return{"user_id" : lob.spieler_erstellen(name).get_id()}

@rest_api.get("/lobby")
async def get_queue():
    return{"q_size" : lob.queue_size()}

@rest_api.get("/spiele")
async def spiele_size():
    return{"s_size" : lob.spiele_size()}

@rest_api.get("/{id}")
async def get_in_game(id: int):
    return{"current_game" : lob.player_by_id(id).get_in_game()}


@rest_api.get("/{game}/turn")
async def get_turn(game: int):
    return{"current_turn": lob.game_by_id(game).get_turn()} 

@rest_api.get("/{game}/shoot/{x}/{y}")
async def shoot(game: int, x: int, y: int):
    spiel=lob.game_by_id(game)
    s1=spiel.get_p1()
    s2=spiel.get_p2()

    if spiel.get_turn()==s1.get_id():
        return{"hit": s2.get_ship().hit(x,y)}
        
    else:
        return{"hit": s2.get_ship().hit(x,y)}

@rest_api.get("/{sid}/postkoordinaten/{x}/{y}")
async def post_koordinaten(sid: int, x : int, y : int):
    lob.player_by_id(sid).add_tuple(x,y)
    return{"Status": "Koordinaten empfangen"}
    """spiel=lob.game_by_id(game)
    s1=spiel.get_p1()
    s2=spiel.get_p2()

    if sid==s1.get_id():
        s1.add_tuple(x,y)            #potenzielles Problem

    else:
        s2.add_tuple(x,y)
        
    return{"Status": "koordinaten empfangen"}"""
        

@rest_api.get("/{sid}/test")
async def test(sid: int):
    #spiel=lob.game_by_id(game)
    #x=spiel.get_p2().get_ship().get_koordinaten()
    x=lob.player_by_id(sid).get_ship().get_koordinaten()
    intx=len(x)
    return {"test": intx}


    
