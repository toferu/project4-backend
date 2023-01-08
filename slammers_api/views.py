from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer, VideoSerializer
from .models import Product, Customer, Order, Video

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json

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


### THIS IS THE FUNCTION THAT PERFORMS AUTH
def check_login(request):
        #IF A GET REQUEST IS MADE, RETURN AN EMPTY {}
    if request.method=='GET':
        return JsonResponse({})

        #CHECK IF A PUT REQUEST IS BEING MADE
    if request.method=='PUT':

        jsonRequest = json.loads(request.body) #make the request JSON format
        email = jsonRequest['email'] #get the email from the request
        password = jsonRequest['password'] #get the password from the request
        if Customer.objects.get(email=email): #see if email exists in db
            user = Customer.objects.get(email=email)  #find user object with matching email
            if check_password(password, user.password): #check if passwords match
                return JsonResponse({'id': user.id, 'email': user.email}) #if passwords match, return a user dict
            else: #passwords don't match so return empty dict
                return JsonResponse({})
        else: #if email doesn't exist in db, return empty dict
            return JsonResponse({})