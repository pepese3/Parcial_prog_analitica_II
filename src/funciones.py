import sys
sys.path.append("/content/mi_proyecto/data")

import data
Canciones_artistas = data.Canciones_artistas

def anadir_nuevo_artista(artista: str, canciones: list)-> None:
    Canciones_artistas.update({artista: canciones})
def mostrar_canciones_artista(artista: str)-> list:
    return Canciones_artistas[artista]
def anadir_canciones_artista(artista: str, canciones: list)-> None:
    Canciones_artistas[artista] += canciones
def buscar_cancion_p_nombre(cancion: str)-> str:
    for items in Canciones_artistas.values():
       for elementos in items:
          if elementos == cancion:
              return cancion
