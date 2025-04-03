import tkinter as tk
from tkinter import ttk
import pandas as pd

def cargar_datos():
    df = pd.read_csv('datos.csv')  # Reemplaza con tu archivo CSV
    for row in df.values:
        tree.insert('datos.csv', 'end', values=row)

ventana = tk.Tk()
ventana.title("Cargar Datos CSV")

cargar_button = tk.Button(ventana, text="Cargar Datos", command=cargar_datos)
cargar_button.pack()

columns = ["Columna 1", "Columna 2", "Columna 3"]  # Asegúrate de cambiar los nombres de las columnas
tree = ttk.Treeview(ventana, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack()

ventana.mainloop()


