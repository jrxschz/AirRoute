import csv 
from modelos import Aeropuerto


def cargar_aeropuertos(ruta_fichero):
    aeropuertos = []
    descartados = 0
    
    
    with open(ruta_fichero, encoding="Utf-8") as archivo:
        lector = csv.reader(archivo)
        
        for fila in lector:
            if fila[0] == "\\N" or fila[6] == "\\N" or fila[7] == "\\N":
                descartados += 1
                continue
            
            aeropuerto = Aeropuerto(fila[0], fila[1], fila[2], fila[3], fila[4], fila[6], fila[7])
            aeropuertos.append(aeropuerto)

    print(f"Aeropuertos cargados: {len(aeropuertos)} | descartados: {descartados}")
    return aeropuertos
