from django.urls import path
from . import views

app_name= 'order'

urlpatterns = [
    path('order/', views.order, name='order'),
    path('addtoshopcart/', views.addtoshopcart, name='addtoshopcart'),
    path('shopcart/', views.shopcart, name='shopcart'),
    path('updatequantity/', views.updatequantity, name='updatequantity'),
    path('deletefromcart/<str:id>', views.deletefromcart, name='deletefromcart'),
]
