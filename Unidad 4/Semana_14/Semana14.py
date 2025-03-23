import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaPersonal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi Agenda")
        self.ventana.geometry("620x420")

        # Área de entrada de datos
        self.marco_datos = tk.LabelFrame(ventana, text="Nuevo Evento", padx=10, pady=10)
        self.marco_datos.pack(fill="x", padx=15, pady=10)

        tk.Label(self.marco_datos, text="Fecha:").grid(row=0, column=0, sticky="w")
        self.entrada_fecha = DateEntry(self.marco_datos, width=15)
        self.entrada_fecha.grid(row=0, column=1, padx=10)

        tk.Label(self.marco_datos, text="Hora:").grid(row=0, column=2, sticky="w")
        self.entrada_hora = tk.Entry(self.marco_datos, width=15)
        self.entrada_hora.grid(row=0, column=3, padx=10)

        tk.Label(self.marco_datos, text="Descripción:").grid(row=1, column=0, sticky="w")
        self.entrada_desc = tk.Entry(self.marco_datos, width=50)
        self.entrada_desc.grid(row=1, column=1, columnspan=3, pady=5)

        # Área de botones
        self.marco_botones = tk.Frame(ventana)
        self.marco_botones.pack(pady=5)

        tk.Button(self.marco_botones, text="Guardar", width=15, bg="#4CAF50", fg="white", command=self.guardar_evento).pack(side="left", padx=10)
        tk.Button(self.marco_botones, text="Eliminar Seleccionado", width=20, bg="#f44336", fg="white", command=self.confirmar_eliminacion).pack(side="left", padx=10)
        tk.Button(self.marco_botones, text="Salir", width=10, command=ventana.quit).pack(side="left", padx=10)

        # Área para mostrar los eventos
        self.marco_lista = tk.LabelFrame(ventana, text="Eventos Programados")
        self.marco_lista.pack(fill="both", expand=True, padx=15, pady=10)

        self.vista_eventos = ttk.Treeview(self.marco_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.vista_eventos.heading("Fecha", text="Fecha")
        self.vista_eventos.heading("Hora", text="Hora")
        self.vista_eventos.heading("Descripción", text="Descripción")
        self.vista_eventos.pack(fill="both", expand=True)

    def guardar_evento(self):
        fecha = self.entrada_fecha.get()
        hora = self.entrada_hora.get().strip()
        desc = self.entrada_desc.get().strip()

        if not (fecha and hora and desc):
            messagebox.showwarning("Faltan Datos", "Completa todos los campos para guardar el evento.")
            return

        self.vista_eventos.insert("", "end", values=(fecha, hora, desc))
        self.entrada_hora.delete(0, tk.END)
        self.entrada_desc.delete(0, tk.END)

    def confirmar_eliminacion(self):
        seleccion = self.vista_eventos.selection()
        if not seleccion:
            messagebox.showinfo("Selecciona un evento", "Debes seleccionar un evento para eliminar.")
            return

        confirmar = messagebox.askyesno("¿Eliminar?", "¿Estás seguro de eliminar el evento seleccionado?")
        if confirmar:
            self.vista_eventos.delete(seleccion)

if __name__ == "__main__":
    raiz = tk.Tk()
    app = AgendaPersonal(raiz)
    raiz.mainloop()
