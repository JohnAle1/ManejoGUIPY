import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz Dinámica - Ingreso de Términos")

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

# Frame para pedir el número de términos
num_frame = ttk.Frame(root)
num_frame.pack(pady=20)

# Etiqueta y campo de entrada para el número de términos
label_n = ttk.Label(num_frame, text="Introduce el número de términos:", style='TLabel')
label_n.pack(pady=10)
entry_n = ttk.Entry(num_frame, style='TEntry')
entry_n.pack(pady=5)

# Frame para contener el canvas y el scrollbar
canvas_frame = ttk.Frame(root)
canvas_frame.pack(fill=tk.BOTH, expand=True, pady=20)

# Crear un canvas para los términos dinámicos
canvas = tk.Canvas(canvas_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Añadir un scrollbar al canvas
scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configurar el canvas para usar el scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Crear un frame dentro del canvas para los términos
terms_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=terms_frame, anchor="nw")

# Lista para guardar los campos de entrada de términos
entries = []

# Función para generar los campos de entrada de términos
def generar_terminos():
    try:
        n = int(entry_n.get())
        # Limpiar el frame de términos anterior
        for widget in terms_frame.winfo_children():
            widget.destroy()
        entries.clear()
        
        for i in range(n):
            label = ttk.Label(terms_frame, text=f"Término {i+1}:", style='TLabel')
            label.pack(pady=5)
            entry = ttk.Entry(terms_frame, style='TEntry')
            entry.pack(pady=5)
            entries.append(entry)
        
        # Botón para recolectar los valores ingresados
        submit_button = ttk.Button(terms_frame, text="Submit", command=mostrar_terminos, style='TButton')
        submit_button.pack(pady=20)
        
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        
    except ValueError:
        pass

# Función para mostrar los términos ingresados
def mostrar_terminos():
    valores = [entry.get() for entry in entries]
    print("Términos ingresados:", valores)
    result_label.config(text=f"Términos ingresados: {', '.join(valores)}")

# Botón para generar los campos de entrada de términos
generate_button = ttk.Button(num_frame, text="Generar Términos", command=generar_terminos, style='TButton')
generate_button.pack(pady=10)

# Etiqueta para mostrar el resultado
result_label = ttk.Label(root, text="", style='TLabel')
result_label.pack(pady=20)

# Botón para cerrar la aplicación
close_button = ttk.Button(root, text="Cerrar", command=root.quit, style='TButton')
close_button.pack(side='bottom', pady=20)

# Ejecutar el bucle principal
root.mainloop()
