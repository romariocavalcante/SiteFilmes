from django.db import models

class Diretor(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Diretor"
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
class Ator(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Ator"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Gênero"
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
class Classificacao(models.Model):
    classificacao = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Classificação"
        ordering = ['classificacao']

    def __str__(self):
        return self.classificacao

class Filme(models.Model):

    PAIS_CHOICES = [
        ('US', 'Estados Unidos'),
        ('CA', 'Canadá'),
        ('CN', 'China'),
        ('GB', 'Reino Unido'),
        ('JP', 'Japão'),
        ('IN', 'Índia'),
        ('KR', 'Coréia do Sul'),
        ('FR', 'França'),
        ('NG', 'Nigéria'),
        ('BR', 'Brasil'),
        ('IT', 'Itália'),
        ('AU', 'Austrália'),
        ('DE', 'Alemanha'),
        ('RU', 'Rússia'),
        ('ES', 'Espanha'),
    ]

    IDIOMA_CHOICES = [
        ('EN', 'Inglês'),  # Estados Unidos, Canadá, Reino Unido, Austrália
        ('FR', 'Francês'),  # França, Canadá
        ('ZH', 'Chinês'),  # China
        ('HI', 'Hindi'),  # Índia
        ('JA', 'Japonês'),  # Japão
        ('KO', 'Coreano'),  # Coréia do Sul
        ('ES', 'Espanhol'),  # Espanha
        ('PT', 'Português'),  # Brasil
        ('IT', 'Italiano'),  # Itália
        ('DE', 'Alemão'),  # Alemanha
        ('RU', 'Russo'),  # Rússia
        ('AR', 'Árabe'),  # Nigéria
    ]

    ANO_LANCAMENTO_CHOICES = [(r, r) for r in range(1990, 2024)]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    duracao = models.TimeField()
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    elenco = models.ManyToManyField(Ator, related_name='filmes')
    ano_de_lancamento = models.IntegerField(choices=ANO_LANCAMENTO_CHOICES)
    genero = models.ManyToManyField(Genero)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)
    pais_de_origem = models.CharField(max_length=2, choices=PAIS_CHOICES, default='BR')
    idioma = models.CharField(max_length=2, choices=IDIOMA_CHOICES, default='PT')
    orcamento = models.DecimalField(max_digits=15, decimal_places=2)
    bilheteria = models.DecimalField(max_digits=15, decimal_places=2)
    poster = models.ImageField(upload_to='posters/')
    trailer = models.URLField(max_length=200)
    video = models.FileField(upload_to='videos/')

    class Meta:
        verbose_name_plural = "Filmes"
        ordering = ['titulo']
        
    
    def __str__(self):
        return self.titulo