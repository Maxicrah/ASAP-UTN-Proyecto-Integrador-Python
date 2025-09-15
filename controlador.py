from modelo import Curso

#TODO: traspasar mensajes try except raise
#TODO: Agregar validaciones/logica
class CursoControlador:
    """Controlador CRUD para cursos"""

    def crear_curso(self, nombre, autor, precio, duracion, fecha):
        """Crea un nuevo curso"""
        return Curso.create(
            nombre=nombre,
            autor=autor,
            precio=precio,
            duracion=duracion,
            fechaCreacion=fecha,
        )

    def obtener_cursos(self):
        """Obtiene todos los cursos"""
        return list(Curso.select())

    def eliminar_curso(self, curso_id):
        """Borra el curso con el ID """
        curso_borrado = Curso.delete_by_id(curso_id)
        if(not curso_borrado):
            return f"El ID ingresado: {curso_id} inexistente"
        else:
            return "Curso eliminado exitosamente!"


