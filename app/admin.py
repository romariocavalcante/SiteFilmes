from django.contrib import admin
from .models import *
from django.utils.html import format_html

class LoginUsersAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'usuario', 
    'senha'
  )
  search_fields = (
    'usuario', 
    'senha',
  )
class GenerosAdmin(admin.ModelAdmin):
  list_display = (
    'id', 
    'genero'
  )
class UsersAccountAdmin(admin.ModelAdmin):
  list_display = (
    'id', 
    'usuario', 
    'image'
  )
class FilmesAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'titulo', 
    'descricao', 
    'data_lancamento', 
    'duracao', 
    'lista_generos', 
    'diretor', 
    'elenco', 
    'classificacao', 
    'imagem', 
    'linguagem', 
    'pais_de_origem'
  )
  search_fields = (
    'id',
    'titulo', 
    'diretor',
    'genero'
  )

  filter_horizontal = ('genero',)

class SeriesAdmin(admin.ModelAdmin):
  list_display = (
    'titulo', 
    'descricao', 
    'data_lancamento', 
    'n_temporadas', 
    'n_episodios',
    'lista_generos',  
    'diretor', 
    'elenco', 
    'classificacao', 
    'imagem', 
    'linguagem', 
    'pais_de_origem'
  )
  search_fields = (
    'titulo', 
    'diretor',
    'genero'
  )


    

admin.site.register(LoginUsers, LoginUsersAdmin)
admin.site.register(Generos, GenerosAdmin)
admin.site.register(UsersAccount, UsersAccountAdmin)
admin.site.register(Filmes, FilmesAdmin)
admin.site.register(Series, SeriesAdmin)