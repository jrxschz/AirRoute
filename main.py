from pathlib import Path

from airroute.carga import cargar_aeropuertos, cargar_rutas

DATA = Path(__file__).parent / "Data"

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
        print("Salido de la interfaz.")
        break

    else:
        print("Opción no válida.")
