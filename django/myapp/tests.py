from django.test import TestCase
from rest_framework.test import APITestCase
from myapp.models import InformacaoMorador

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
