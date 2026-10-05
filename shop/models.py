from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,default='pending')

    def __str__(self):
        return self.order_date

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.order

