class TrayectoEncontrado: # Guarda el resultado de un camino completo con la suma total de distancia, precio, duración y número de escalas.
    
    def __init__(self, lista_codigos, distancia, precio, duracion, escalas):
        self.lista_codigos = lista_codigos
        self.distancia = distancia
        self.precio = precio
        self.duracion = duracion
        self.escalas = escalas


class GrafoConPesos: # Grafo dirigido con pesos representado mediante lista de adyacencia.
    
    def __init__(self):
        self.aeropuertos = {}   # id_aeropuerto: Objeto Aeropuerto
        self.adyacencia = {}    # id_origen: Lista de objetos Ruta que salen de él

    def cargar_datos(self, lista_aeropuertos, lista_rutas): # Mete todos los aeropuertos como nodos y todas las rutas como aristas.
        for aero in lista_aeropuertos:
            self.aeropuertos[aero.id] = aero
            self.adyacencia[aero.id] = []

        for ruta in lista_rutas:
            if ruta.id_origen in self.adyacencia and ruta.id_destino in self.aeropuertos:
                self.adyacencia[ruta.id_origen].append(ruta)

    def buscar_id_por_iata(self, codigo_iata): # Busca secuencialmente el ID de un aeropuerto dado su código IATA (ej. MAD)
        codigo_iata = codigo_iata.strip().upper()
        for id_aero in self.aeropuertos:
            if self.aeropuertos[id_aero].iata.upper() == codigo_iata:
                return id_aero
        return None

    def buscar_rutas(self, id_origen, id_destino, max_escalas): # Método principal que inicia la búsqueda de rutas
        resultados = []
        aero_inicial = self.aeropuertos[id_origen]

        # Inicia la recursión pasando el aeropuerto de origen como ya visitado
        self._explorar_recursivo(
            actual_id=id_origen,
            id_destino=id_destino,
            escalas_restantes=max_escalas,
            camino_iata=[aero_inicial.iata],
            visitados=[id_origen],
            dist_acum=0.0,
            precio_acum=0.0,
            dur_acum=0.0,
            resultados=resultados
        )
        return resultados

    def _explorar_recursivo(self, actual_id, id_destino, escalas_restantes,
                            camino_iata, visitados, dist_acum, precio_acum, dur_acum, resultados): # Recursión en cascada acotada por 'escalas_restantes'. Métrica de reducción: en cada salto disminuye 'escalas_restantes - 1'.
        
        # Caso 1: Se ha llegado al aeropuerto de destino (y se ha hecho al menos 1 vuelo)
        if actual_id == id_destino and len(camino_iata) > 1:
            num_escalas = len(camino_iata) - 2
            nuevo_trayecto = TrayectoEncontrado(
                list(camino_iata), dist_acum, precio_acum, dur_acum, num_escalas
            )
            resultados.append(nuevo_trayecto)
            return

        # Caso 2: No quedan escalas disponibles para seguir saltando
        if escalas_restantes < 0:
            return

        # Explorar los vuelos que salen del aeropuerto actual
        aristas_salientes = self.adyacencia[actual_id]
        destinos_vistos_en_este_salto = []

        for ruta in aristas_salientes:
            sig_id = ruta.id_destino

            # Evitar ciclos (no volver a un aeropuerto ya visitado) y evitar duplicados de aerolíneas
            if sig_id not in visitados and sig_id not in destinos_vistos_en_este_salto:
                destinos_vistos_en_este_salto.append(sig_id)
                sig_iata = self.aeropuertos[sig_id].iata

               
                self._explorar_recursivo(
                    actual_id=sig_id,
                    id_destino=id_destino,
                    escalas_restantes=escalas_restantes - 1,
                    camino_iata=camino_iata + [sig_iata],
                    visitados=visitados + [sig_id],
                    dist_acum=dist_acum + ruta.distancia,
                    precio_acum=precio_acum + ruta.precio,
                    dur_acum=dur_acum + ruta.duracion,
                    resultados=resultados
                )
