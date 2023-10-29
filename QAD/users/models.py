from django.db import models

# Create your models here.
class Rol(models.Model):
    name = models.CharField(max_length=50)

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    roles = models.ManyToManyField(Rol, related_name="users")
    # Otros campos relevantes para el usuario

class Address(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='address')
    street = models.CharField(max_length=255, default='Calle')
    city = models.CharField(max_length=255, default='Ciudad')
    country = models.CharField(max_length=255, default='País')

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    items = models.ManyToManyField('Product', through='CartProduct')

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    items = models.ManyToManyField('Product', through='OrderProduct')
    total = models.DecimalField(max_digits=10, decimal_places=2)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()