from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Pessoa
 
def ver_produtos(request):
    if request.method == 'GET':

        return render(request, 'ver_produto.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        
        return HttpResponse("Fui chamado")

    

#def inserir_produto(request):
    #return HttpResponse("estou no inserir")


