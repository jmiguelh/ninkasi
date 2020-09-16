from django.db import models

# Create your models here.


class Empresa(models.Model):
    SEGMENTO = (
        (1, 'SOMA'),
        (2, 'BOVESPA NIVEL 2'),
        (3, 'BOLSA'),
        (4, 'NOVO MERCADO'),
        (5, 'BOVESPA NIVEL 1'),
        (6, 'MAIS'),
        (7, 'FIP MT'),
        (8, 'FIP IE'),
        (9, 'FIP EE'),
        (10, 'MAIS NIVEL 2'),
    )
    cod_empresa = models.CharField(
        max_length=4, primary_key=True, verbose_name="Código")
    nome = models.CharField(
        max_length=100, null=False, verbose_name="Nome")
    razao_social = models.CharField(
        max_length=100, null=False, verbose_name="Razão Social")
    segmento = models.PositiveSmallIntegerField(
        choices=SEGMENTO, verbose_name="Segmento")
    capital = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Capital",)
    qtd_ordinarias = models.PositiveBigIntegerField(
        verbose_name="Quant. Ações Ordinárias")
    qtd_preferenciais = models.PositiveBigIntegerField(
        verbose_name="Quant. Ações Preferenciais")

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nome
