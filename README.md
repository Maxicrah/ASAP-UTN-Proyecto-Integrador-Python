# CRUD de Cursos con Python, Peewee y Tkinter

## Integrantes
- Maximiliano Ramiro Flores
- Ramiro Galvan

## Descripción

Este proyecto es una aplicación de escritorio para **gestionar cursos**, desarrollada en Python usando:

* **Peewee**: ORM ligero para manejar la base de datos SQLite.
* **Tkinter**: Interfaz gráfica para agregar, ver, editar y eliminar cursos.
* **MVC**: Arquitectura Modelo-Vista-Controlador para separar la lógica de negocio, la interfaz y los datos.

Cada curso tiene los siguientes campos:

| Campo         | Tipo         | Restricciones                          |
| ------------- | ------------ | -------------------------------------- |
| id            | AutoField    | Clave primaria autoincremental         |
| nombre        | CharField    | Obligatorio, único, max 200 caracteres |
| autor         | CharField    | Obligatorio, max 50 caracteres         |
| precio        | DecimalField | Obligatorio, ≥ 0, 2 decimales          |
| duracion      | IntegerField | Obligatorio, > 0                       |
| fechaCreacion | DateField    | Fecha del curso, por defecto hoy       |

---

## Requisitos

* Python 3.11+
* Librerías:

  * peewee
  * tkinter (viene con Python)

Instalación de dependencias:

```bash
pip install peewee
```

---

## Estructura del proyecto

```
.
├── models.py        # Define la tabla Curso y la conexión a la DB
├── controllers.py   # Lógica CRUD de los cursos
├── views.py         # Interfaz gráfica con Tkinter
├── main.py          # Punto de entrada de la aplicación
└── cursos.db        # Base de datos SQLite generada automáticamente
```

---

## Cómo usar

1. Clonar el repositorio:

```bash
git clone https://github.com/Maxicrah/ASAP-UTN-Proyecto-Integrador-Python.git
cd ASAP-UTN-Proyecto-Integrador-Python
```

2. Ejecutar la aplicación:

```bash
python main.py
```

3. Usar la interfaz para:

* Agregar cursos llenando el formulario y presionando "Agregar Curso".
* Ver todos los cursos en la lista.
* Editar un curso (en futuras versiones puede implementarse).
* Eliminar un curso (en futuras versiones puede implementarse).

---
