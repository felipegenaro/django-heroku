from django.shortcuts import render
from catalogo.models import Filme

# Create your views here.

def catalogo_view(request):
        filmes = Filme.objects.all()

        context = {
                'filmes': filmes
        }
        return render(request, 'catalogo.html', context)
        