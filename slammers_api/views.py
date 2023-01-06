from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer, VideoSerializer
from .models import Product, Customer, Order, Video

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ProductSerializer # tell django what serializer to use

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer

class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all().order_by('id')
    serializer_class = VideoSerializer

class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all().order_by('id')
    serializer_class = VideoSerializer