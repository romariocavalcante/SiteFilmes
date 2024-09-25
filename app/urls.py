from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # login
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path("", views.login, name="login"),
    path("conta/de/<str:id>/user/<str:username>/", views.home, name="home"),
    path("conta/de/<str:id>/", views.whois, name="whois"),
    path('conta/de/<str:id>/createUser/', views.create_user, name='create_user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)