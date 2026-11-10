class Nodo: 
    
    def __init__(self, info):
        self.info = info
        self.next = None


class ListaEnlazada:
 
    def __init__(self):
        self.first = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    def get_size(self):
        return self.size

    def add_first(self, x): # Inserta un nuevo elemento al principio de la lista en O(1) 
        nuevo = Nodo(x)
        nuevo.next = self.first
        self.first = nuevo
        self.size += 1

    def get(self, pos): # Devuelve el valor almacenado en la posición indicada 
        if pos < 0 or pos >= self.size:
            return None
        actual = self.first
        for _ in range(pos):
            actual = actual.next
        return actual.info

    def remove_at(self, pos): # Elimina el nodo que está en la posición indicada 
        if pos < 0 or pos >= self.size or self.is_empty():
            return False

        # Caso 1: se elimina el primer nodo (posición 0)
        if pos == 0:
            self.first = self.first.next
            self.size -= 1
            return True

        # Caso general: se recorre hasta el nodo anterior (pos - 1) y salta el nodo 'pos'
        anterior = self.first
        for _ in range(pos - 1):
            anterior = anterior.next

        nodo_a_borrar = anterior.next
        anterior.next = nodo_a_borrar.next
        self.size -= 1
        return True

    def clear(self): # Elimina todos los elementos liberando los nodos
        self.first = None
        self.size = 0

    def show(self): # Recorre la lista nodo a nodo y muestra sus elementos 
        if self.is_empty():
            print("  El historial está vacío.")
            return

        actual = self.first
        posicion = 0
        while actual is not None:
            print(f"  [{posicion}] {actual.info}")
            actual = actual.next
            posicion += 1
