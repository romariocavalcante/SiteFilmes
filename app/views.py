from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from functools import wraps
from .models import *


def login_required(view_func):
    """Decorator para verificar se o usuário está logado"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if "id" not in request.session:
            return redirect("login")
        
        try:
            user = LoginUsers.objects.get(id=request.session["id"])
            request.user = user  # Adicionar o usuário ao request
        except LoginUsers.DoesNotExist:
            if "id" in request.session:
                del request.session["id"]
            return redirect("login")
        
        return view_func(request, *args, **kwargs)
    return wrapper


def login(request):
    if request.method == "POST":
        # Verificar se é um login ou cadastro
        if 'reg_username' in request.POST:
            # Processar cadastro
            return process_register(request)
        else:
            # Processar login
            return process_login(request)
    
    return render(request, "login.html")


def process_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    try:
        user = LoginUsers.objects.get(usuario=username, senha=password)
        request.session["id"] = user.id
        return redirect("whois")
    except LoginUsers.DoesNotExist:
        messages.error(request, "Nome de usuário ou senha incorretos!")
    return render(request, "login.html")


def process_register(request):
    username = request.POST.get("reg_username")
    email = request.POST.get("reg_email")
    password = request.POST.get("reg_password")
    confirm_password = request.POST.get("reg_confirm_password")
    terms = request.POST.get("terms")
    
    # Validações
    if not terms:
        messages.error(request, "Você deve aceitar os termos de uso!")
        return render(request, "login.html")
    
    if password != confirm_password:
        messages.error(request, "As senhas não coincidem!")
        return render(request, "login.html")
    
    if len(password) < 6:
        messages.error(request, "A senha deve ter pelo menos 6 caracteres!")
        return render(request, "login.html")
    
    # Verificar se o usuário já existe
    if LoginUsers.objects.filter(usuario=username).exists():
        messages.error(request, "Nome de usuário já existe!")
        return render(request, "login.html")
    
    # Verificar se o email já existe
    if LoginUsers.objects.filter(email=email).exists():
        messages.error(request, "E-mail já cadastrado!")
        return render(request, "login.html")
    
    # Criar novo usuário
    try:
        new_user = LoginUsers(
            usuario=username,
            email=email,
            senha=password
        )
        new_user.save()
        messages.success(request, "Conta criada com sucesso! Faça login para continuar.")
    except Exception as e:
        messages.error(request, "Erro ao criar conta. Tente novamente.")
    
    return render(request, "login.html")


def logout(request):
    if "id" in request.session:
        del request.session["id"]  # Remove o ID do usuário da sessão
        messages.success(request, "Você saiu com sucesso.")
    return redirect("login")


@login_required
def whois(request):
    usuarios = UsersAccount.objects.filter(login_user=request.user)
    return render(
        request, "whois.html", {"login_user": request.user, "usuarios": usuarios}
    )


@login_required
def create_user(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        image = request.FILES.get("image")

        novo_usuario = UsersAccount(usuario=usuario, image=image, login_user=request.user)
        novo_usuario.save()

        return redirect("whois")

    return render(request, "create_user.html", {"user": request.user})


@login_required
def home(request, username):
    # Buscar o usuário específico pelo username
    try:
        usuario = UsersAccount.objects.get(usuario=username)
    except UsersAccount.DoesNotExist:
        # Se o usuário não existir, redirecionar para whois
        return redirect('whois')
    
    # Buscar filmes e séries do banco de dados
    filmes = Filmes.objects.all()[:10]  # Limitar a 10 filmes
    series = Series.objects.all()[:10]  # Limitar a 10 séries
    
    context = {
        'filmes': filmes,
        'series': series,
        'username': username,
        'usuario': usuario  # Passar o objeto usuário completo com a imagem
    }
    
    return render(request, "home.html", context)


@login_required
def filme(request):
    # Buscar filmes do banco de dados
    filmes = Filmes.objects.all()[:20]  # Limitar a 20 filmes
    
    context = {
        'filmes': filmes
    }
    
    return render(request, "filme.html", context)


@login_required
def serie(request):
    # Buscar séries do banco de dados
    series = Series.objects.all()[:20]  # Limitar a 20 séries
    
    context = {
        'series': series
    }
    
    return render(request, "serie.html", context)


@login_required
def termos_uso(request):
    """View para a página de Termos de Uso"""
    return render(request, "termos_uso.html")


@login_required
def politica_privacidade(request):
    """View para a página de Política de Privacidade"""
    return render(request, "politica_privacidade.html")
