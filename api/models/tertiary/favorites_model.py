from django.db import models
from utils.choices import REACTIONS



class Favorite(models.Model):

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'

    id = models.AutoField(verbose_name = 'ID', primary_key = True, unique = True)

    post = models.ForeignKey('Posts', on_delete = models.CASCADE,
    verbose_name = 'Postagem', blank = False, related_name = 'favorite')

    user = models.ForeignKey('User', on_delete = models.CASCADE,
    verbose_name = 'Usuário', blank = False, related_name = 'favorite')

    def __str__(self) -> str:
        return f'post_favorito: {self.post}'