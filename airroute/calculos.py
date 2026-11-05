import math

RADIO_TIERRA_KM = 6371
TARIFA_BASE_EUR = 30      
PRECIO_POR_KM = 0.10
TIEMPO_EXTRA = 0.5
VELOCIDAD_MEDIA = 800

def haversine(lat1, lon1, lat2, lon2):
    # 1. Pasar de grados a radianes
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # 2. Diferencias entre los dos puntos
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # 3. Fórmula de Haversine
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # 4. Ángulo x radio = distancia
    return RADIO_TIERRA_KM * c


def calcular_precio(distancia):
    precio = TARIFA_BASE_EUR + PRECIO_POR_KM * distancia
    return precio


def calcular_tiempo(distancia):
    tiempo  = distancia / VELOCIDAD_MEDIA + TIEMPO_EXTRA
    return tiempo