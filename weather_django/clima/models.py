from django.db import models

# Create your models here.
class PrevisaoClimatica(models.Model):
    localidade = models.CharField(max_length=100)
    data_hora = models.DateTimeField()
    temperatura = models.FloatField()
    sensacao_termica = models.FloatField()
    umidade = models.FloatField()
    condicao_climatica = models.CharField(max_length=50)
    descricao = models.TextField()
    endereco_resolvido = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.localidade} - {self.data_hora} - {self.temperatura}°C"