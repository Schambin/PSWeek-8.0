from django.db import models

class Curso(models.Model):
    # nome da classe = models.tipo do campo(parametro) 
    nome = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()
    data_criacao = models.DateTimeField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome    