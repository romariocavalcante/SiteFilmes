from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # login
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path("", views.login, name="login"),
    path("selecionar_usuario", views.whois, name="whois"),
    path('criar_usuario/', views.create_user, name='create_user'),
    path("conta/de/<str:username>/", views.home, name="home"),
    
    # filmes e séries
    path("filmes/", views.filme, name="filme"),
    path("series/", views.serie, name="serie"),
    
    # páginas legais
    path("termos-de-uso/", views.termos_uso, name="termos_uso"),
    path("politica-de-privacidade/", views.politica_privacidade, name="politica_privacidade"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)