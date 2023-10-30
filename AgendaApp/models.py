from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField(verbose_name='Data Nascimento')
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
 
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoa'