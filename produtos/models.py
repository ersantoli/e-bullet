from django.db import models

class Gravar(models.Model):
    criado_em= models.DateTimeField(auto_now_add=True)
    matricula = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    endereco = models.CharField(max_length=150)
    nascido = models.CharField(max_length=30)
    contato = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
 
    def __str__(self):
        return(f"{self.nome} {self.matricula}")
    
class boletim(models.Model):
    matricula = models.CharField(max_length=10)
    nome  = models.CharField(max_length=100)
    matematica = models.CharField(max_length=2)
    portugues = models.CharField(max_length=2)
    fisica = models.CharField(max_length=2)
    quimica = models.CharField(max_length=2)
    ingles = models.CharField(max_length=2)
    geografia = models.CharField(max_length=2)
    historia= models.CharField(max_length=2)
    ciencias = models.CharField(max_length=2)
 
    def __str__(self):
        return(f"{self.nome}  {self.matricula} {self.matematica}")    