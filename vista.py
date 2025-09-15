import tkinter as tk
from tkinter import ttk
from controlador import CursoControlador
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

class Ventana(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(padx=10, pady=10)
        self.id_seleccionado = None
        self.crear_labels()
        self.crear_botones()
        self.crear_treeview()
        self.cursoControlador = CursoControlador()
        self.actualizar_treeview()
        self.treeview.bind("<Double-1>", self.on_treeview_select)

    def crear_labels(self):
        # Label nombre curso
        tk.Label(self, text="Nombre Curso").grid(row=0, column=0, sticky="w")
        self.entry_nombre_curso = tk.Entry(self)
        self.entry_nombre_curso.grid(row=0, column=1, sticky="ew")
        # Label autor curso
        tk.Label(self, text="Autor").grid(row=1, column=0, sticky="w")
        self.entry_autor = tk.Entry(self)
        self.entry_autor.grid(row=1, column=1, sticky="ew")
        # Label precio
        tk.Label(self, text="Precio").grid(row=2, column=0, sticky="w")
        self.entry_precio = tk.Entry(self)
        self.entry_precio.grid(row=2, column=1, sticky="ew")
        # Label duracion
        tk.Label(self, text="Duración").grid(row=3, column=0, sticky="w")
        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.grid(row=3, column=1, sticky="ew")
        # Label Fecha
        tk.Label(self, text="Fecha").grid(row=4, column=0, sticky="w")
        self.entry_fecha = DateEntry(self, date_pattern="yyyy-mm-dd")
        self.entry_fecha.grid(row=4, column=1, sticky="ew")

    def crear_botones(self):
        self.btn_agregar = tk.Button(self, text="Agregar curso", command=self.vista_agregar_curso)
        self.btn_agregar.grid(row=5, column=0, pady=5)
        self.btn_actualizar = tk.Button(self, text="Actualizar curso", command=self.vista_actualizar_curso)
        self.btn_actualizar.grid(row=5, column=1, pady=5)
        self.btn_eliminar = tk.Button(self, text="Eliminar", command=self.vista_eliminar_curso)
        self.btn_eliminar.grid(row=5, column=2, pady=5)

    def crear_treeview(self):
        self.treeview = ttk.Treeview(
            self,
            columns=("id", "curso", "autor", "precio", "duracion", "fecha"),
            show="headings",
        )
        self.treeview.grid(row=6, column=0, columnspan=3, pady=10, sticky="ew")
        # Definimos nombres para las columnas
        self.treeview.heading("id", text="ID")
        self.treeview.heading("curso", text="Curso")
        self.treeview.heading("autor", text="Autor")
        self.treeview.heading("precio", text="Precio")
        self.treeview.heading("duracion", text="Duracion")
        self.treeview.heading("fecha", text="Fecha")
        # Definimos tamanio columnas
        self.treeview.column("id", width=50, anchor="center")
        self.treeview.column("curso", width=100)
        self.treeview.column("autor", width=100)
        self.treeview.column("precio", width=150)
        self.treeview.column("duracion", width=150)
        self.treeview.column("fecha", width=80, anchor="e")
        # Definimos accion para seleccionar dato del treeview para editar, eliminar, etc.
        # implementacion falta
        self.columnconfigure(1, weight=1)

    def actualizar_treeview(self):
        # limpiar treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # cargar cursos desde el controlador
        cursos = self.cursoControlador.obtener_cursos()

        # Insertar en el treeview
        for curso in cursos:
            self.treeview.insert(
                "",
                "end",
                values=(
                    curso.id,
                    curso.nombre,
                    curso.autor,
                    curso.precio,
                    curso.duracion,
                    curso.fechaCreacion,
                ),
            )

    def vista_actualizar_curso(self):
        if self.id_seleccionado is None:
            messagebox.showerror("Error de selección", "Seleccione un curso del Treeview para actualizar.")
            return

        # Tomar datos de los inputs
        nombreCurso = self.entry_nombre_curso.get()
        autor = self.entry_autor.get()
        precio = self.entry_precio.get()
        duracion = self.entry_duracion.get()
        fecha = self.entry_fecha.get()

        try:
            precio = float(precio)
            duracion = int(duracion)
        except ValueError:
            messagebox.showerror("Error de validación", "Precio debe ser número y duración un entero")
            return

        # Llamar al controlador
        exito, mensaje = self.cursoControlador.editar_curso(
            self.id_seleccionado, nombreCurso, autor, precio, duracion, fecha
        )

        # Mostrar mensaje y actualizar treeview si es exitoso
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.actualizar_treeview()
            self.limpiar_campos()
            self.id_seleccionado = None
        else:
            messagebox.showerror("Error", mensaje)


    def vista_agregar_curso(self):
        #pasale los datos directamente, el contolador no deberia de hacer .get()
        nombreCurso = self.entry_nombre_curso.get()
        autor = self.entry_autor.get()
        precio = self.entry_precio.get()
        duracion = self.entry_duracion.get()
        fecha = self.entry_fecha.get()

        try:
            precio = float(precio)
            duracion = int(duracion)
        except ValueError:
            messagebox.showerror("Error de validación", "Precio debe ser número y duración un entero")
            return

        # Llamar al controlador
        exito, mensaje = self.cursoControlador.crear_curso(nombreCurso, autor, precio, duracion, fecha)

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.actualizar_treeview()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", mensaje)
    
    def limpiar_campos(self):
        self.entry_nombre_curso.delete(0, tk.END)        
        self.entry_autor.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_duracion.delete(0, tk.END)
        self.entry_fecha.set_date(datetime.today().date())
    
    def vista_eliminar_curso(self):
        seleccion = self.treeview.selection()  # devuelve tupla de items seleccionados en el Treeview

        if seleccion:
            # Tomamos el primer item seleccionado
            item_id = seleccion[0]
            valores = self.treeview.item(item_id, "values")  # trae los valores de la fila
            curso_id = valores[0]  # el id está en la primera columna

            # Ejecutamos eliminación en el controlador
            resultado = self.cursoControlador.eliminar_curso(int(curso_id))

            # Mostramos mensaje en un messagebox
            if "exitosamente" in resultado.lower():
                messagebox.showinfo(title="Curso eliminado", message=resultado)
                self.actualizar_treeview()
            else:
                messagebox.showerror(title="Error", message=resultado)
        else:
            messagebox.showerror(
                title="Error de selección",
                message="Seleccione un curso para eliminarlo."
            )

    def on_treeview_select(self, event):
        seleccion = self.treeview.selection()
        if seleccion:
            item_id = seleccion[0]
            valores = self.treeview.item(item_id, "values")
            self.id_seleccionado = int(valores[0])
            #rellenar inputs automáticamente
            self.entry_nombre_curso.delete(0, tk.END)
            self.entry_nombre_curso.insert(0, valores[1])
            self.entry_autor.delete(0, tk.END)
            self.entry_autor.insert(0, valores[2])
            self.entry_precio.delete(0, tk.END)
            self.entry_precio.insert(0, valores[3])
            self.entry_duracion.delete(0, tk.END)
            self.entry_duracion.insert(0, valores[4])
            try:
                fecha = datetime.strptime(valores[5], "%Y-%m-%d").date()
                self.entry_fecha.set_date(fecha)
            except Exception:
                # Si falla el parseo, cargo la fecha de hoy
                self.entry_fecha.set_date(datetime.today().date())