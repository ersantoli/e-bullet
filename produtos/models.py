from django.db import models
#python manage.py makemigrations
# python manage.py migrate

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
    
class boletim2b(models.Model):
    
    matematica1b = models.CharField(max_length=2)
    portugues1b = models.CharField(max_length=2)
    
 
  #  def __str__(self):
   #     return(f"{self.matematica2b}  {self.portugues2b}")    
   
#teste boletim bimestre
from django.db import models

class Boletimb(models.Model):
    aluno = models.CharField(max_length=200)
    matricula = models.CharField(max_length=10)
    
    # Ciências
    ciencias_bim1 = models.FloatField(max_length=2)
    ciencias_bim2 = models.FloatField(max_length=2,blank=True, null=True)
    ciencias_bim3 = models.FloatField(max_length=2,blank=True, null=True)
    ciencias_bim4 = models.FloatField(max_length=2,blank=True, null=True)
    
    # Matemática
    matematica_bim1 = models.FloatField(max_length=2)
    matematica_bim2 = models.FloatField(max_length=2,blank=True, null=True)
    matematica_bim3 = models.FloatField(max_length=2,blank=True, null=True)
    matematica_bim4 = models.FloatField(max_length=2,blank=True, null=True)
    
    # Geografia
    geografia_bim1 = models.FloatField()
    geografia_bim2 = models.FloatField(max_length=2,blank=True, null=True)
    geografia_bim3 = models.FloatField(max_length=2,blank=True, null=True)
    geografia_bim4 = models.FloatField(max_length=2,blank=True, null=True)
    
    # História
    historia_bim1 = models.FloatField()
    historia_bim2 = models.FloatField(max_length=2,blank=True, null=True)
    historia_bim3 = models.FloatField(max_length=2,blank=True, null=True)
    historia_bim4 = models.FloatField(max_length=2,blank=True, null=True)
    
    # Português
    portugues_bim1 = models.FloatField()
    portugues_bim2 = models.FloatField(max_length=2,blank=True, null=True)
    portugues_bim3 = models.FloatField(max_length=2,blank=True, null=True)
    portugues_bim4 = models.FloatField(max_length=2,blank=True, null=True)
    
    # Inglês
    ingles_bim1 = models.FloatField()
    ingles_bim2 = models.FloatField(max_length=2,blank=True, null=True)
    ingles_bim3 = models.FloatField(max_length=2,blank=True, null=True)
    ingles_bim4 = models.FloatField(max_length=2,blank=True, null=True)
    
    # Física
    fisica_bim1 = models.FloatField()
    fisica_bim2 = models.FloatField(max_length=2,blank=True, null=True)
    fisica_bim3 = models.FloatField(max_length=2,blank=True, null=True)
    fisica_bim4 = models.FloatField(max_length=2,blank=True, null=True)
    
    # Química
    quimica_bim1 = models.FloatField()
    quimica_bim2 = models.FloatField(max_length=2,blank=True, null=True)
    quimica_bim3 = models.FloatField(max_length=2,blank=True, null=True)
    quimica_bim4 = models.FloatField(max_length=2,blank=True, null=True)

    def __str__(self):
        return self.aluno
   