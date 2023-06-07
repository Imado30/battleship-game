from fastapi import FastAPI

try:
    import schiffeversenken
except ImportError as e:
  print(f"Importing the shared library 'schiffeversenken' did not work.")
  print(f"Is (a link to) the shared library 'schiffeversenken.____.so' in the same directory as this python script?")
  print(f"The import caused the following exception '{e}'")
  print(f"Exiting")
  exit(1)

from schiffeversenken import Schiffe
import os
from fastapi import FastAPI
import uvicorn


#lob = Lobby()
schiff = Schiffe()

rest_api= FastAPI()

@rest_api.get("/")
async def wurzel_pfad():
    return{"coole_nachricht" : "Fast API funktioniert"}

@rest_api.get("/user/{uid}")
async def get_user_by_id(uid: int):
    return{"user_id" : uid}

"""
@rest_api.get("/lobby/{name}")
async def create_player(name: str):
    return{"user_id:" : lob.spieler_erstellen(name).get_id()}
"""
