from datetime import date  
from peewee import SqliteDatabase, Model, AutoField, IntegerField, DateField, CharField, DecimalField, Check

db = SqliteDatabase("cursos.db")

# Creamos una clase base que hereda de peewee.Model
# La usamos para que todos los modelos compartan la misma configuración de base de datos
class BaseModel(Model):
    class Meta:
        database = db  # Todos los modelos que hereden de BaseModel usarán esta base de datos

# Representa la tabla "curso" en la base de datos
class Curso(BaseModel):
    id = AutoField() # ID autoincremental
    
    # nombre: texto obligatorio, máximo 200 caracteres, único
    nombre = CharField(
        null=False, 
        max_length=200, 
        unique=True,        # no permite duplicados
        collation="NOCASE"  # ignora mayusculas/minusculas
        )
    
    # autor: texto obligatorio, máximo 50 caracteres
    autor = CharField(null=False, max_length=50, collation="NOCASE")
    
    # precio: número decimal obligatorio, máximo 10 dígitos, 2 decimales
    # default=0.00 y constraint para que nunca sea negativo
    precio = DecimalField(
        null=False, 
        max_digits=10, 
        decimal_places=2, 
        default=0.00, 
        constraints=[Check("precio >= 0")] #Nunca negativo
    )
    
    duracion = IntegerField(
        default=1,
        constraints=[Check("duracion > 0")] #Siempre mayor a 0
    )
    
    fechaCreacion = DateField(default=date.today) #fecha por defecto hoy

# Conecta a la base de datos
# Crea la tabla 'Curso' si no existe, usando la definición del modelo
db.connect()
db.create_tables([Curso])