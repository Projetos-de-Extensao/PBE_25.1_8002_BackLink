from django.test import TestCase
from rest_framework.test import APITestCase
from myapp.models import Morador, Domicilio

# botem os  testes ai de cada formulario 

class InformacaoMoradorTests(APITestCase):
    def test_create_informacao_morador(self):
        data = {
            "nome": "João",
            "sobrenome": "Silva",
            "sexo": "M",
            "data_nascimento": "1990-01-01",
            "idade": 35
        }
        response = self.client.post('/informacao-morador/', data)
        self.assertEqual(response.status_code, 201)

class MoradorTests(APITestCase):
    def setUp(self):
        # Cria um Domicilio para associar ao Morador
        self.domicilio = Domicilio.objects.create(
            uf="SP",
            municipio="São Paulo",
            distrito="Centro",
            subdistrito="Centro",
            setor="01",
            numero_quadra="10",
            numero_face="A",
            seq_endereco="001",
            seq_coletivo="",
            seq_especie="",
            especie_domicilio="1",
            tipo="011"
        )

    def test_create_morador(self):
        data = {
            "nome": "João",
            "sobrenome": "Silva",
            "domicilio": self.domicilio.id,
            "sexo": "M",
            "data_nascimento": "1990-01-01",
            "idade": 35
        }
        response = self.client.post('/informacao-morador/', data)
        self.assertEqual(response.status_code, 201)
