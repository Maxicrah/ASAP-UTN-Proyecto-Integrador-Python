import tkinter as tk
from tkinter import ttk

class Ventana(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.grid(padx=10,pady=10)
        self.id_seleccionado = None
        self.crear_labels()
        self.crear_botones()
        self.crear_treeview()
        #self.actualizar()
    
    def crear_labels(self):
        #Label nombre curso
        tk.Label(self, text="Nombre Curso").grid(row=0, column=0, sticky="w")
        self.entry_nombre_curso = tk.Entry(self)
        self.entry_nombre_curso.grid(row=0, column=1, sticky="ew")
        #Label autor curso
        tk.Label(self, text="Autor").grid(row=1, column=0, sticky="w")
        self.entry_autor = tk.Entry(self)
        self.entry_autor.grid(row=1, column=1, sticky="ew")
        #Label precio
        tk.Label(self, text="Precio").grid(row=2, column=0, sticky="w")
        self.entry_precio = tk.Entry(self)
        self.entry_precio.grid(row=2, column=1, sticky="ew")
        #Label duracion
        tk.Label(self, text="Duración").grid(row=3, column=0, sticky="w")
        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.grid(row=3, column=1, sticky="ew")
        #Label Fecha
        tk.Label(self, text="Fecha").grid(row=4, column=0, sticky="w")
        self.entry_fecha = tk.Entry(self)
        self.entry_fecha.grid(row=4, column=1, sticky="ew")
    
    def crear_botones(self):
        self.btn_agregar = tk.Button(self, text = "Agregar curso", command=None)
        self.btn_agregar.grid(row=5, column=0, pady=5)
        self.btn_actualizar = tk.Button(self, text="Actualizar curso", command=None)
        self.btn_actualizar.grid(row=5, column=1, pady=5)
        self.btn_eliminar = tk.Button(self, text="Eliminar", command=None)
        self.btn_eliminar.grid(row=5, column=2, pady=5)

    def crear_treeview(self):
        self.treeview = ttk.Treeview(self, columns=("id", "curso", "autor", "precio", "duracion", "fecha"), show="headings")
        self.treeview.grid(row=5, column=0, columnspan=3, pady=10, sticky="ew")
        #Definimos nombres para las columnas
        self.treeview.heading("id", text="ID")
        self.treeview.heading("curso", text="Curso")
        self.treeview.heading("autor", text="Autor")
        self.treeview.heading("precio", text="Precio")
        self.treeview.heading("duracion", text="Duracion")
        self.treeview.heading("fecha", text="Fecha")
        #Definimos tamanio columnas
        self.treeview.column("id", width=50, anchor="center")
        self.treeview.column("curso", width=100)
        self.treeview.column("autor", width=100)
        self.treeview.column("precio", width=150)
        self.treeview.column("duracion", width=150)
        self.treeview.column("fecha", width=80, anchor="e")
        #Definimos accion para seleccionar dato del treeview para editar, eliminar, etc.
        #implementacion falta
        self.columnconfigure(1,weight=1)

