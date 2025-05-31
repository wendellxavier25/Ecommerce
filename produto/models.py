from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao_curta = models.TextField(max_length=200)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produtos_imagens/%Y/%m/', blank=True, null=True)
    sulg = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.Choices(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples')
        )
    )
