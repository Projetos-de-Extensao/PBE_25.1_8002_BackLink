from rest_framework import serializers
from myapp.models import Domicilio, Morador

class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields = [
            'id',
            'uf',
            'municipio',
            'distrito',
            'subdistrito',
            'setor',
            'numero_quadra',
            'numero_face',
            'seq_endereco',
            'seq_coletivo',
            'seq_especie',
            'especie_domicilio',
            'tipo',
        ]
        read_only_fields = ['id']

class MoradorSerializer(serializers.ModelSerializer):
    domicilio = DomicilioSerializer()
    class Meta:
        model = Morador
        fields = [
            'id',
            'nome',
            'sobrenome',
            'domicilio',
            'sexo',
            'data_nascimento',
            'idade',
          
        ]
        read_only_fields = ['id']