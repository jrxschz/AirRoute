from pathlib import Path
import time
from airroute.carga import cargar_aeropuertos, cargar_rutas
from airroute.algoritmos import quicksort_aeropuertos, busqueda_interpolacion, quicksort_rutas
from airroute.grafo import GrafoConPesos
from airroute.historial import ListaEnlazada

DATA = Path(__file__).parent / "Data"

# 1. Carga y limpieza de los ficheros CSV 
aeropuertos = cargar_aeropuertos(DATA / "airports.dat")
rutas = cargar_rutas(DATA / "routes.dat", aeropuertos)

print("=== AirRoute ===")
print("1. Ver número de aeropuertos")
print("2. Buscar aeropuerto")
print("3. Salir")

while True:
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Hay {len(aeropuertos)} aeropuertos cargados.")

    elif opcion == "2":
        codigo = input("Introduce el código IATA: ").upper()
        encontrado = False

        for aeropuerto in aeropuertos:
            if aeropuerto.iata == codigo:
                print(f"{aeropuerto.nombre} - {aeropuerto.ciudad} ({aeropuerto.pais})")
                encontrado = True
                break

        if not encontrado:
            print("No se encontró ese aeropuerto.")

    elif opcion == "3":
        for i in range(3):
            print("Saliendo de la interfaz...")
        
    else:
        print("Opción no válida.")
