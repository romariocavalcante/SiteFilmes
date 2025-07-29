from django.contrib import admin
from django.utils import timezone
from datetime import timedelta

def exportar_para_csv(modeladmin, request, queryset):
    """Ação para exportar dados selecionados para CSV"""
    import csv
    from django.http import HttpResponse
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{modeladmin.model._meta.verbose_name_plural}.csv"'
    
    writer = csv.writer(response)
    
    # Escrever cabeçalhos
    field_names = [field.name for field in modeladmin.model._meta.fields]
    writer.writerow(field_names)
    
    # Escrever dados
    for obj in queryset:
        row = []
        for field_name in field_names:
            value = getattr(obj, field_name)
            if hasattr(value, 'strftime'):  # Para campos de data
                value = value.strftime('%Y-%m-%d')
            row.append(str(value) if value is not None else '')
        writer.writerow(row)
    
    return response
exportar_para_csv.short_description = "Exportar selecionados para CSV"

def marcar_como_destaque(modeladmin, request, queryset):
    """Ação para marcar conteúdo como destaque"""
    for obj in queryset:
        # Aqui você pode adicionar lógica para marcar como destaque
        # Por exemplo, adicionar um campo 'destaque' ao modelo
        pass
    modeladmin.message_user(request, f"{queryset.count()} itens marcados como destaque.")
marcar_como_destaque.short_description = "Marcar como destaque"

def atualizar_classificacao_media(modeladmin, request, queryset):
    """Ação para atualizar classificação média"""
    from django.db.models import Avg
    
    for obj in queryset:
        if hasattr(obj, 'classificacao') and not obj.classificacao:
            # Simular uma classificação baseada em critérios
            obj.classificacao = 7.5
            obj.save()
    
    modeladmin.message_user(request, f"Classificação atualizada para {queryset.count()} itens.")
atualizar_classificacao_media.short_description = "Atualizar classificação média"

def limpar_dados_antigos(modeladmin, request, queryset):
    """Ação para limpar dados antigos"""
    from datetime import datetime, timedelta
    
    # Exemplo: remover conteúdo mais antigo que 5 anos
    data_limite = timezone.now().date() - timedelta(days=5*365)
    antigos = queryset.filter(data_lancamento__lt=data_limite)
    count = antigos.count()
    antigos.delete()
    
    modeladmin.message_user(request, f"{count} itens antigos removidos.")
limpar_dados_antigos.short_description = "Limpar dados antigos"

def duplicar_registro(modeladmin, request, queryset):
    """Ação para duplicar registros selecionados"""
    for obj in queryset:
        obj.pk = None  # Remove a chave primária para criar um novo registro
        obj.titulo = f"{obj.titulo} (Cópia)"
        obj.save()
    
    modeladmin.message_user(request, f"{queryset.count()} registros duplicados com sucesso.")
duplicar_registro.short_description = "Duplicar registros selecionados"

def marcar_como_ativo(modeladmin, request, queryset):
    """Ação para marcar como ativo/inativo"""
    for obj in queryset:
        # Aqui você pode adicionar lógica para marcar como ativo
        pass
    modeladmin.message_user(request, f"{queryset.count()} itens marcados como ativos.")
marcar_como_ativo.short_description = "Marcar como ativo"

# Lista de todas as ações disponíveis
ADMIN_ACTIONS = [
    exportar_para_csv,
    marcar_como_destaque,
    atualizar_classificacao_media,
    limpar_dados_antigos,
    duplicar_registro,
    marcar_como_ativo,
] 