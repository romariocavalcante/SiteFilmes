from django.db import models


# Login de Usuário
class LoginUsers(models.Model):
    usuario = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)

    def __str__(self):
        return self.usuario
    
    class Meta:
        verbose_name = 'Login'
        verbose_name_plural = 'Login'

class Generos(models.Model):
    genero = models.CharField(max_length=200)

    def __str__(self):
        return self.genero
    
    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'


# Lista de usuarios dentro da conta de um usuário
class UsersAccount(models.Model):
    usuario = models.CharField(max_length=200)
    image = models.ImageField(upload_to="static/imgUser")

    def __str__(self):
        return self.usuario
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Filmes(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    data_lancamento = models.DateField(verbose_name="Data de Lançamento")
    duracao = models.PositiveIntegerField(verbose_name="Duração")
    genero = models.ManyToManyField(Generos, verbose_name="Gêneros")
    diretor = models.CharField(max_length=255, verbose_name="Diretor")
    elenco = models.TextField(verbose_name="Elenco")
    classificacao = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name="Classificação")
    imagem = models.ImageField(upload_to='movie_posters/', null=True, blank=True, verbose_name="Imagem")
    linguagem = models.CharField(max_length=100, verbose_name="Idioma Principal")
    pais_de_origem = models.CharField(max_length=100, verbose_name="País de Origem")


    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    def lista_generos(self):
        return ", ".join(genero.genero for genero in self.genero.all())
    lista_generos.short_description = 'Gêneros'

class Series(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    data_lancamento = models.DateField(verbose_name="Data de Lançamento")
    n_temporadas = models.PositiveIntegerField(verbose_name="Temporadas")
    n_episodios = models.PositiveIntegerField(verbose_name="Episódios")
    genero = models.ManyToManyField(Generos, verbose_name="Gêneros")
    diretor = models.CharField(max_length=255, verbose_name="Diretor")
    elenco = models.TextField(verbose_name="Elenco")
    classificacao = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name="Classificação")
    imagem = models.ImageField(upload_to='series_posters/', null=True, blank=True, verbose_name="Imagem")
    linguagem = models.CharField(max_length=100, verbose_name="Idioma Principal")
    pais_de_origem = models.CharField(max_length=100, verbose_name="País de Origem")

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'

    def lista_generos(self):
        return ", ".join(genero.genero for genero in self.genero.all())
    lista_generos.short_description = 'Gêneros'
