from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/register', csrf_exempt(views.create_user), name="create_user"),
    path('api/login', csrf_exempt(views.check_login), name="check_login"),
    path('api/users/<int:pk>', csrf_exempt(views.edit_login), name="edit_login"),
    path('api/boards', views.BoardsList.as_view(), name='boards_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/boards/<int:pk>', views.BoardsDetail.as_view(), name='boards_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('api/goods', views.GoodsList.as_view(), name='goods_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/goods/<int:pk>', views.GoodsDetail.as_view(), name='goods_detail'), # api/contacts will be routed to the ContactDetail view for handling
    # This one below is likely unnecessary
    path('api/order', views.OrderList.as_view(),
    name='order_list'),
    # Because you would only need to look at the current order unless you're admin
    path('api/order/<int:pk>', views.OrderDetail.as_view(),
    name='order_detail'),
    path('api/video', views.VideoList.as_view(),
    name='video_list'),
    # This is also likely redundant as these will all be embedded on one page
    path('api/video/<int:pk>', views.VideoDetail.as_view(),
    name='video_detail'),
]
