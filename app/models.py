from django.db import models

class Ator(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
