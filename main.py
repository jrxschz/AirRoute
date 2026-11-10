from pathlib import Path

from airroute.carga import cargar_aeropuertos, cargar_rutas
from airroute.algoritmos import quicksort_aeropuertos, busqueda_interpolacion, quicksort_rutas
from airroute.grafo import GrafoConPesos
from airroute.historial import ListaEnlazada

DATA = Path(__file__).parent / "Data"

# 1. Carga y limpieza de los ficheros CSV 
aeropuertos = cargar_aeropuertos(DATA / "airports.dat")
rutas = cargar_rutas(DATA / "routes.dat", aeropuertos)

# 2. Ordenar aeropuertos por ID con QuickSort para poder usar Búsqueda por Interpolación
aeropuertos_ordenados = quicksort_aeropuertos(aeropuertos)

# 3. Crear y poblar el Grafo dirigido con pesos
grafo = GrafoConPesos()
grafo.cargar_datos(aeropuertos_ordenados, rutas)

# 4. Inicializar la Lista Enlazada para el historial de búsquedas
historial = ListaEnlazada()

# 5. Menú principal interactivo 
while True:
    print("\n==========================================")
    print("         AIRROUTE MANAGER - MENÚ          ")
    print("==========================================")
    print("1. Buscar aeropuerto por ID (Interpolación)")
    print("2. Buscar rutas entre aeropuertos (Grafo + QuickSort)")
    print("3. Ver historial de búsquedas (Lista Enlazada)")
    print("4. Eliminar una búsqueda del historial (remove_at)")
    print("0. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        id_texto = input("Introduce el ID numérico del aeropuerto (ej. 1229 para Madrid): ").strip()
        if not id_texto.isdigit():
            print("Error: El ID debe ser un número entero positivo.")
            continue

        id_buscado = int(id_texto)
        encontrado = busqueda_interpolacion(aeropuertos_ordenados, id_buscado)

        if encontrado is not None:
            print(f"\n-> Encontrado: [ID {encontrado.id}] {encontrado}")
            print(f"   Ciudad: {encontrado.ciudad} | Coordenadas: ({encontrado.lat}, {encontrado.lon})")
            historial.add_first(f"Consulta ID {id_buscado}: {encontrado.iata} ({encontrado.nombre})")
        else:
            print("\n-> No existe ningún aeropuerto con ese ID en la base de datos.")

    elif opcion == "2":
        origen_iata = input("Código IATA de origen (ej. MAD): ").strip().upper()
        destino_iata = input("Código IATA de destino (ej. JFK): ").strip().upper()

        if origen_iata == destino_iata:
            print("Error: El aeropuerto de origen y el de destino no pueden ser iguales.")
            continue

        id_origen = grafo.buscar_id_por_iata(origen_iata)
        id_destino = grafo.buscar_id_por_iata(destino_iata)

        if id_origen is None or id_destino is None:
            print("Error: Alguno de los códigos IATA introducidos no existe.")
            continue

        escalas_txt = input("Máximo de escalas (0 = vuelo directo, 1 = hasta 1 escala): ").strip()
        if not escalas_txt.isdigit() or int(escalas_txt) > 2:
            print("Aviso: Se usará por defecto máximo 1 escala.")
            max_escalas = 1
        else:
            max_escalas = int(escalas_txt)

        criterio = input("Ordenar por (precio / duracion / distancia / escalas): ").strip().lower()
        if criterio not in ["precio", "duracion", "distancia", "escalas"]:
            criterio = "precio"

        print(f"\nBuscando vuelos de {origen_iata} a {destino_iata} (máx. {max_escalas} escalas)...")
        trayectos = grafo.buscar_rutas(id_origen, id_destino, max_escalas)

        if len(trayectos) == 0:
            print("No se ha encontrado ninguna combinación posible con esas escalas.")
            continue

        # Se ordena con el algoritmo QuickSort
        trayectos_ordenados = quicksort_rutas(trayectos, criterio)

        print(f"\nSe han encontrado {len(trayectos_ordenados)} rutas. Mostrando las 5 mejores por {criterio}:")
        for i in range(min(5, len(trayectos_ordenados))):
            t = trayectos_ordenados[i]
            camino_str = " -> ".join(t.lista_codigos)
            print(f"  {i+1}. {camino_str} | Escalas: {t.escalas} | "
                  f"Precio: {t.precio:.2f} € | Duración: {t.duracion:.2f} h | Dist: {t.distancia:.0f} km")

        # Guarda la consulta al inicio de la lista enlazada en O(1)
        historial.add_first(f"Ruta {origen_iata}->{destino_iata} (máx {max_escalas} esc., orden: {criterio})")

    elif opcion == "3":
        print(f"\n--- HISTORIAL DE BÚSQUEDAS (Total: {historial.get_size()}) ---")
        historial.show()

    elif opcion == "4":
        historial.show()
        if not historial.is_empty():
            pos_txt = input("Introduce la posición [número] que quieres borrar: ").strip()
            if pos_txt.isdigit() and historial.remove_at(int(pos_txt)):
                print("Elemento eliminado correctamente de la lista enlazada.")
            else:
                print("Error: Posición fuera de rango.")

    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")


