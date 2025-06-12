import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Domicilio, Morador

def run():
    # Limpa dados antigos
    Domicilio.objects.all().delete()
    Morador.objects.all().delete()

    # Cria moradores principais (um para cada domicílio)
    morador1 = Morador.objects.create(
        username="joao",
        nome="João",
        idade=34,
        sexo="M",
        data_nascimento="1990-01-01"
    )
    morador2 = Morador.objects.create(
        username="maria",
        nome="Maria",
        idade=32,
        sexo="F",
        data_nascimento="1992-05-10"
    )

    # Cria domicílios vinculados ao morador principal (responsável)
    dom1 = Domicilio.objects.create(
        uf="RJ",
        municipio="Angra dos Reis",
        distrito="01",
        subdistrito="01",
        setor="01",
        numero_quadra="01",
        numero_face="01",
        seq_endereco="001",
        especie_domicilio="1",
        tipo="011",
        abastecimento_agua="Poço",
        morador=morador1
    )
    dom2 = Domicilio.objects.create(
        uf="RJ",
        municipio="Angra dos Reis",
        distrito="01",
        subdistrito="01",
        setor="01",
        numero_quadra="02",
        numero_face="02",
        seq_endereco="002",
        especie_domicilio="1",
        tipo="011",
        abastecimento_agua="Encanada",
        morador=morador2
    )

    # Cria outros moradores e associa manualmente ao domicílio via related_name
    pedro = Morador.objects.create(
        username="pedro",
        nome="Pedro",
        idade=12,
        sexo="M",
        data_nascimento="2012-03-15"
    )
    ana = Morador.objects.create(
        username="ana",
        nome="Ana",
        idade=8,
        sexo="F",
        data_nascimento="2016-07-22"
    )

    # Acrescenta mais 3 moradores com ensino superior completo e idades variadas
    carla = Morador.objects.create(
        username="carla",
        nome="Carla",
        idade=28,
        sexo="F",
        data_nascimento="1996-02-10",
        concluiu_superior=True
    )
    roberto = Morador.objects.create(
        username="roberto",
        nome="Roberto",
        idade=45,
        sexo="M",
        data_nascimento="1979-08-25",
        concluiu_superior=True
    )
    luciana = Morador.objects.create(
        username="luciana",
        nome="Luciana",
        idade=59,
        sexo="F",
        data_nascimento="1965-05-03",
        concluiu_superior=True
    )

    print("Dados de teste inseridos com sucesso!")

if __name__ == "__main__":
    run()