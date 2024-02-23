from django.contrib import admin

# Register your models here.
from .models import Avaliacao, Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'url', 'atualizacao', 'ativo']
    
    
@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['curso', 'nome', 'email', 'nota', 'atualizacao', 'ativo']