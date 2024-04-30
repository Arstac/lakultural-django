from django.urls import path
from . import views

app_name = 'carrito' 

urlpatterns = [
    path('', views.carrito, name='carrito'),
    path('add/<int:producto_id>/', views.add_producto, name='add_producto'),
    path('remove/<int:producto_id>/', views.remove_producto, name='remove_producto'),    
]