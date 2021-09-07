from django.urls import path
from shortener import views


urlpatterns = [
    path('encode', views.encode),
    path('decode', views.decode),
]
