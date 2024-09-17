from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = LoginUsers.objects.get(usuario=username, senha=password)
            request.session['id'] = user.id
            return redirect('whois', id=user.usuario)
        except LoginUsers.DoesNotExist:
             messages.error(request, 'Nome de usuário ou senha incorretos!')
    return render(request, "login.html")

def logout(request):
    if 'id' in request.session:
        del request.session['id']  # Remove o ID do usuário da sessão
        messages.success(request, 'Você saiu com sucesso.')
    return redirect('login')

def whois(request, id):
    user = get_object_or_404(UsersAccount, usuario=id)
    usuarios = UsersAccount.objects.all()
    return render(request, "whois.html", {'usuarios':usuarios, 'user':user})

def accountUser(request, user_id):
    usuario = get_object_or_404(UsersAccount, user_id=user_id)
    return render(request, "home.html", {'usuario':usuario})