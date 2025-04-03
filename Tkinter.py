import tkinter as tk

def saludar():
    etiqueta.config(text="¡Hola, Mundo!")

ventana = tk.Tk()
ventana.title("Mi Primera Ventana")

etiqueta = tk.Label(ventana, text="Bienvenido")
etiqueta.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

ventana.mainloop()
