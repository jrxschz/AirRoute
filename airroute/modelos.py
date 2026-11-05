class Aeropuerto:
    def __init__(self, id, nombre, ciudad, pais, iata, lat, lon):
        self.id = int(id)
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais
        self.iata = iata
        self.lat = float(lat)
        self.lon = float(lon)

    def __str__(self):
        return f"{self.iata} - {self.nombre} ({self.pais})"

class Ruta:
    def __init__(self, id_origen, id_destino, distancia, precio, duracion):
        self.id_origen = int(id_origen)
        self.id_destino = int(id_destino)
        self.distancia = float(distancia)
        self.precio = float(precio)
        self.duracion = float(duracion)