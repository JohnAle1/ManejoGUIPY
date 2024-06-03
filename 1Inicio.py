import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz Gráfica en Pantalla Completa")

# Hacer que la ventana ocupe toda la pantalla
#root.attributes('-fullscreen', True)
root.geometry("500x500")

# Crear una etiqueta
label = tk.Label(root, text="¡Hola, Mundo en Pantalla Completa!")
label.pack(pady=20)

# Crear un botón
def on_button_click():
    root.quit()

button = tk.Button(root, text="Cerrar", command=on_button_click)
button.pack(pady=10)

# Función para salir del modo de pantalla completa
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

# Asignar la tecla "Esc" para salir del modo de pantalla completa
root.bind("<Escape>", exit_fullscreen)

# Ejecutar el bucle principal
root.mainloop()
