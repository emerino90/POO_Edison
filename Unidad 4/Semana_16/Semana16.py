import tkinter as tk
from tkinter import font

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Tareas")
        self.master.geometry("420x450")

        self.task_var = tk.StringVar()

        # Entrada para nueva tarea
        self.entry = tk.Entry(master, textvariable=self.task_var, width=30)
        self.entry.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry.bind("<Return>", self.add_task)

        # Botón para añadir
        self.btn_add = tk.Button(master, text="Añadir", width=10, command=self.add_task)
        self.btn_add.grid(row=0, column=1, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(master, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Fuente para tareas completadas
        self.normal_font = font.Font(self.task_listbox, self.task_listbox.cget("font"))
        self.completed_font = self.normal_font.copy()
        self.completed_font.configure(slant="italic", overstrike=1)

        # Botones
        self.btn_complete = tk.Button(master, text="Completar", width=15, command=self.complete_task)
        self.btn_complete.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.btn_delete = tk.Button(master, text="Eliminar", width=15, command=self.delete_task)
        self.btn_delete.grid(row=2, column=1, padx=10, pady=5, sticky="e")

        # Atajos de teclado
        self.master.bind("<c>", self.complete_task)
        self.master.bind("<C>", self.complete_task)
        self.master.bind("<d>", self.delete_task)
        self.master.bind("<D>", self.delete_task)
        self.master.bind("<Escape>", lambda event: master.quit())

    def add_task(self, event=None):
        task = self.task_var.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            index = self.task_listbox.size() - 1
            self.task_listbox.itemconfig(index, fg="black", font=self.normal_font)
            self.task_var.set("")

    def complete_task(self, event=None):
        try:
            index = self.task_listbox.curselection()[0]
            current_text = self.task_listbox.get(index)
            # Verificamos si ya está completada (fuente tachada)
            current_font = self.task_listbox.itemcget(index, "font")

            if current_font == str(self.normal_font):
                # Marcar como completada
                self.task_listbox.itemconfig(index, fg="gray", font=self.completed_font)
            else:
                # Desmarcar
                self.task_listbox.itemconfig(index, fg="black", font=self.normal_font)
        except IndexError:
            pass

    def delete_task(self, event=None):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
        except IndexError:
            pass

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
