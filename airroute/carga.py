import csv

from airroute.modelos import Aeropuerto, Ruta
from airroute.calculos import haversine, calcular_precio, calcular_tiempo




def cargar_aeropuertos(ruta_fichero):
    aeropuertos = []
    descartados = 0
    
    
    with open(ruta_fichero, encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        
        for fila in lector:
            if fila[0] == "\\N" or fila[6] == "\\N" or fila[7] == "\\N":
                descartados += 1
                continue
            
            aeropuerto = Aeropuerto(fila[0], fila[1], fila[2], fila[3], fila[4], fila[6], fila[7])
            aeropuertos.append(aeropuerto)

    print(f"Aeropuertos cargados: {len(aeropuertos)} | descartados: {descartados}")
    return aeropuertos



def cargar_rutas(ruta_fichero, aeropuertos):

    # 1. Diccionario para encontrar cada aeropuerto por su ID al instante
    aeropuertos_por_id = {}
    for aeropuerto in aeropuertos:
        aeropuertos_por_id[aeropuerto.id] = aeropuerto

    rutas = []
    descartadas = 0

    with open(ruta_fichero, encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        for fila in lector:
            # 2. Descartar si falta algún ID
            if fila[3] == "\\N" or fila[5] == "\\N":
                descartadas += 1
                continue

            origen_id = int(fila[3])
            destino_id = int(fila[5])

            # 3. Descartar si algún aeropuerto no está en nuestro diccionario
            if origen_id not in aeropuertos_por_id or destino_id not in aeropuertos_por_id:
                descartadas += 1
                continue

            # 4. Calcular los pesos de la arista
            origen = aeropuertos_por_id[origen_id]
            destino = aeropuertos_por_id[destino_id]
            distancia = haversine(origen.lat, origen.lon, destino.lat, destino.lon)
            precio = calcular_precio(distancia)
            tiempo = calcular_tiempo(distancia)

            # 5. Crear la ruta y guardarla
            ruta = Ruta(origen_id, destino_id, distancia, precio, tiempo)
            rutas.append(ruta)

    print(f"Rutas cargadas: {len(rutas)} | descartadas: {descartadas}")
    return rutas


sda
sd
as
d
as
d
sad