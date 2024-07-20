from django.db import models


class Comments(models.Model):

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    id = models.AutoField(verbose_name = 'ID', primary_key = True, unique = True)
    content = models.TextField(verbose_name = 'Conteúdo', blank = False)
    user = models.ForeignKey('User', on_delete = models.CASCADE,
    verbose_name = 'Usuário', blank = False, related_name='comments')
    posts = models.ForeignKey('Posts', on_delete = models.CASCADE,
    verbose_name = 'Postagem', blank = False, related_name='comments')

    def __str__(self) -> str:
        return f'comentário de: {self.user}'