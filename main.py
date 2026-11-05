import Data
import csv
from modelos import Aeropuerto


from cargar_aeropuertos import cargar_aeropuertos

aeropuertos = cargar_aeropuertos("Data/airports.dat")
print(aeropuertos[0])
print(aeropuertos[-1])
