import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz Gráfica en Pantalla Completa - Suma de Números")

# Hacer que la ventana ocupe toda la pantalla
root.attributes('-fullscreen', True)

# Función para salir del modo de pantalla completa
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

# Asignar la tecla "Esc" para salir del modo de pantalla completa
root.bind("<Escape>", exit_fullscreen)

# Estilo para los widgets
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 14), padding=10)
style.configure('TButton', font=('Helvetica', 14), padding=10)
style.configure('TEntry', font=('Helvetica', 14), padding=10)

#Estilos adicionales
#style.configure('TLabel', font=('Helvetica', 14), padding=10, background='white', foreground='blue')
#style.configure('TButton', font=('Helvetica', 14), padding=10, background='blue', foreground='white')
#style.configure('TEntry', font=('Helvetica', 14), padding=10, fieldbackground='lightgray')


# Etiquetas y campos de entrada
label1 = ttk.Label(root, text="Introduce el primer número:", style='TLabel')
label1.pack(pady=10)
entry1 = ttk.Entry(root, style='TEntry')
entry1.pack(pady=5)

label2 = ttk.Label(root, text="Introduce el segundo número:", style='TLabel')
label2.pack(pady=10)
entry2 = ttk.Entry(root, style='TEntry')
entry2.pack(pady=5)

# Etiqueta para mostrar el resultado
result_label = ttk.Label(root, text="", style='TLabel')
result_label.pack(pady=20)

# Función para sumar los números
def sumar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 + num2
        result_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        result_label.config(text="Por favor, introduce números válidos")

# Botón para realizar la suma
sum_button = ttk.Button(root, text="Sumar", command=sumar, style='TButton')
sum_button.pack(pady=10)

# Botón para cerrar la aplicación
close_button = ttk.Button(root, text="Cerrar", command=root.quit, style='TButton')
close_button.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()
