import tkinter as tk
from tkinter import ttk

# Función que se llama cuando se selecciona un elemento en el Combobox
def mostrar_seleccion(event):
    seleccion = combo.get()  # Obtener la selección actual del Combobox
    entry.delete(0, tk.END)  # Limpiar el contenido actual del Entry
    entry.insert(0, seleccion)  # Insertar la selección en el Entry

# Crear la ventana principal
root = tk.Tk()
root.title("Hacer una Lista")

# Hacer que la ventana ocupe toda la pantalla
root.geometry("500x500")

# Crear el Combobox
combo = ttk.Combobox(root, values=["Opción 1", "Opción 2", "Opción 3"])
combo.pack(pady=10)  # Agregar espacio vertical entre el Combobox y el Entry

# Crear el Entry
entry = tk.Entry(root)
entry.pack(pady=10)  # Agregar espacio vertical entre el Entry y el borde inferior de la ventana

# Vincular la función mostrar_seleccion al evento de selección del Combobox
combo.bind("<<ComboboxSelected>>", mostrar_seleccion)

# Ejecutar el bucle principal
root.mainloop()