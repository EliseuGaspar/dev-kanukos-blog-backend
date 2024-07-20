from django.db import models
from uuid import uuid4
from utils.choices import DRAFT, STATUS_CHOICES, CATEGORIES




class Posts(models.Model):

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

    id = models.UUIDField(verbose_name = 'ID', primary_key = True, unique = True,
    db_index = True, default = uuid4)

    title = models.CharField(verbose_name = 'Título', max_length = 255,
    blank = False, unique = True, db_index = True)

    header = models.CharField(verbose_name = 'Cabeçalho', max_length = 255, blank = False)
    body = models.TextField(verbose_name = 'Corpo', blank = False)

    author = models.ForeignKey('Admin', on_delete = models.CASCADE, verbose_name = 'Autor',
    blank = False, db_index = True, related_name='posts')

    published = models.BooleanField(verbose_name = 'Publicado', default = False,
    blank = False, db_index = True)

    cover = models.FileField(verbose_name = 'Imagem de capa', upload_to = 'storage/images/',
    blank = False)

    midia = models.FileField(verbose_name = 'Midia do Post', upload_to = 'storage/images/',
    blank = True)

    status = models.CharField(verbose_name = 'Estado', max_length = 10, choices = STATUS_CHOICES,
    default = DRAFT)

    category = models.CharField(verbose_name = 'Categoria', max_length = 120, choices = CATEGORIES)
    comments_enabled = models.BooleanField(verbose_name = 'Comentários?', default = True, blank = False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Atualizado em')


    def __str__(self) -> str:
        return f'postagem: {self.title}'