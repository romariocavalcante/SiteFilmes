from django.shortcuts import render
from .models import *


def index(request):
    filmes = Filme.objects.all()
    for f in filmes:
        print(f.video.url)
    return render(request, 'index.html', {'filmes': filmes})
