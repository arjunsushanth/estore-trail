from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images', null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
