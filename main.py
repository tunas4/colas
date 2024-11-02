import tkinter as tk
import clases as c

root = tk.Tk()
root.title("Colas")
root.geometry("200x300")
root.resizable(False, False)

button = tk.Button(root, text="Inicializar/Borrar", command=c.inicializar)
button.pack(padx=10, pady=10)

button = tk.Button(root, text="Mostrar cola", command=c.mostrar_cola)
button.pack(padx=10, pady=10)

button = tk.Button(root, text="Insertar", command=c.insertar)
button.pack(padx=10, pady=10)

button = tk.Button(root, text="Eliminar", command=c.eliminar)
button.pack(padx=10, pady=10)

button = tk.Button(root, text="Creditos", command=c.creditos)
button.pack(padx=10, pady=10)

button = tk.Button(root, text="Salir", command=root.destroy)
button.pack(padx=10, pady=10)

root.mainloop()
