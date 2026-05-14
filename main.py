import sys
sys.path.append("/content/mi_proyecto/src")
sys.path.append("/content/mi_proyecto/data")

import data
Canciones_artistas = data.Canciones_artistas
from funciones import anadir_nuevo_artista, mostrar_canciones_artista, anadir_canciones_artista, buscar_cancion_p_nombre
print(f"Canciones originales: {Canciones_artistas.values()}")
print(f"añado un nuevo artista: {anadir_nuevo_artista("supreme_artist", ["Heaven", "Hell"])}")
anadir_canciones_artista("Ronaldo_musique", ["Una noche en Colombia"])
print(Canciones_artistas)
mostrar_canciones_artista("Ronaldo_musique")
print(Canciones_artistas)
print(buscar_cancion_p_nombre("plato"))
