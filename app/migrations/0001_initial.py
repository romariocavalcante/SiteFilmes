# Generated by Django 5.1.1 on 2024-09-25 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='LoginUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Usuário de Login',
                'verbose_name_plural': 'Usuários de Login',
            },
        ),
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('data_lancamento', models.DateField(verbose_name='Data de Lançamento')),
                ('duracao', models.PositiveIntegerField(verbose_name='Duração')),
                ('diretor', models.CharField(max_length=255, verbose_name='Diretor')),
                ('elenco', models.TextField(verbose_name='Elenco')),
                ('classificacao', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Classificação')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='movie_posters/', verbose_name='Imagem')),
                ('linguagem', models.CharField(max_length=100, verbose_name='Idioma Principal')),
                ('pais_de_origem', models.CharField(max_length=100, verbose_name='País de Origem')),
                ('genero', models.ManyToManyField(to='app.generos', verbose_name='Gêneros')),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('data_lancamento', models.DateField(verbose_name='Data de Lançamento')),
                ('n_temporadas', models.PositiveIntegerField(verbose_name='Temporadas')),
                ('n_episodios', models.PositiveIntegerField(verbose_name='Episódios')),
                ('diretor', models.CharField(max_length=255, verbose_name='Diretor')),
                ('elenco', models.TextField(verbose_name='Elenco')),
                ('classificacao', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Classificação')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='series_posters/', verbose_name='Imagem')),
                ('linguagem', models.CharField(max_length=100, verbose_name='Idioma Principal')),
                ('pais_de_origem', models.CharField(max_length=100, verbose_name='País de Origem')),
                ('genero', models.ManyToManyField(to='app.generos', verbose_name='Gêneros')),
            ],
            options={
                'verbose_name': 'Serie',
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='UsersAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='static/imgUser')),
                ('login_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='app.loginusers')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
    ]
