from django.db import models
from utils.choices import REACTIONS



class Saved(models.Model):

    class Meta:
        verbose_name = 'Salvo'
        verbose_name_plural = 'Salvos'

    id = models.AutoField(verbose_name = 'ID', primary_key = True, unique = True)

    post = models.ForeignKey('Posts', on_delete = models.CASCADE,
    verbose_name = 'Postagem', blank = False, related_name = 'saveds')

    user = models.ForeignKey('User', on_delete = models.CASCADE,
    verbose_name = 'Usuário', blank = False, related_name = 'saveds')

    def __str__(self) -> str:
        return f'post_salvo: {self.post}'