from django.urls import path
from . import views

app_name = 'eventos' 

urlpatterns = [
    path('', views.eventos, name='eventos'),
]