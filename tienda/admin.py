from django.contrib import admin
from tienda.models import Orden, Producto, Detalle

class DetalleInLine(admin.StackedInline):
    model = Detalle
    extra = 0

class OrdenAdmin(admin.ModelAdmin):
    list_display = ("cliente", "direccion")
    inlines = [DetalleInLine]

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion")

class DetalleAdmin(admin.ModelAdmin):
    list_display = ("orden_link", "producto_link", "cantidad", "precio", "subtotal")
    
    def orden_link(self, obj):
        return obj.orden.cliente
    orden_link.short_description = "Orden"

    def producto_link(self, obj):
        return obj.producto.nombre 
    producto_link.short_description = "Producto"

    def subtotal(self, obj):
        return obj.cantidad * obj.precio 
    subtotal.short_description = "Sub Total"

admin.site.register(Orden, OrdenAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Detalle, DetalleAdmin)