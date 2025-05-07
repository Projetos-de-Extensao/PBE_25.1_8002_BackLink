
from rest_framework import serializers
from myapp.models import InformacaoDomicilio
from myapp.models import InformacaoMorador

class InformacaoDomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacaoDomicilio
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
        

class InformacaoMoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacaoMorador
        fields = [
            'id',
            'nome',
            'sobrenome',
            'sexo',
            'data_nascimento',
            'idade',
        ]
        read_only_fields = ['id']