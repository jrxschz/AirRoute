# airroute/algoritmos.py

def quicksort_aeropuertos(lista):
    """
    Ordena la lista de objetos Aeropuerto por su atributo 'id' de menor a mayor.
    Sigue el esquema del Tema 1 (diapositiva 64): menores, iguales y mayores.
    """
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]
    id_pivote = pivote.id

    menores = []
    iguales = []
    mayores = []

    for aeropuerto in lista:
        if aeropuerto.id < id_pivote:
            menores.append(aeropuerto)
        elif aeropuerto.id == id_pivote:
            iguales.append(aeropuerto)
        else:
            mayores.append(aeropuerto)

    return quicksort_aeropuertos(menores) + iguales + quicksort_aeropuertos(mayores)


def busqueda_interpolacion(a, x):
    """
    Busca un aeropuerto cuyo ID sea 'x' en la lista ordenada 'a'.
    Fórmula Tema 1 (diapositiva 43):
    pos = low + ((x - a[low]) / (a[high] - a[low])) * (high - low)
    """
    if len(a) == 0:
        return None

    low = 0
    high = len(a) - 1

    while low <= high and x >= a[low].id and x <= a[high].id:
        if low == high:
            if a[low].id == x:
                return a[low]
            return None

        if a[high].id == a[low].id:
            if a[low].id == x:
                return a[low]
            return None

        pos = low + int(((x - a[low].id) / (a[high].id - a[low].id)) * (high - low))

        if a[pos].id == x:
            return a[pos]
        elif a[pos].id < x:
            low = pos + 1
        else:
            high = pos - 1

    return None


def quicksort_rutas(lista_rutas, criterio="precio"):
    """
    Ordena las rutas encontradas según el criterio elegido:
    'precio', 'duracion', 'distancia' o 'escalas'.
    """
    if len(lista_rutas) <= 1:
        return lista_rutas

    pivote = lista_rutas[len(lista_rutas) // 2]

    if criterio == "precio":
        valor_pivote = pivote.precio
    elif criterio == "duracion":
        valor_pivote = pivote.duracion
    elif criterio == "escalas":
        valor_pivote = pivote.escalas
    else:
        valor_pivote = pivote.distancia

    menores = []
    iguales = []
    mayores = []

    for ruta in lista_rutas:
        if criterio == "precio":
            valor_actual = ruta.precio
        elif criterio == "duracion":
            valor_actual = ruta.duracion
        elif criterio == "escalas":
            valor_actual = ruta.escalas
        else:
            valor_actual = ruta.distancia

        if valor_actual < valor_pivote:
            menores.append(ruta)
        elif valor_actual == valor_pivote:
            iguales.append(ruta)
        else:
            mayores.append(ruta)

    return quicksort_rutas(menores, criterio) + iguales + quicksort_rutas(mayores, criterio)
