from django.contrib import admin
from .models import *

class DiretorAdmin(admin.ModelAdmin):
    list_display = ('nome',)  
    search_fields = ('nome',)  
    list_filter = ('nome',) 
class AtorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'nacionalidade')  
    search_fields = ('nome', 'nacionalidade')  
    list_filter = ('nome',) 
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)  
    search_fields = ('nome',)  
    list_filter = ('nome',) 
class ClassificacaoAdmin(admin.ModelAdmin):
    list_display = ('classificacao',)  
    search_fields = ('classificacao',)  
    list_filter = ('classificacao',) 
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'diretor', 'duracao','classificacao', 'pais_de_origem', 'idioma', 'ano_de_lancamento')
    search_fields = ('titulo', 'diretor')
    list_filter = ('titulo',)


admin.site.register(Diretor, DiretorAdmin)
admin.site.register(Ator, AtorAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Classificacao, ClassificacaoAdmin)
admin.site.register(Filme, FilmeAdmin)