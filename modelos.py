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