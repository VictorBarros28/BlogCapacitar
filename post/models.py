from django.db import models
from user.models import User

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default="")
    autor = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='autor')
    titulo = models.CharField(max_length=180)
    img = models.ImageField(upload_to='post/')

    def __str__(self):
        return f' Titulo : {self.titulo} | ID = {self.id} |Outros campos '

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural =  'Postagens'