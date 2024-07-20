from django.db import models
from utils.choices import REACTIONS



class Reaction(models.Model):

    class Meta:
        verbose_name = 'Reação'
        verbose_name_plural = 'Reações'

    id = models.AutoField(verbose_name = 'ID', primary_key = True, unique = True)

    post = models.ForeignKey('Posts', on_delete = models.CASCADE,
    verbose_name = 'Postagem', blank = True, related_name='reactions')

    user = models.ForeignKey('User', on_delete = models.CASCADE,
    verbose_name = 'Usuário', blank = False, related_name='reactions')

    reaction = models.CharField(verbose_name = 'Reação', max_length = 10,
    blank = True, default = None, choices = REACTIONS)

    def __str__(self) -> str:
        return f'reação: {self.reaction}'