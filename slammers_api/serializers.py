from rest_framework import serializers 
from .models import Product, Customer, Order, Video 


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'price', 'description')

class CustomerSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Customer # tell django which model to use
        fields = ('id', 'email', 'password',) # tell django which fields to include

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'customer', 'product', 'date_created' )
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'link', 'description')
