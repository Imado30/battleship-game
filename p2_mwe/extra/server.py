from fastapi import FastAPI

try:
    import schiffeversenken
except ImportError as e:
  print(f"Importing the shared library 'schiffeversenken' did not work.")
  print(f"Is (a link to) the shared library 'schiffeversenken.____.so' in the same directory as this python script?")
  print(f"The import caused the following exception '{e}'")
  print(f"Exiting")
  exit(1)

from schiffeversenken import Lobby
import os
from fastapi import FastAPI
import uvicorn

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

"""
@rest_api.get("/{game}/turn")
async def get_turn():
    return{"current_turn":}  #irgendwie müsste erkannt werden, dass ich in dem jeweiligen Spiel bin 
"""