from modelo import Curso

#TODO: Agregar validaciones/logica
class CursoControlador:
    """Controlador CRUD para cursos"""

    def crear_curso(self, nombre, autor, precio, duracion, fecha=None):
        """Crea un nuevo curso"""
        return Curso.create(
            nombre=nombre,
            autor=autor,
            precio=precio,
            duracion=duracion,
            fechaCreacion=fecha
        )

    def obtener_cursos(self):
        """Obtiene todos los cursos"""
        return list(Curso.select())