from django.shortcuts import render
from theater.models import Categoria
# Create your views here.
categorias = [Categoria('Humor', ''), Categoria('Drama', '')]

def index(request):
    return render(request, "index.html", context={'categorias': categorias})