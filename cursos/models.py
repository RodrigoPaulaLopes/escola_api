from django.db import models

# Create your models here.


class Base(models.Model):
    publicacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    
    
    class Meta:
        abstract = True
        
        
class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        
    def __str__(self):
        return self.titulo
    
class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    
    nota = models.DecimalField(max_digits=2, decimal_places=1)
    
    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'
        unique_together = ['email', 'curso']
        
    def __str__(self) -> str:
        return f'{self.nome} avaliou o {self.curso} com a nota {self.nota}'