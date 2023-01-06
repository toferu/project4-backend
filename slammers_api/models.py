from django.db import models

# Create your models here.
class Boards(models.Model):
    name = models.CharField(max_length=64, null=True)
    image = models.URLField(max_length=250, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=1000, null=True, blank=True)

class Goods(models.Model):
    name = models.CharField(max_length=64, null=True)
    image = models.URLField(max_length=250, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=1000, null=True, blank=True)

class Customer(models.Model):
    name = models.CharField(max_length=24, null=True)
    password = models.CharField(max_length=32, null=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    boards = models.ForeignKey(Boards, null=True, on_delete=models.SET_NULL)
    goods = models.ForeignKey(Goods, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Video(models.Model):
    link = models.URLField(max_length=250, null=True)
    description = models.CharField(max_length=88, null=True, blank=True)