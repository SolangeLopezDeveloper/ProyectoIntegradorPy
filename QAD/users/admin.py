from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Rol, User, Address, Cart, Order

admin.site.register(Rol)
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(Order)