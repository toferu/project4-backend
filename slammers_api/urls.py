from django.urls import path
from . import views

urlpatterns = [
    path('api/product', views.ProductList.as_view(), name='product_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/product/<int:pk>', views.ProductDetail.as_view(), name='product_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('api/customer', views.CustomerList.as_view(),
    name='customer_list'),
    path('api/customer/<int:pk>', views.CustomerDetail.as_view(),
    name='customer_detail'),
    # This one below is likely unnecessary
    path('api/order', views.OrderList.as_view(),
    name='order_list'),
    # Because you would only need to look at the current order unless you're admin
    path('api/order/<int:pk>', views.OrderDetail.as_view(),
    name='order_detail'),
    path('api/video', views.VideoList.as_view(),
    name='video_list'),
    # This is also likely redundant
    path('api/video/<int:pk>', views.VideoDetail.as_view(),
    name='video_detail'),
]
