import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz Gráfica Extendida")
root.geometry("400x300")

# Crear una etiqueta
label = tk.Label(root, text="Introduce tu nombre:")
label.pack(pady=10)

# Crear un campo de entrada de texto
entry = tk.Entry(root)
entry.pack(pady=5)

# Crear una etiqueta para mostrar el saludo
greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=20)

# Crear una función para mostrar el saludo
def show_greeting():
    name = entry.get()
    greeting_label.config(text=f"¡Hola, {name}!")

# Crear un botón para mostrar el saludo
greet_button = tk.Button(root, text="Saludar", command=show_greeting)
greet_button.pack(pady=10)

# Crear un botón para cerrar la aplicación
close_button = tk.Button(root, text="Cerrar", command=root.quit)
close_button.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()
