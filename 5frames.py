import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz Sum 2 numeros")

# Hacer que la ventana ocupe toda la pantalla
root.geometry("800x500")

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

# Crear el frame para los inputs
input_frame = ttk.Frame(root)
input_frame.pack(side='left', padx=20, pady=20)

# Crear el frame para el resultado
result_frame = ttk.Frame(root)
result_frame.pack(side='right', padx=20, pady=20)

# Etiquetas y campos de entrada
label1 = ttk.Label(input_frame, text="Introduce el primer número:", style='TLabel')
label1.pack(pady=10)
entry1 = ttk.Entry(input_frame, style='TEntry')
entry1.pack(pady=5)

label2 = ttk.Label(input_frame, text="Introduce el segundo número:", style='TLabel')
label2.pack(pady=10)
entry2 = ttk.Entry(input_frame, style='TEntry')
entry2.pack(pady=5)

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
sum_button = ttk.Button(input_frame, text="Sumar", command=sumar, style='TButton')
sum_button.pack(pady=10)

# Etiqueta para mostrar el resultado
result_label = ttk.Label(result_frame, text="", style='TLabel')
result_label.pack(pady=20)

# Botón para cerrar la aplicación
close_button = ttk.Button(root, text="Cerrar", command=root.quit, style='TButton')
close_button.pack(side='bottom', pady=20)

# Ejecutar el bucle principal
root.mainloop()
