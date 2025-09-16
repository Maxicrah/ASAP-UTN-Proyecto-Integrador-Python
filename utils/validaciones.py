from datetime import date, datetime
import re

def validar_nombre_curso(nombre: str, min_len: int = 3, max_len: int = 200) -> str:
    """
    Valida el nombre del curso con regex
    - no puede estar vacío
    - debe cumplir cona longitud mínima y máxima
    - solo permite letras, números, espacios, tildes, ñ y algunos simbolos de puntuación
    """

    #verificar que el valor no esté vacío o compuesto solo de espacios
    if not nombre or not nombre.strip():
        raise ValueError("El nombre del curso es obligatorio")

    #Elimina espacios extra al inicio y al final
    nombre = nombre.strip()

    #validar la longitud minima y máxima
    if len(nombre) < min_len:
        raise ValueError(f"El nombre debe tener al menos {min_len} caracteres")
    if len(nombre) > max_len:
        raise ValueError(f"El nombre no puede superar los {max_len} caracteres")

    # expresion regular que restringe los caracteres permitidos
    patron = re.compile(r"^[A-Za-z0-9ÁÉÍÓÚáéíóúÑñ\s:,\.\-\+!%#\(\)/]+$")
    if not patron.match(nombre):
        raise ValueError("El nombre contiene caracteres no permitidos")

    return nombre

def validar_fecha(valor):
    """
    Valida que la fecha sea correcta:
    - si no se pasa, se asigna la fecha de hoy
    - si es un objeto date, se devuelve tal cual
    - si es un string, debe estar en formato YYYY-MM-DD
    """

    if valor is None:
        return date.today()

    if isinstance(valor, date):
        return valor

    if isinstance(valor, str):
        try:
            #intentar convertir el string a objeto date
            return datetime.strptime(valor, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("La fecha debe estar en formato YYYY-MM-DD (ej: 2025-09-16)")

    # si no cumple ninguno de los casos anteriores
    raise ValueError("La fecha debe ser un objeto date o un string válido")

def validar_autor(nombre: str, min_len: int = 2, max_len: int = 50) -> str:
    """
    Valida el nombre del autor con regex
    - no puede estar vacío
    - debe cumplir con una longitud minima y máxima
    - solo permite letras, espacios, tildes, ñ, puntos y guiones
    """
    if not nombre or not nombre.strip():
        raise ValueError("El autor es obligatorio")

    nombre = nombre.strip()

    if len(nombre) < min_len:
        raise ValueError(f"El autor debe tener al menos {min_len} caracteres")
    if len(nombre) > max_len:
        raise ValueError(f"El autor no puede superar los {max_len} caracteres")

    # expresion regular que restringe los caracters a letras, espacios y simbolos
    patron = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s\.\-]+$")
    if not patron.match(nombre):
        raise ValueError("El autor contiene caracteres no permitidos")

    return nombre

def validar_precio(precio: float):
    """
    Valida el precio:
    - no puede ser None
    - no puede ser negativo
    """
    if precio is None or precio < 0:
        raise ValueError("El precio no puede ser negativo")
    return precio


def validar_duracion(duracion: int):
    """
    Valida la duracion del curso:
    - no puede ser None
    - debe ser mayor a 0
    """
    if duracion is None or duracion <= 0:
        raise ValueError("La duración debe ser mayor a 0")
    return duracion
