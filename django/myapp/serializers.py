from rest_framework import serializers
from myapp.models import Domicilio, Morador

class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields = '__all__'
        read_only_fields = ['id']

class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = [
            'id',
            'username',
            'nome',
            'sobrenome',
            'sexo',
            'data_nascimento',
            'idade',
            'relacao_com_responsavel',
            'registro_nascimento',
            'possui_conjuge',
            'vive_com_conjuge',
            'nome_conjuge',
            'tipo_uniao',
            'trabalhou_remunerado',
            'qtd_trabalhos',
            'ocupacao',
            'atividade_empresa',
            'carteira_assinada',
            'empresa_cnpj',
            'faixa_rendimento',
            'dificuldade_enxergar',
            'dificuldade_andar',
            'sabe_ler_escrever',
            'frequenta_escola',
            'curso_frequentado',
            'concluiu_superior',
            'local_trabalho',
            'retorna_casa',
            'tempo_casa_trabalho_horas',
            'tempo_casa_trabalho_minutos',
            'principal_transporte',
            'autismo_diagnostico',
            'contato_nome',
            'contato_email',
            'contato_telefone',
            'religiao_culto',
        ]
        read_only_fields = ['id']