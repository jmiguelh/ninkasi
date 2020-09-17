from rest_framework import serializers
from .models import Empresa


class EmpresaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('cod_empresa', 'nome', 'razao_social', 'segmento',
                  'capital', 'qtd_ordinarias', 'qtd_preferenciais')
