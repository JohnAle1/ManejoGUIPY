import tkinter as tk

lista1 = []
doom = tk.Tk()
doom.title("Interfaz Gráfica en Pantalla Completa")
doom.geometry("500x500")

# Variable global para la cantidad de datos
cantidadDatos = 0

def lecturadato():
    global cantidadDatos
    cantidadDatos = int(Ndatos.get())
    Ndatos.delete(0, tk.END)
    btnAceptar.config(state='disabled')
    Ndatos.config(state='normal')

def IngresoLista():
    global cantidadDatos
    lista1.append(Ndatos.get())
    Ndatos.delete(0, tk.END)
    cantidadDatos -= 1
    if cantidadDatos == 0:
        btnllenarlista.config(state='disabled')
        Ndatos.config(state='disabled')

def ImprimirLista():
    try:
        resultado.config(text=f"Resultado: {lista1}")
    except ValueError:
        resultado.config(text="Ocurrio un error")

# Objetos del doom y pack
label = tk.Label(doom, text="Cuantos datos vamos a ingresar: ")
label.pack(pady=20)

Ndatos = tk.Entry(doom, text="Ingreso")
Ndatos.pack()

btnAceptar = tk.Button(doom, text="Aceptar", command=lecturadato)
btnAceptar.pack(pady=10)

btnllenarlista = tk.Button(doom, text="Ingresar", command=IngresoLista)
btnllenarlista.pack(pady=10)

btnmostrarlista = tk.Button(doom, text="Imprimir", command=ImprimirLista)
btnmostrarlista.pack(pady=10)

resultado = tk.Label(doom, text="")
resultado.pack(pady=20)

# Tercera parte main loop
doom.mainloop()


