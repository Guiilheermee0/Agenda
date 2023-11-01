from django.db import models

# Create your models here.
UFS = [
        ("SP", "São Paulo"),
        ("MG", "Minas Gerais"),
        ("RJ", "Rio de Janeiro"),
        ("ES", "Espirito Santo")
    ]

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    UF = models.CharField(max_length=2, choices=UFS)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    
    ESTADOS_CIVIS = [
        ('S', 'Solteiro'), 
        ('C', 'Casado'), 
        ('D', 'Divorciado'), 
        ('V', 'Viúvo')
        ]
    
   
   
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField(verbose_name='Data Nascimento')
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=30)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    estado = models.CharField(max_length=2, choices=UFS, null=True)
    estado_civil = models.CharField(max_length=1, choices=ESTADOS_CIVIS, null=True)


    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoa'


    