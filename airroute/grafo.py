class TrayectoEncontrado:
    
    def __init__(self, lista_codigos, distancia, precio, duracion, escalas):
        self.lista_codigos = lista_codigos
        self.distancia = distancia
        self.precio = precio
        self.duracion = duracion
        self.escalas = escalas


class GrafoConPesos:
    
    def __init__(self):
        self.aeropuertos = {}
        self.adyacencia = {}

    def cargar_datos(self, lista_aeropuertos, lista_rutas):
        for aero in lista_aeropuertos:
            self.aeropuertos[aero.id] = aero
            self.adyacencia[aero.id] = []

        for ruta in lista_rutas:
            if ruta.id_origen in self.adyacencia and ruta.id_destino in self.aeropuertos:
                self.adyacencia[ruta.id_origen].append(ruta)

    def buscar_id_por_iata(self, codigo_iata):
        codigo_iata = codigo_iata.strip().upper()
        for id_aero in self.aeropuertos:
            if self.aeropuertos[id_aero].iata.upper() == codigo_iata:
                return id_aero
        return None

    def buscar_rutas(self, id_origen, id_destino, max_escalas):
        resultados = []
        aero_inicial = self.aeropuertos[id_origen]

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
                            camino_iata, visitados, dist_acum, precio_acum, dur_acum, resultados):
        
        if actual_id == id_destino and len(camino_iata) > 1:
            num_escalas = len(camino_iata) - 2
            nuevo_trayecto = TrayectoEncontrado(
                list(camino_iata), dist_acum, precio_acum, dur_acum, num_escalas
            )
            resultados.append(nuevo_trayecto)
            return

        if escalas_restantes < 0:
            return

        aristas_salientes = self.adyacencia[actual_id]
        destinos_vistos_en_este_salto = []

        for ruta in aristas_salientes:
            sig_id = ruta.id_destino

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
