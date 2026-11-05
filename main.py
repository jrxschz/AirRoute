from pathlib import Path

from airroute.carga import cargar_aeropuertos, cargar_rutas

DATA = Path(__file__).parent / "Data"

aeropuertos = cargar_aeropuertos(DATA / "airports.dat")
rutas = cargar_rutas(DATA / "routes.dat", aeropuertos)
