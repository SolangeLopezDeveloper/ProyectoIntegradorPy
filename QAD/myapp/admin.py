from django.contrib import admin

from django.contrib import admin
from .models import Product, Event, Category, Medida

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ('title', 'description', 'price', 'categoria_id', 'evento_id', 'medida_id', 'image')
    
    
admin.site.register(Product, ProductAdmin,)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Medida)