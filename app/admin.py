from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.db.models import Count, Avg, Q
from django.contrib.admin import SimpleListFilter
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta
from .models import *
from .admin_actions import *

# ==================== FILTROS PERSONALIZADOS ====================

class DataLancamentoFilter(SimpleListFilter):
    title = 'Data de Lançamento'
    parameter_name = 'data_lancamento'

    def lookups(self, request, model_admin):
        return (
            ('recente', 'Últimos 30 dias'),
            ('mes_passado', 'Mês passado'),
            ('ano_atual', 'Este ano'),
            ('ano_passado', 'Ano passado'),
            ('antigo', 'Mais antigo que 1 ano'),
        )

    def queryset(self, request, queryset):
        hoje = timezone.now().date()
        if self.value() == 'recente':
            return queryset.filter(data_lancamento__gte=hoje - timedelta(days=30))
        elif self.value() == 'mes_passado':
            return queryset.filter(
                data_lancamento__gte=hoje - timedelta(days=60),
                data_lancamento__lt=hoje - timedelta(days=30)
            )
        elif self.value() == 'ano_atual':
            return queryset.filter(data_lancamento__year=hoje.year)
        elif self.value() == 'ano_passado':
            return queryset.filter(data_lancamento__year=hoje.year - 1)
        elif self.value() == 'antigo':
            return queryset.filter(data_lancamento__lt=hoje - timedelta(days=365))

class ClassificacaoFilter(SimpleListFilter):
    title = 'Classificação'
    parameter_name = 'classificacao'

    def lookups(self, request, model_admin):
        return (
            ('excelente', 'Excelente (9.0+)'),
            ('muito_bom', 'Muito Bom (8.0-8.9)'),
            ('bom', 'Bom (7.0-7.9)'),
            ('regular', 'Regular (6.0-6.9)'),
            ('ruim', 'Ruim (< 6.0)'),
            ('sem_classificacao', 'Sem Classificação'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'excelente':
            return queryset.filter(classificacao__gte=9.0)
        elif self.value() == 'muito_bom':
            return queryset.filter(classificacao__gte=8.0, classificacao__lt=9.0)
        elif self.value() == 'bom':
            return queryset.filter(classificacao__gte=7.0, classificacao__lt=8.0)
        elif self.value() == 'regular':
            return queryset.filter(classificacao__gte=6.0, classificacao__lt=7.0)
        elif self.value() == 'ruim':
            return queryset.filter(classificacao__lt=6.0)
        elif self.value() == 'sem_classificacao':
            return queryset.filter(classificacao__isnull=True)

class DuracaoFilter(SimpleListFilter):
    title = 'Duração'
    parameter_name = 'duracao'

    def lookups(self, request, model_admin):
        return (
            ('curto', 'Curto (< 90 min)'),
            ('medio', 'Médio (90-120 min)'),
            ('longo', 'Longo (120-150 min)'),
            ('muito_longo', 'Muito Longo (> 150 min)'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'curto':
            return queryset.filter(duracao__lt=90)
        elif self.value() == 'medio':
            return queryset.filter(duracao__gte=90, duracao__lte=120)
        elif self.value() == 'longo':
            return queryset.filter(duracao__gt=120, duracao__lte=150)
        elif self.value() == 'muito_longo':
            return queryset.filter(duracao__gt=150)

# ==================== ADMIN PERSONALIZADO ====================

class LoginUsersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'usuario', 
        'email', 
        'total_usuarios_criados',
        'data_criacao',
        'ultimo_acesso'
    )
    list_display_links = ('id', 'usuario')
    list_filter = ('data_criacao',)
    search_fields = ('usuario', 'email')
    readonly_fields = ('id', 'data_criacao', 'ultimo_acesso')
    ordering = ('-data_criacao',)
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('usuario', 'email', 'senha')
        }),
        ('Informações do Sistema', {
            'fields': ('id', 'data_criacao', 'ultimo_acesso'),
            'classes': ('collapse',)
        }),
    )
    
    def total_usuarios_criados(self, obj):
        count = obj.LoginUsers.count()
        return format_html('<span style="color: green; font-weight: bold;">{}</span>', count)
    total_usuarios_criados.short_description = 'Usuários Criados'

class GenerosAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'genero', 
        'total_filmes',
        'total_series'
    )
    list_display_links = ('id', 'genero')
    search_fields = ('genero',)
    ordering = ('genero',)
    
    def total_filmes(self, obj):
        count = obj.filmes_set.count()
        return format_html('<span style="color: blue;">{}</span>', count)
    total_filmes.short_description = 'Total de Filmes'
    
    def total_series(self, obj):
        count = obj.series_set.count()
        return format_html('<span style="color: purple;">{}</span>', count)
    total_series.short_description = 'Total de Séries'

class UsersAccountAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'usuario', 
        'imagem_preview',
        'login_user',
        'data_criacao'
    )
    list_display_links = ('id', 'usuario')
    list_filter = ('login_user',)
    search_fields = ('usuario', 'login_user__usuario')
    readonly_fields = ('id', 'imagem_preview')
    ordering = ('-id',)
    
    fieldsets = (
        ('Informações do Usuário', {
            'fields': ('usuario', 'login_user')
        }),
        ('Imagem', {
            'fields': ('image', 'imagem_preview')
        }),
    )
    
    def imagem_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px; border-radius: 5px;" />',
                obj.image.url
            )
        return "Sem imagem"
    imagem_preview.short_description = 'Imagem'
    


class FilmesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo', 
        'imagem_preview',
        'data_lancamento', 
        'duracao_formatada', 
        'lista_generos', 
        'diretor', 
        'classificacao_formatada',
        'pais_de_origem',
        'linguagem'
    )
    list_display_links = ('id', 'titulo')
    list_filter = (
        DataLancamentoFilter,
        ClassificacaoFilter,
        DuracaoFilter,
        'genero',
        'pais_de_origem',
        'linguagem',
        'data_lancamento'
    )
    search_fields = (
        'titulo', 
        'diretor',
        'elenco',
        'descricao',
        'genero__genero'
    )
    readonly_fields = ('id', 'imagem_preview')
    filter_horizontal = ('genero',)
    ordering = ('-data_lancamento', 'titulo')
    list_per_page = 25
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'imagem', 'imagem_preview')
        }),
        ('Detalhes Técnicos', {
            'fields': ('data_lancamento', 'duracao', 'classificacao')
        }),
        ('Classificação e Gêneros', {
            'fields': ('genero', 'pais_de_origem', 'linguagem')
        }),
        ('Equipe', {
            'fields': ('diretor', 'elenco')
        }),
    )
    
    actions = ['marcar_como_recente', 'atualizar_classificacao', 'exportar_para_csv', 'duplicar_registro', 'limpar_dados_antigos']
    
    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html(
                '<img src="{}" style="max-height: 60px; max-width: 40px; border-radius: 3px;" />',
                obj.imagem.url
            )
        return "Sem imagem"
    imagem_preview.short_description = 'Poster'
    
    def duracao_formatada(self, obj):
        horas = obj.duracao // 60
        minutos = obj.duracao % 60
        if horas > 0:
            return f"{horas}h {minutos}min"
        return f"{minutos}min"
    duracao_formatada.short_description = 'Duração'
    
    def classificacao_formatada(self, obj):
        if obj.classificacao:
            color = 'green' if obj.classificacao >= 8.0 else 'orange' if obj.classificacao >= 6.0 else 'red'
            return format_html(
                '<span style="color: {}; font-weight: bold;">★ {}</span>',
                color, obj.classificacao
            )
        return "Sem classificação"
    classificacao_formatada.short_description = 'Classificação'
    
    def marcar_como_recente(self, request, queryset):
        queryset.update(data_lancamento=timezone.now().date())
        self.message_user(request, f"{queryset.count()} filmes marcados como recentes.")
    marcar_como_recente.short_description = "Marcar como recente"
    
    def atualizar_classificacao(self, request, queryset):
        # Simular atualização de classificação
        for filme in queryset:
            if not filme.classificacao:
                filme.classificacao = 7.5
                filme.save()
        self.message_user(request, f"Classificação atualizada para {queryset.count()} filmes.")
    atualizar_classificacao.short_description = "Atualizar classificação"

    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }

class SeriesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo', 
        'imagem_preview',
        'data_lancamento', 
        'temporadas_episodios', 
        'lista_generos',  
        'diretor', 
        'classificacao_formatada',
        'pais_de_origem',
        'linguagem'
    )
    list_display_links = ('id', 'titulo')
    list_filter = (
        DataLancamentoFilter,
        ClassificacaoFilter,
        'n_temporadas',
        'genero',
        'pais_de_origem',
        'linguagem',
        'data_lancamento'
    )
    search_fields = (
        'titulo', 
        'diretor',
        'elenco',
        'descricao',
        'genero__genero'
    )
    readonly_fields = ('id', 'imagem_preview')
    filter_horizontal = ('genero',)
    ordering = ('-data_lancamento', 'titulo')
    list_per_page = 25
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'imagem', 'imagem_preview')
        }),
        ('Detalhes Técnicos', {
            'fields': ('data_lancamento', 'n_temporadas', 'n_episodios', 'classificacao')
        }),
        ('Classificação e Gêneros', {
            'fields': ('genero', 'pais_de_origem', 'linguagem')
        }),
        ('Equipe', {
            'fields': ('diretor', 'elenco')
        }),
    )
    
    actions = ['marcar_como_recente', 'atualizar_classificacao', 'exportar_para_csv', 'duplicar_registro', 'limpar_dados_antigos']
    
    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html(
                '<img src="{}" style="max-height: 60px; max-width: 40px; border-radius: 3px;" />',
                obj.imagem.url
            )
        return "Sem imagem"
    imagem_preview.short_description = 'Poster'
    
    def temporadas_episodios(self, obj):
        return f"{obj.n_temporadas} temp. • {obj.n_episodios} ep."
    temporadas_episodios.short_description = 'Temporadas/Episódios'
    
    def classificacao_formatada(self, obj):
        if obj.classificacao:
            color = 'green' if obj.classificacao >= 8.0 else 'orange' if obj.classificacao >= 6.0 else 'red'
            return format_html(
                '<span style="color: {}; font-weight: bold;">★ {}</span>',
                color, obj.classificacao
            )
        return "Sem classificação"
    classificacao_formatada.short_description = 'Classificação'
    
    def marcar_como_recente(self, request, queryset):
        queryset.update(data_lancamento=timezone.now().date())
        self.message_user(request, f"{queryset.count()} séries marcadas como recentes.")
    marcar_como_recente.short_description = "Marcar como recente"
    
    def atualizar_classificacao(self, request, queryset):
        # Simular atualização de classificação
        for serie in queryset:
            if not serie.classificacao:
                serie.classificacao = 7.5
                serie.save()
        self.message_user(request, f"Classificação atualizada para {queryset.count()} séries.")
    atualizar_classificacao.short_description = "Atualizar classificação"

    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }

# ==================== PERSONALIZAÇÃO DO SITE ADMIN ====================

admin.site.site_header = "🎬 MovieFlix - Administração"
admin.site.site_title = "MovieFlix Admin"
admin.site.index_title = "Bem-vindo ao Painel de Administração do MovieFlix"



# ==================== ESTATÍSTICAS PERSONALIZADAS ====================

class MovieFlixAdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        
        # Estatísticas gerais
        total_filmes = Filmes.objects.count()
        total_series = Series.objects.count()
        total_usuarios = LoginUsers.objects.count()
        total_generos = Generos.objects.count()
        
        # Média de classificação
        media_filmes = Filmes.objects.aggregate(media=Avg('classificacao'))['media'] or 0
        media_series = Series.objects.aggregate(media=Avg('classificacao'))['media'] or 0
        
        # Conteúdo recente (últimos 30 dias)
        hoje = timezone.now().date()
        filmes_recentes = Filmes.objects.filter(data_lancamento__gte=hoje - timedelta(days=30)).count()
        series_recentes = Series.objects.filter(data_lancamento__gte=hoje - timedelta(days=30)).count()
        
        extra_context.update({
            'total_filmes': total_filmes,
            'total_series': total_series,
            'total_usuarios': total_usuarios,
            'total_generos': total_generos,
            'media_filmes': round(media_filmes, 1),
            'media_series': round(media_series, 1),
            'filmes_recentes': filmes_recentes,
            'series_recentes': series_recentes,
        })
        
        return super().index(request, extra_context)

# Substituir o site admin padrão
admin_site = MovieFlixAdminSite()

# Registrar os modelos no site admin personalizado
admin_site.register(LoginUsers, LoginUsersAdmin)
admin_site.register(Generos, GenerosAdmin)
admin_site.register(UsersAccount, UsersAccountAdmin)
admin_site.register(Filmes, FilmesAdmin)
admin_site.register(Series, SeriesAdmin)

# Substituir o site admin padrão
admin.site = admin_site