from django.db import models


# Create your models here.
class Libros (models.model):
    nombre=models.CharField(max_length=45)
    descripcion= models.CharField(max_length=45)
    isbn=models.CharField(max_length=45)

class Ejemplar (models.model):
    numeroejemplare=models.CharField(max_length=45)
    fechadecompra= models.CharField(max_length=45)
    id_Libros = models.ForeignKey(Libros,on_delete=models.CASCADE)
class Prestamo (models.model):
    fechaprestamo=models.CharField(max_length=45)
    nombrecliente=models.CharField(max_length=45)
    telefonocliente=models.CharField(max_length=45)
    estado=models.BooleanField(default=True,editable=False)
class Detalleprestamo (models.model):
    id_Libros = models.ForeignKey(Libros, on_delete=models.CASCADE)
    id_prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)