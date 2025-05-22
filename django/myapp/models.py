from django.db import models
from django.contrib.auth.models import User


class Morador(User):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    
    nome = models.CharField("Nome do Morador", max_length=100)
    sobrenome = models.CharField("Sobrenome", max_length=100)
    sexo = models.CharField("Sexo", max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField("Data de Nascimento")
    idade = models.PositiveIntegerField("Idade")
    
    

    def __str__(self):
        return f"{self.nome} {self.sobrenome} ({self.idade} anos)"


class Domicilio(models.Model):
    uf = models.CharField("UF", max_length=2)
    municipio = models.CharField("Município", max_length=100)
    distrito = models.CharField("Distrito", max_length=10)
    subdistrito = models.CharField("Subdistrito", max_length=10)
    setor = models.CharField("Setor", max_length=10)
    numero_quadra = models.CharField("Nº da Quadra", max_length=10)
    numero_face = models.CharField("Nº da Face", max_length=10)
    seq_endereco = models.CharField("Seq Endereço", max_length=10)
    seq_coletivo = models.CharField("Seq Coletivo", max_length=10, blank=True, null=True)
    seq_especie = models.CharField("Seq Espécie", max_length=10, blank=True, null=True)
    
    morador = models.ForeignKey(
        Morador,
        default=1,
        on_delete=models.CASCADE,
        related_name="domicilios"
    )

    quantidade_moradores = models.PositiveIntegerField(
        "Quantidade de Moradores",
        help_text="Número de pessoas que moram neste domicílio",
        default=1
    )
    acesso_agua_rede = models.BooleanField(
        "Acesso geral à rede de distribuição de água?",
        help_text="O domicílio tem acesso geral à rede de distribuição de água?",
        default=False
    )
    quantidade_comodos = models.PositiveIntegerField(
        "Quantidade de Cômodos",
        help_text="Número de cômodos deste domicílio",
        default=1
    )

    ESPECIE_CHOICES = [
        ('1', 'Domicílio Particular Permanente Ocupado'),
        ('5', 'Domicílio Particular Improvisado Ocupado'),
        ('6', 'Domicílio Coletivo com Morador'),
    ]
    especie_domicilio = models.CharField(
        "Espécie de Domicílio Ocupado",
        max_length=1,
        choices=ESPECIE_CHOICES
    )

    TIPO_CHOICES = [
        ('011', 'Casa'),
        ('012', 'Casa de vila ou em condomínio'),
        ('013', 'Apartamento'),
        ('014', 'Habitação em casa de cômodos ou cortiço'),
        ('015', 'Habitação indígena sem paredes ou maloca'),
        ('106', 'Estrutura residencial permanente degradada ou inacabada'),
        ('051', 'Tenda ou barraca de lona, plástico ou tecido'),
        ('052', 'Dentro do estabelecimento em funcionamento'),
        ('053', 'Outros (abrigos naturais e outras estruturas improvisadas)'),
        ('504', 'Estrutura improvisada em logradouro público, exceto tenda ou barraca'),
        ('505', 'Estrutura não residencial permanente degradada ou inacabada'),
        ('061', 'Asilo ou outra instituição de longa permanência para idosos'),
        ('062', 'Hotel ou pensão'),
        ('063', 'Alojamento'),
        ('064', 'Penitenciária, centro de detenção e similar'),
        ('065', 'Outro'),
        ('606', 'Abrigo, albergue ou casa de passagem para população em situação de rua'),
        ('607', 'Abrigo, casas de passagem ou república assistencial para outros grupos vulneráveis'),
        ('608', 'Clínica psiquiátrica, comunidade terapêutica e similar'),
        ('609', 'Orfanato e similar'),
        ('610', 'Unidade de internação de menores'),
        ('611', 'Quartel ou outra organização militar'),
        ('506', 'Veículos (Carros, Caminhões, Trailers, Barcos etc.)'),
        ('071', 'Asilo ou outra instituição de longa permanência para idosos'),
    ]
    tipo = models.CharField(
        "Tipo",
        max_length=3,
        choices=TIPO_CHOICES
    )

    def __str__(self):
        return f"Domicílio em {self.municipio}, UF: {self.uf}"


