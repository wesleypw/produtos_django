from django.shortcuts import render
from django.http import HttpResponse
 
def ver_produtos(request):
    # nome = 'caio'
    return render(request, 'ver_produto.html', {'nome':'caio'})
    

def inserir_produto(request):
    return HttpResponse("estou no inserir")


