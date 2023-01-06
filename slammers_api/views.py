from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BoardsSerializer, GoodsSerializer, CustomerSerializer, OrderSerializer, VideoSerializer
from .models import Boards, Goods, Customer, Order, Video

class BoardsList(generics.ListCreateAPIView):
    queryset = Boards.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = BoardsSerializer # tell django what serializer to use

class BoardsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boards.objects.all().order_by('id')
    serializer_class = BoardsSerializer

class GoodsList(generics.ListCreateAPIView):
    queryset = Goods.objects.all().order_by('id') 
    serializer_class = GoodsSerializer 

class GoodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer

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