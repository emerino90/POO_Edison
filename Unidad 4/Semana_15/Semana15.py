import tkinter as tk
from tkinter import simpledialog, messagebox

# Archivo de respaldo
ARCHIVO_TAREAS = "mis_tareas.txt"


# ---------------- Funciones ---------------- #

# Cargar tareas desde archivo
def cargar_tareas():
    try:
        with open(ARCHIVO_TAREAS, "r") as archivo:
            for linea in archivo:
                tarea = linea.strip()
                lista.insert(tk.END, tarea)
                if tarea.endswith("[✓]"):
                    lista.itemconfig(tk.END, fg="green")
    except FileNotFoundError:
        pass


# Guardar tareas en archivo
def guardar_tareas():
    with open(ARCHIVO_TAREAS, "w") as archivo:
        for tarea in lista.get(0, tk.END):
            archivo.write(tarea + "\n")


# Agregar una nueva tarea
def agregar_tarea(event=None):
    nueva = entrada.get().strip()
    if nueva:
        lista.insert(tk.END, nueva)
        entrada.delete(0, tk.END)
        guardar_tareas()
    else:
        messagebox.showinfo("Atención", "No se puede añadir una tarea vacía.")


# Cambiar estado de completado
def completar_tarea(event=None):
    try:
        i = lista.curselection()[0]
        texto = lista.get(i)
        if texto.endswith("[✓]"):
            texto = texto.replace(" [✓]", "")
            lista.itemconfig(i, fg="black")
        else:
            texto += " [✓]"
            lista.itemconfig(i, fg="green")
        lista.delete(i)
        lista.insert(i, texto)
        guardar_tareas()
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para marcar o desmarcar.")


# Eliminar tarea seleccionada
def eliminar_tarea():
    try:
        i = lista.curselection()[0]
        lista.delete(i)
        guardar_tareas()
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para eliminar.")


# Editar tarea seleccionada
def editar_tarea():
    try:
        i = lista.curselection()[0]
        actual = lista.get(i)
        nuevo = simpledialog.askstring("Editar", "Editar tarea:", initialvalue=actual)
        if nuevo:
            lista.delete(i)
            lista.insert(i, nuevo)
            lista.itemconfig(i, fg="black")
            guardar_tareas()
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para editar.")


# Salir de la aplicación
def cerrar_app(event=None):
    guardar_tareas()
    ventana.quit()


# ---------------- Interfaz ---------------- #

ventana = tk.Tk()
ventana.title("Mi Gestor de Tareas")
ventana.geometry("420x450")

entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=8)
entrada.bind("<Return>", agregar_tarea)

btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_tarea)
btn_agregar.pack(pady=5)

lista = tk.Listbox(ventana, width=50, height=12)
lista.pack(pady=10)
lista.bind("<Double-1>", completar_tarea)

btn_completar = tk.Button(ventana, text="Marcar/Desmarcar", command=completar_tarea)
btn_completar.pack(pady=4)

btn_borrar = tk.Button(ventana, text="Eliminar", command=eliminar_tarea)
btn_borrar.pack(pady=4)

btn_editar = tk.Button(ventana, text="Editar", command=editar_tarea)
btn_editar.pack(pady=4)

ventana.bind("<Escape>", cerrar_app)

cargar_tareas()
ventana.mainloop()

