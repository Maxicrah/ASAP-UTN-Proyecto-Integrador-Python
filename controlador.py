from modelo import Curso
from datetime import date
from peewee import IntegrityError, DoesNotExist
from utils.validaciones import (
    validar_duracion,
    validar_precio,
    validar_fecha,
    validar_autor,
    validar_nombre_curso,
)

# Este controlador se encarga de manejar la lógica de negocio
# para realizar operaciones CRUD de cursos en la base de datos

class CursoControlador:
    """Controlador CRUD para cursos"""

    def crear_curso(self, nombre, autor, precio, duracion, fecha=None):
        """
        Crea un nuevo curso con validaciones y manejo de errores.
        Devuelve una tupla (estado, mensaje)
        """
        try:
            # Validaciones de entrada
            nombre = validar_nombre_curso(nombre, 3, 200)
            autor = validar_autor(autor, 2, 50)
            precio = validar_precio(precio)
            duracion = validar_duracion(duracion)
            fecha = validar_fecha(fecha)

            # despues procesarlos los datos, se los inserta en la base de datos
            curso = Curso.create(
                nombre=nombre.strip(),
                autor=autor.strip(),
                precio=precio,
                duracion=duracion,
                fechaCreacion=fecha,
            )
            # Retornamos confirmacion con el ID generado
            return True, f"Curso '{curso.nombre}' creado con ID {curso.id}"

        #Manejo de erorres comunes
        except IntegrityError:
            #Error para controlar un nombre de curso duplicado
            return False, f"Error: ya existe un curso con ese nombre ({nombre})"
        except ValueError as e:
            #Error de validacion personalizados 
            return False, f"Error de validación: {str(e)}"
        except Exception as e: 
            return False, f"Error inesperado al crear curso: {str(e)}"

    def obtener_cursos(self):
        """
        Obtiene todos los cursos
        Retorna siempre una lista (vacía si no hay registros)
        """
        try:
            cursos = list(Curso.select())
            return cursos  
        except Exception as e:
            # se captura calquier erorr inesperado y se devuelve lista vacía
            print(f"Error al obtener cursos: {str(e)}")
            return []

    def eliminar_curso(self, curso_id):
        """
        Elimina un curso por ID
        Retorna un mensaje con el resultado
        """
        try:
            eliminado = Curso.delete_by_id(curso_id)
            if not eliminado:
                # peewee devuelve 0 si no eliminó ningún registro
                return f"El curso con ID {curso_id} no existe"
            return f"Curso con ID {curso_id} eliminado exitosamente"
        except Exception as e:
            return f"Error al eliminar curso: {str(e)}"

    def editar_curso(self, curso_id, nombre=None, autor=None, precio=None, duracion=None, fecha=None):
        """
        Edita un curso existente con validaciones
        Retorna una tupla (estado, mensaje).
        """
        try:
            # recuperar el curso por ID
            curso = Curso.get_by_id(curso_id)

            # validar y asignar solo los campos recibidos
            if nombre is not None:
                curso.nombre = validar_nombre_curso(nombre, 3, 200)

            if autor is not None:
                curso.autor = validar_autor(autor, 2, 50)

            if precio is not None:
                curso.precio = validar_precio(precio)

            if duracion is not None:
                curso.duracion = validar_duracion(duracion)

            if fecha:
                curso.fechaCreacion = fecha

            # guardar cambios en la base de datos
            curso.save()
            return True, f"Curso con ID {curso.id} actualizado correctamente"

        # manejo de errores
        except DoesNotExist:
            return False, f"No se encontró un curso con ID {curso_id}"
        except IntegrityError:
            return False, f"Error: ya existe un curso con ese nombre ({nombre})"
        except ValueError as e:
            return False, f"Error de validación: {str(e)}"
        except Exception as e:
            return False, f"Error inesperado al editar curso: {str(e)}"
