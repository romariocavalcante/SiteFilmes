from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # login
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path("", views.login, name="login"),
    path("home/", views.accountUser, name="home"),
    path("conta/de/<str:id>/", views.whois, name="whois"),
    # path("conta/de/<str:id>/usuario/<str:id>", views.user, name="user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)