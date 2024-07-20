from django.db import models



class Admin(models.Model):

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    id = models.AutoField(verbose_name = 'ID', primary_key = True, unique = True)
    name = models.CharField(verbose_name = 'Nome', max_length = 255, blank = False)
    email = models.EmailField(verbose_name = 'E-mail', unique = True, blank = False)
    password = models.CharField(verbose_name = 'Senha', max_length = 255, blank = False)
    is_super = models.BooleanField(verbose_name = 'Admin Superior?', default = False)
    is_content = models.BooleanField(verbose_name = 'Admin d\'Conteúdo?', default = False)
    is_pub = models.BooleanField(verbose_name = 'Admin Publicador?', default = False)
    is_active = models.BooleanField(verbose_name = 'Activo?', default = True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Registrado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Atualizado em')

    def __str__(self) -> str:
        return f'administrador: {self.name}'