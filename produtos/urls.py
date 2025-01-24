from django.urls import path
from . import views

urlpatterns = [
    path('ver_produto/', views.ver_produtos, name='ver_produtos'),
    path("inserir_produto/", views.inserir_produto, name="inserir_produto"),
]