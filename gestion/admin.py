from django.contrib import admin
from .models import Producto, Empleado

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_barras', 'nombre', 'precio_venta', 'created_at')
    search_fields = ('nombre', 'codigo_barras')
    list_filter = ('created_at',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'documento_identidad', 'rol', 'email')
    search_fields = ('nombre', 'apellido', 'documento_identidad')
    list_filter = ('rol',)
