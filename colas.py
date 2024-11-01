class colas:
    def __init__(self):
        self.max = 5
        self.cola = []
        self.inicio = -1
        self.fin = -1

    def inicializar(self):
        self.inicio = -1
        self.fin = -1

    def insertar_cola_doble_circular(self, v, l):
        # Verifica si la cola está llena en ambos extremos
        if (self.inicio == 0 and self.fin == self.max - 1) or (self.fin == self.inicio - 1):
            return "Cola llena"

        # Si la cola está vacía
        if self.inicio == -1:
            self.inicio = self.fin = 0
            self.cola[self.inicio] = v
            return "Valor insertado"

        # Inserción al final de la cola (l = 0)
        if l == 0:
            # Si `fin` llega al final de la cola, vuelve al inicio (comportamiento circular)
            if self.fin == self.max - 1:
                self.fin = 0
            else:
                self.fin += 1
            self.cola[self.fin] = v
        # Inserción al inicio de la cola (l = 1)
        else:
            # Si `inicio` llega al principio de la cola, vuelve al final (comportamiento circular)
            if self.inicio == 0:
                self.inicio = self.max - 1
            else:
                self.inicio -= 1
            self.cola[self.inicio] = v

        return "Valor insertado"

    def eliminar_cola_doble_circular(self, l):
        # Verificar si la cola está vacía
        if self.inicio == -1:
            return "Cola vacía"

        # Cuando hay un solo elemento
        if self.inicio == self.fin:
            t = self.cola[self.inicio]
            self.inicio = self.fin = -1
        else:
            # Eliminar desde el final (l = 0)
            if l == 0:
                t = self.cola[self.fin]
                # Si `fin` está en el primer índice, vuelve al final (comportamiento circular)
                if self.fin == 0:
                    self.fin = self.max - 1
                else:
                    self.fin -= 1
            # Eliminar desde el inicio (l = 1)
            else:
                t = self.cola[self.inicio]
                # Si `inicio` está en el último índice, vuelve al comienzo (comportamiento circular)
                if self.inicio == self.max - 1:
                    self.inicio = 0
                else:
                    self.inicio += 1

        return t

    def mostrar_cola_doble_circular(self):
        # Verifica si la cola está vacía
        if self.inicio == -1:
            return "Cola vacía"

        elementos = []
        i = self.inicio

        # Recorrer la cola desde inicio hasta fin
        while True:
            # Agrega a la lista el valor y su posición en formato (posición, valor)
            elementos.append((i, self.cola[i]))
            
            # Detiene el ciclo si hemos llegado al último elemento
            if i == self.fin:
                break
            
            # Mueve el índice al siguiente elemento, considerando la circularidad
            i = (i + 1) % self.max

        # Genera el formato de salida para mostrar posición y valor
        resultado = "\n".join([f"Posición {pos}: {valor}" for pos, valor in elementos])
        return resultado