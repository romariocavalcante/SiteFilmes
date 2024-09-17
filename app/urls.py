from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.login, name="login"),
    path("home/", views.accountUser, name="home"),
    path("whois/<int:id>/", views.whois, name="whois"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)