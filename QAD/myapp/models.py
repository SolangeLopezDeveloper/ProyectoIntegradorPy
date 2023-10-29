from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.

class Category(models.Model):  # Categorías de los productos
    name = models.CharField(verbose_name="Categoria", max_length=50)
    description = models.TextField(verbose_name="Descripcion", default="Categoría Nueva")
    image= models.ImageField(upload_to="productos", null=True, blank=True, verbose_name="Imagen")
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.name
    
class Event(models.Model):  # A qué evento corresponde el producto
    name = models.CharField(verbose_name="Evento", max_length=50)
    description = models.TextField(verbose_name="Descripcion", default="Días especiales")
    image= models.ImageField(upload_to="productos", null=True, blank=True, verbose_name="Imagen")
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
    
    def __str__(self):
        return self.name
    
class Medida(models.Model): # Cual es el tamaño del producto
    name = models.CharField(verbose_name="Medida", max_length=50)
    description = models.TextField(verbose_name="Descripcion",default="S - 15/25 personas")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Medida"
        verbose_name_plural = "Medidas"
    
    def __str__(self):
        return self.name


class Product(models.Model): 
    title = models.CharField(verbose_name="Producto", max_length=50)
    description = models.TextField(verbose_name="Descripcion")
    price= models.IntegerField(verbose_name="Precio")
    categoria_id = models.ForeignKey(Category, verbose_name="Categoria", on_delete=models.CASCADE)
    evento_id= models.ForeignKey(Event, verbose_name="Evento",on_delete=models.CASCADE)
    medida_id= models.ForeignKey(Medida, verbose_name="medida",on_delete=models.CASCADE,null=True)
    image= models.ImageField(upload_to="productos", null=True, blank=True, verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    categoria_choices = [
        (1, "Tortas"),
        (2, "Desayunos"),
        (3, "Tartas"),
        (4, "Catering")
    ]

    evento_choices = [
        (1, "Días Especiales"),
        (2, "Cumpleaños Infantiles"),
        (3, "Quince Años"),
        (4, "Casamientos"),
        (5, "Eventos empresariales")
    ]

    medida_choices = [
        (1, "S - 15/25 personas"),
        (2, "M - 25/35 personas"),
        (3, "L - 35/50 personas"),
        (4, "XL - 50/100 personas"),
        (5, "XXL - 100/300 personas")
    ]
    
    class Meta:
            verbose_name= "Producto"
            verbose_name_plural= "Productos"
    
    def __str__(self):
        return self.title

    @admin.display(ordering="title")
    def producto(self):
            return format_html(f"<span style='color:red;'>{self.title}</span>")
        
    @admin.display(ordering="description")
    def descripcion(self):
        return format_html(self.description[:150]+"...")  
    
"""  MEDIDA = [
        (1, "S - 15/25 personas"),
        (2, "M - 25/35 personas"),
        (3, "L - 35/50 personas"),
        (4, "XL - 50/100 personas"),
        (5, "XXL - 100/300 personas")
        
    ]
    medida = models.PositiveSmallIntegerField(choices=MEDIDA) """
