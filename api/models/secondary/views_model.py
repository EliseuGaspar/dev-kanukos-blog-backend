from django.db import models



class Views(models.Model):

    class Meta:
        verbose_name = 'Visualização'
        verbose_name_plural = 'Visualizações'

    id = models.AutoField(verbose_name = 'ID', primary_key = True, unique = True)
    post = models.ForeignKey('Posts', verbose_name = 'Postagem', on_delete = models.CASCADE, blank = False)
    user = models.ForeignKey('User', on_delete = models.CASCADE, verbose_name = 'Usuário', blank = False)

    def __str__(self) -> str:
        return f'visualizações: {self.id}'