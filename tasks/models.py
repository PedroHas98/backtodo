from django.db import models
class Tasks(models.Model):
  tarefa = models.CharField(max_length=50)
  descricao = models.CharField(max_length=50)
  prioridade = models.CharField(max_length=20)
  data = models.CharField(max_length=8)
  status = models.CharField(max_length=20)

# Create your models here.
