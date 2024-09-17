from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = LoginUsers.objects.get(usuario=username, senha=password)
            user.save()
            return redirect('whois')
        except LoginUsers.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')
    return render(request, "login.html")

def whois(request, id):
    user = get_object_or_404(UsersAccount, id=id)
    usuarios = UsersAccount.objects.all()
    return render(request, "whois.html", {'usuarios':usuarios, 'user':user})

def accountUser(request, user_id):
    usuario = get_object_or_404(UsersAccount, user_id=user_id)
    return render(request, "home.html", {'usuario':usuario})