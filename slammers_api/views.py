from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BoardsSerializer, GoodsSerializer, CustomerSerializer, OrderSerializer, VideoSerializer
from .models import Boards, Goods, Customer, Order, Video

# from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json


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

### THIS CREATES A USER
def create_user(request):
    if request.method=='GET':
        return JsonResponse({})
    if request.method=='POST':

        newFormData = json.loads(request.body)
        email = newFormData.get('email')
        password = newFormData.get('password')
        # make_password(password)
        newCustomer = Customer(email=email, password=password)
        newCustomer.save()
        id = newCustomer.id
        return JsonResponse({'id': id, 'email': email, 'password': password})

### THIS IS THE FUNCTION THAT PERFORMS AUTH
def check_login(request):
        #IF A GET REQUEST IS MADE, RETURN AN EMPTY {}
    if request.method=='GET':
        return JsonResponse({})

        #CHECK IF A PUT REQUEST IS BEING MADE
    if request.method=='PUT':

        jsonRequest = json.loads(request.body) 
        email = jsonRequest['email'] 
        password = jsonRequest['password'] 
        if Customer.objects.get(email=email): 
            user = Customer.objects.get(email=email)  
            # if check_password(password, user.password): can't get this to work
            if password == user.password:
                return JsonResponse({'id': user.id, 'email': user.email}) 
            else: 
                return JsonResponse({"Match Error": "Passwords do not match"})
        else: 
            return JsonResponse({"Error": "User does not exist"})


### EDIT CUSTOMER LOGIN
def edit_login(request):
    if request.method=='GET':
        return request.body
    if request.method == 'PUT':
        jsonRequest = json.loads(request.body)
        new_email = jsonRequest.get('email')
        new_pass = jsonRequest.get('password')
        # Unsure if this will work but would be cool
        # check_login()

        customer = Customer.objects.get(id=jsonRequest['id'])
        customer.email = new_email
        customer.password = new_pass
        customer.save()
        return JsonResponse({'id': customer.id, 'email': customer.email, 'password': customer.password})


