from modelo import Curso
from datetime import date
from peewee import IntegrityError, DoesNotExist

#TODO: traspasar mensajes try except raise
#TODO: Agregar validaciones/logica

class CursoControlador:
    """Controlador CRUD para cursos"""

    def crear_curso(self, nombre, autor, precio, duracion, fecha=None):
        """Crea un nuevo curso con validaciones y manejo de errores"""
        try:
            # Validaciones previas
            if not nombre or not autor:
                raise ValueError("El nombre y el autor son obligatorios")
            if precio < 0:
                raise ValueError("El precio no puede ser negativo")
            if duracion <= 0:
                raise ValueError("La duración debe ser mayor a 0")
            if fecha is None:
                fecha = date.today()

            curso = Curso.create(
                nombre=nombre.strip(),
                autor=autor.strip(),
                precio=precio,
                duracion=duracion,
                fechaCreacion=fecha,
            )
            # Retornamos un tuple: (estado, mensaje)
            return True, f"Curso '{curso.nombre}' creado con ID {curso.id}"

        except IntegrityError:
            return False, f"Error: ya existe un curso con ese nombre ({nombre})"
        except ValueError as e:
            return False, f"Error de validación: {str(e)}"
        except Exception as e:
            return False, f"Error inesperado al crear curso: {str(e)}"

    def obtener_cursos(self):
        """Obtiene todos los cursos"""
        try:
            cursos = list(Curso.select())
            return cursos  # Siempre una lista, vacía si no hay registros
        except Exception as e:
            print(f"Error al obtener cursos: {str(e)}")
            return []

    def eliminar_curso(self, curso_id):
        """Elimina un curso por ID"""
        try:
            eliminado = Curso.delete_by_id(curso_id)
            if not eliminado:
                return f"El curso con ID {curso_id} no existe"
            return f"Curso con ID {curso_id} eliminado exitosamente"
        except Exception as e:
            return f"Error al eliminar curso: {str(e)}"

    def editar_curso(self, curso_id, nombre=None, autor=None, precio=None, duracion=None, fecha=None):
        """Edita un curso existente con validaciones"""
        try:
            curso = Curso.get_by_id(curso_id)

            if nombre is not None:
                if not nombre.strip():
                    raise ValueError("El nombre no puede estar vacío")
                curso.nombre = nombre.strip()

            if autor is not None:
                if not autor.strip():
                    raise ValueError("El autor no puede estar vacío")
                curso.autor = autor.strip()

            if precio is not None:
                if precio < 0:
                    raise ValueError("El precio no puede ser negativo")
                curso.precio = precio

            if duracion is not None:
                if duracion <= 0:
                    raise ValueError("La duración debe ser mayor a 0")
                curso.duracion = duracion

            if fecha:
                curso.fechaCreacion = fecha

            curso.save()
            return True, f"Curso con ID {curso.id} actualizado correctamente"

        except DoesNotExist:
            return False, f"No se encontró un curso con ID {curso_id}"
        except IntegrityError:
            return False, f"Error: ya existe un curso con ese nombre ({nombre})"
        except ValueError as e:
            return False, f"Error de validación: {str(e)}"
        except Exception as e:
            return False, f"Error inesperado al editar curso: {str(e)}"
