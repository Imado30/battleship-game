from fastapi import FastAPI

try:
    import schiffeversenken
except ImportError as e:
  print(f"Importing the shared library 'schiffeversenken' did not work.")
  print(f"Is (a link to) the shared library 'schiffeversenken.____.so' in the same directory as this python script?")
  print(f"The import caused the following exception '{e}'")
  print(f"Exiting")
  exit(1)

from typing import List,Tuple
from schiffeversenken import Schiffe
import os
from fastapi import FastAPI
import uvicorn

rest_api= FastAPI()

schiff = Schiffe()

@rest_api.get("/postkoordinaten/{x}/{y}")
async def post_koordinaten(x : int, y : int):
   schiff.tupel_erstellen(x,y)
   return{"Status" : "Koordinaten empfangen"}


@rest_api.get("/schiffe")
async def spieler_koordinaten():
   return{"koordinaten" : schiff.get_koordinaten()}


"""
@rest_api.get("/")
async def wurzel_pfad():
    return{"coole_nachricht" : "Fast API funktioniert"}

@rest_api.get("/user/{uid}")
async def get_user_by_id(uid: int):
    return{"user_id" : uid}

@rest_api.get("/lobby/{name}")
async def create_player(name: str):
    return{"user_id:" : lob.spieler_erstellen(name).get_id()}
"""
