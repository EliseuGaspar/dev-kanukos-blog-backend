# Generated by Django 5.0.7 on 2024-07-17 18:14

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('password', models.CharField(max_length=255, verbose_name='Senha')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('password', models.CharField(max_length=255, verbose_name='Senha')),
                ('is_super', models.BooleanField(default=False, verbose_name='Admin Superior?')),
                ('is_content', models.BooleanField(default=False, verbose_name="Admin d'Conteúdo?")),
                ('is_pub', models.BooleanField(default=False, verbose_name='Admin Publicador?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Conteúdo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Comentário',
                'verbose_name_plural': 'Comentários',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Título')),
                ('header', models.CharField(max_length=255, verbose_name='Cabeçalho')),
                ('body', models.TextField(verbose_name='Corpo')),
                ('published', models.BooleanField(db_index=True, default=False, verbose_name='Publicado')),
                ('cover', models.FileField(upload_to='storage/images/', verbose_name='Imagem de capa')),
                ('midia', models.FileField(blank=True, upload_to='storage/images/', verbose_name='Midia do Post')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')], default='draft', max_length=10, verbose_name='Estado')),
                ('category', models.CharField(choices=[('development', 'development'), ('networks', 'networks'), ('hardware', 'hardware'), ('database', 'database'), ('stream', 'stream'), ('discussions', 'discussions'), ('machine-learning', 'machine-learning')], max_length=120, verbose_name='Categoria')),
                ('comments_enabled', models.BooleanField(default=True, verbose_name='Comentários?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Postagem',
                'verbose_name_plural': 'Postagens',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.posts', verbose_name='Postagem')),
            ],
            options={
                'verbose_name': 'Favorito',
                'verbose_name_plural': 'Favoritos',
            },
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('reaction', models.CharField(blank=True, choices=[('😆', 'laughter'), ('👏', 'congratulations'), ('😮', 'admiration'), ('😢', 'sadness'), ('😡', 'anger')], default=None, max_length=10, verbose_name='Reação')),
                ('comments', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.comments', verbose_name='Comentário')),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.posts', verbose_name='Postagem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Reação',
                'verbose_name_plural': 'Reações',
            },
        ),
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.posts', verbose_name='Postagem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Salvo',
                'verbose_name_plural': 'Salvos',
            },
        ),
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.posts', verbose_name='Postagem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Visualização',
                'verbose_name_plural': 'Visualizações',
            },
        ),
    ]
