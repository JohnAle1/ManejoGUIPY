import tkinter as tk

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

# Etiquetas y campos de entrada
label1 = tk.Label(root, text="Introduce el primer número:")
label1.pack(pady=10)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Introduce el segundo número:")
label2.pack(pady=10)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="")
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
sum_button = tk.Button(root, text="Sumar", command=sumar)
sum_button.pack(pady=10)

# Botón para cerrar la aplicación
close_button = tk.Button(root, text="Cerrar", command=root.quit)
close_button.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()
