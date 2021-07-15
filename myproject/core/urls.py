from django.urls import path
from core import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('contacto/', views.contact, name='contact'),
    path('hacemos/', views.hacemos, name='hacemos'),
]
