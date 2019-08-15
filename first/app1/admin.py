from django.contrib import admin

# Register your models here.
from .models import Libros,Prestamo,Detalleprestamo,Ejemplar
admin.site.register(Libros)
admin.site.register(Prestamo)
admin.site.register(Detalleprestamo)
admin.site.register(Ejemplar)