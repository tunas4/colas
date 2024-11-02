import tkinter as tk

class ColaDobleCircular:
    max_tamano = 5
    def __init__(self, max_tamano=None):
        self.max = max_tamano if max_tamano else ColaDobleCircular.max_tamano
        self.cola = [None] * self.max
        self.inicio = -1
        self.fin = -1

    def inicializar(self):
        self.inicio = self.fin = -1
        self.cola = [None] * self.max

    def insertar_cola_doble_circular(self, v, l):
        if (self.inicio == 0 and self.fin == self.max - 1) or (self.fin == self.inicio - 1):
            return "Cola llena"

        if self.inicio == -1:
            self.inicio = self.fin = 0
            self.cola[self.inicio] = v
            return "Valor insertado"

        if l == 0:
            if self.fin == self.max - 1:
                self.fin = 0
            else:
                self.fin += 1
            self.cola[self.fin] = v
        else:
            if self.inicio == 0:
                self.inicio = self.max - 1
            else:
                self.inicio -= 1
            self.cola[self.inicio] = v

        return "Valor insertado"

    def eliminar_cola_doble_circular(self, l):
        if self.inicio == -1:
            return "Cola vacía"

        if self.inicio == self.fin:
            t = self.cola[self.inicio]
            self.inicio = self.fin = -1
        else:
            if l == 0:
                t = self.cola[self.fin]
                if self.fin == 0:
                    self.fin = self.max - 1
                else:
                    self.fin -= 1
            else:
                t = self.cola[self.inicio]
                if self.inicio == self.max - 1:
                    self.inicio = 0
                else:
                    self.inicio += 1

        return t

    def mostrar_cola_doble_circular(self):
        if self.inicio == -1:
            return "Cola vacía"

        elementos = []
        i = self.inicio

        while True:
            elementos.append((i, self.cola[i]))
            
            if i == self.fin:
                break
            
            i = (i + 1) % self.max

        resultado = "\n".join([f"Posición {pos}: {valor}" for pos, valor in elementos])
        return resultado

c = ColaDobleCircular(5)

def inicializar():
    root = tk.Tk()
    root.title("Inicializar")
    root.geometry("200x100")
    root.resizable(False, False)

    def borrar_cola():
        c.inicializar()
        label = tk.Label(root, text="Cola borrada")
        label.pack(padx=10, pady=10, anchor="center")

    button = tk.Button(root, text="Inicializar", command=borrar_cola)
    button.pack(padx=10, pady=10, anchor="center")

    root.mainloop()

def mostrar_cola():
    root = tk.Tk()
    root.title("Mostrar cola")
    root.geometry("500x200")
    root.resizable(False, False)

    resultado = c.mostrar_cola_doble_circular()
    label = tk.Label(root, text=resultado)
    label.pack(padx=10, pady=10, anchor="center")

    root.mainloop()

def insertar():
    root = tk.Tk()
    root.title("Insertar")
    root.geometry("250x250")
    root.resizable(False, False)

    def acualizar_interfaz():
        if (c.inicio == 0 and c.fin == c.max - 1) or (c.fin == c.inicio - 1):
            label.config(text="Cola llena")
            button_inicio.config(state="disabled")
            button_final.config(state="disabled")
        else:   
            label.config(text="")
            button_inicio.config(state="normal")
            button_final.config(state="normal")

    def ins_in():
        v = entry.get()
        try:
            v = int(v)
        except ValueError:
            resultado_label.config(text="Ingrese un número válido")
            return

        res = c.insertar_cola_doble_circular(int(v), 1)
        resultado_label.config(text=res)
        entry.delete(0, tk.END)
        entry.focus()
        acualizar_interfaz()

    def ins_fin():
        v = entry.get()
        try:
            v = int(v)
        except ValueError:
            resultado_label.config(text="Ingrese un número válido")
            return

        res = c.insertar_cola_doble_circular(int(v), 0)
        resultado_label.config(text=res)
        entry.delete(0, tk.END)
        entry.focus()
        acualizar_interfaz()

    label = tk.Label(root, text="Ingrese el valor a insertar:")
    label.pack(padx=10, pady=10, anchor="center")

    entry = tk.Entry(root)
    entry.pack(padx=10, pady=10, anchor="center")

    button_inicio = tk.Button(root, text="Insertar por el inicio", command=ins_in)
    button_inicio.pack(padx=10, pady=10, anchor="center")

    button_final = tk.Button(root, text="Insertar por el final", command=ins_fin)
    button_final.pack(padx=10, pady=10, anchor="center")

    resultado_label = tk.Label(root, text="")
    resultado_label.pack(padx=10, pady=10, anchor="center")

    acualizar_interfaz()

    root.mainloop()

def eliminar():
    root = tk.Tk()
    root.title("Eliminar")
    root.geometry("200x200")
    root.resizable(False, False)

    label = tk.Label(root, text="")
    label.pack(padx=10, pady=10, anchor="center")

    def acualizar_interfaz():
        if c.inicio == -1:
            label.config(text="Cola vacía")
            button_inicio.config(state="disabled")
            button_final.config(state="disabled")
        else:   
            label.config(text="")

    if c.inicio == -1:
        label = tk.Label(root, text="Cola vacía")
        label.pack(padx=10, pady=10, anchor="center")
        return

    def eliminar_in():
        res = c.eliminar_cola_doble_circular(1)
        label.config(text=f"Elemento eliminado: {res}")
        acualizar_interfaz()
    
    def eliminar_fin():
        res = c.eliminar_cola_doble_circular(0)
        label.config(text=res)
        acualizar_interfaz()

    button_inicio = tk.Button(root, text="Eliminar del inicio", command=eliminar_in)
    button_inicio.pack(padx=10, pady=10, anchor="center")

    button_final = tk.Button(root, text="Eliminar del final", command=eliminar_fin)
    button_final.pack(padx=10, pady=10, anchor="center")

    label = tk.Label(root, text="")
    label.pack(padx=10, pady=10, anchor="center")

    root.mainloop()

def creditos():
    root = tk.Tk()
    root.title("Créditos")
    root.geometry("250x200")
    root.resizable(False, False)
    labelMateria = tk.Label(root, text="Estructura de datos Aplicadas")
    labelMateria.pack(padx=10, pady=10, anchor="center")
    label = tk.Label(root, text="Desarrollado por:")
    labelNoe = tk.Label(root, text="Noé Abel Vargas López | 23170106")
    labelJona = tk.Label(root, text="Jonathan Ivan Castro Saenz | 23170035")
    label.pack(padx=10, pady=10, anchor="center")
    labelNoe.pack(padx=10, pady=10, anchor="center")
    labelJona.pack(padx=10, pady=10, anchor="center")

    root.mainloop()

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cola Doble Circular")
    root.geometry("300x300")
    root.resizable(False, False)

    button_inicializar = tk.Button(root, text="Inicializar", command=inicializar)
    button_inicializar.pack(padx=10, pady=10, anchor="center")

    button_mostrar = tk.Button(root, text="Mostrar Cola", command=mostrar_cola)
    button_mostrar.pack(padx=10, pady=10, anchor="center")

    button_insertar = tk.Button(root, text="Insertar", command=insertar)
    button_insertar.pack(padx=10, pady=10, anchor="center")

    button_eliminar = tk.Button(root, text="Eliminar", command=eliminar)
    button_eliminar.pack(padx=10, pady=10, anchor="center")

    button_creditos = tk.Button(root, text="Créditos", command=creditos)
    button_creditos.pack(padx=10, pady=10, anchor="center")

    root.mainloop()
