from django.shortcuts import render, redirect
from .models import Articulo
from .forms import ArticuloForm

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'crear_articulo.html', {'form': form})

def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'lista_articulos.html', {'articulos': articulos})
# Create your views here.
