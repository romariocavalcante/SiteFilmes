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
    login_user = get_object_or_404(UsersAccount, login_user=id)
    usuarios = UsersAccount.objects.all()
    return render(request, "whois.html", {'login_user':login_user, 'usuarios':usuarios})

def accountUser(request, user_id):
    usuario = get_object_or_404(UsersAccount, user_id=user_id)
    return render(request, "home.html", {'usuario':usuario})

def create_user(request, id):
    user = get_object_or_404(UsersAccount, usuario=id)
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        imagem = request.FILES.get('imagem')

        novo_usuario = UsersAccount(usuario=usuario, imagem=imagem)
        
        novo_usuario.save()

        return redirect('whois')

    return render(request, 'create_user.html', {'user':user})

def home(request, id, username):
    account = get_object_or_404(LoginUsers, usuario=id)
    user = get_object_or_404(UsersAccount, usuario=username)
    return render(request, 'home.html', {'account': account, 'user': user})