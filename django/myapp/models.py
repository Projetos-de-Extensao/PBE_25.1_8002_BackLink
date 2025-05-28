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

    RELACAO_CHOICES = [
        ('01', 'Pessoa responsável pelo domicílio'),
        ('02', 'Cônjuge ou companheiro(a) de sexo diferente'),
        ('03', 'Cônjuge ou companheiro(a) do mesmo sexo'),
        ('04', 'Filho(a) do responsável e do cônjuge'),
        ('05', 'Filho(a) somente do responsável'),
        ('06', 'Enteado(a)'),
        ('07', 'Genro ou nora'),
        ('08', 'Pai, mãe, padrasto ou madrasta'),
        ('09', 'Sogro(a)'),
        ('10', 'Neto(a)'),
        ('11', 'Bisneto(a)'),
        ('12', 'Irmão ou irmã'),
        ('13', 'Avô ou avó'),
        ('14', 'Outro parente'),
        ('15', 'Agregado(a)'),
        ('16', 'Convivente'),
        ('17', 'Pensionista'),
        ('18', 'Empregado(a) doméstico(a)'),
        ('19', 'Parente do(a) empregado(a) doméstico(a)'),
        ('20', 'Individual em domicílio coletivo'),
    ]
    relacao_com_responsavel = models.CharField("Relação com o Responsável pelo Domicílio", max_length=2, choices=RELACAO_CHOICES,  default=1)
    
    

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

    # Novos campos solicitados
    pontos_coleta_lixo = models.TextField(
        "Pontos de coleta de lixo específicos da residência", blank=True, null=True
    )
    tempo_conclusao_falecimento = models.CharField(
        "Tempo para conclusão do processo de falecimento", max_length=100, blank=True, null=True
    )
    abastecimento_agua = models.CharField(
        "Como está sendo feito o abastecimento de água no domicílio", max_length=200, blank=True, null=True
    )
    abastecimento_energia = models.CharField(
        "Como está sendo feito o abastecimento de energia elétrica no domicílio", max_length=200, blank=True, null=True
    )
    energia_internet = models.BooleanField(
        "Chega energia elétrica e conexão de internet no domicílio?", default=False
    )
    demandas_basicas = models.TextField(
        "Principais demandas de necessidades básicas", blank=True, null=True
    )
    perguntas_religiao_indigena = models.TextField(
        "Perguntas sobre religião e relacionadas a indígenas", blank=True, null=True
    )
    relacao_outras_ilhas = models.TextField(
        "Como funciona a relação com as outras ilhas", blank=True, null=True
    )
    nome_rua = models.CharField(
        "Nome da rua", max_length=50, blank=True, null=True,
        choices=[
            ('R. Marina do Sol', 'R. Marina do Sol'),
            ('R. Marina do Frade', 'R. Marina do Frade'),
            ('R. Marina dos Coqueiros', 'R. Marina dos Coqueiros'),
            ('R. Marina da Lua', 'R. Marina da Lua'),
            ('R. Marina do Bosque', 'R. Marina do Bosque'),
            ('R. Marina Porto Bali', 'R. Marina Porto Bali'),
            ('R. Marina das Flores', 'R. Marina das Flores'),
            ('R. Marina das Estrelas', 'R. Marina das Estrelas'),
            ('R. Marina Ponta Leste', 'R. Marina Ponta Leste'),
        ]
    )
    numero_casa = models.CharField(
        "Número da casa", max_length=10, blank=True, null=True
    )
    endereco = models.CharField(
        "Endereço", max_length=200, blank=True, null=True
    )
    quantidade_dormitorios = models.PositiveIntegerField(
        "Quantidade de dormitórios para os moradores", default=0, blank=True, null=True
    )
    quantidade_banheiros_chuveiro = models.PositiveIntegerField(
        "Banheiros com chuveiro e vaso sanitário", default=0, blank=True, null=True
    )
    quantidade_banheiros_sem_chuveiro = models.PositiveIntegerField(
        "Banheiros sem chuveiro mas com vaso sanitário", default=0, blank=True, null=True
    )
    acesso_internet = models.BooleanField(
        "Algum morador tem acesso a internet no domicílio?", default=False
    )
    maquina_lavar_roupa = models.BooleanField(
        "Tem uma máquina de lavar roupa?", default=False
    )

    # Situação do imóvel
    SITUACAO_IMOVEL_CHOICES = [
        ('A', 'Ainda pagando'),
        ('L', 'Alugado'),
        ('E', 'Por empregador'),
        ('F', 'Por familiar'),
        ('O', 'Outra forma'),
        ('C', 'Outra condição'),
        ('J', 'Já pago, herdado ou ganho'),
    ]
    situacao_imovel = models.CharField(
        "Situação do imóvel", max_length=1, choices=SITUACAO_IMOVEL_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return f"Domicílio em {self.municipio}, UF: {self.uf}"


    registro_nascimento = models.CharField(
        "Registro de nascimento",
        max_length=50,
        choices=[
            ('cartorio', 'Do cartório'),
            ('indigena', 'Registro administrativo de nascimento indígena'),
            ('nao_tem', 'Não tem'),
            ('nao_sabe', 'Não sabe'),
        ],
        blank=True, null=True
    )
    possui_conjuge = models.BooleanField(
        "Possui cônjuge ou companheiro(a)?", default=False
    )
    vive_com_conjuge = models.BooleanField(
        "Vive em companhia de cônjuge ou companheiro(a)?", default=False
    )
    nome_conjuge = models.CharField(
        "Nome do cônjuge", max_length=100, blank=True, null=True
    )
    tipo_uniao = models.CharField(
        "Tipo da união",
        max_length=30,
        choices=[
            ('civil_religioso', 'Casamento civil e religioso'),
            ('civil', 'Só casamento civil'),
            ('religioso', 'Só casamento religioso'),
            ('consensual', 'União consensual'),
        ],
        blank=True, null=True
    )

    # Trabalho
    trabalhou_remunerado = models.BooleanField(
        "Trabalhou ou estagiou em atividade remunerada?", default=False
    )
    qtd_trabalhos = models.PositiveIntegerField(
        "Quantos trabalhos tinha nos últimos meses?", default=0, blank=True, null=True
    )
    ocupacao = models.CharField(
        "Ocupação, cargo ou função", max_length=100, blank=True, null=True
    )
    atividade_empresa = models.CharField(
        "Principal atividade do negócio ou empresa", max_length=100, blank=True, null=True
    )
    carteira_assinada = models.BooleanField(
        "Carteira de trabalho assinada?", default=False
    )
    empresa_cnpj = models.BooleanField(
        "Empresa registrada no CNPJ?", default=False
    )
    faixa_rendimento = models.CharField(
        "Faixa de rendimento",
        max_length=2,
        choices=[
            ('1', '1,00 a 500,00'),
            ('2', '501,00 a 1.000,00'),
            ('3', '1.001,00 a 2.000,00'),
            ('4', '2.001,00 a 3.000,00'),
            ('5', '3.001,00 a 5.000,00'),
            ('6', '5.001,00 a 10.000,00'),
            ('7', '10.001,00 a 20.000,00'),
            ('8', '20.001,00 a 100.000'),
            ('9', '100.001 ou mais'),
        ],
        blank=True, null=True
    )

    # Deficiência
    dificuldade_enxergar = models.CharField(
        "Dificuldade para enxergar",
        max_length=1,
        choices=[
            ('1', 'Tem, não consegue de modo algum'),
            ('2', 'Tem muita dificuldade'),
            ('3', 'Tem alguma dificuldade'),
            ('4', 'Não tem dificuldade'),
        ],
        blank=True, null=True
    )
    dificuldade_andar = models.CharField(
        "Dificuldade para andar ou subir degraus",
        max_length=1,
        choices=[
            ('1', 'Tem muita dificuldade'),
            ('2', 'Tem, não consegue de modo algum'),
            ('3', 'Tem alguma dificuldade'),
            ('4', 'Não tem dificuldade'),
        ],
        blank=True, null=True
    )

    # Educação
    sabe_ler_escrever = models.BooleanField(
        "Sabe ler e escrever?", default=False
    )
    frequenta_escola = models.CharField(
        "Frequenta escola ou creche?",
        max_length=1,
        choices=[
            ('1', 'Sim'),
            ('2', 'Não, mas já frequentou'),
            ('3', 'Não, nunca frequentou'),
        ],
        blank=True, null=True
    )
    curso_frequentado = models.CharField(
        "Curso que frequenta",
        max_length=2,
        choices=[
            ('1', 'Pré escola'),
            ('2', 'Creche'),
            ('3', 'Alfabetização de jovens e adultos'),
            ('4', 'Regular do ensino fundamental'),
            ('5', 'EJA do ensino fundamental'),
            ('6', 'Regular do ensino médio'),
            ('7', 'Superior de graduação'),
            ('8', 'EJA do ensino médio'),
            ('9', 'Especialização de nível superior'),
            ('10', 'Mestrado'),
            ('11', 'Doutorado'),
            ('12', 'Nenhum'),
        ],
        blank=True, null=True
    )
    concluiu_superior = models.BooleanField(
        "Já concluiu algum outro curso superior de graduação?", default=False
    )

    # Deslocamento para trabalho
    local_trabalho = models.CharField(
        "Local de trabalho", max_length=100, blank=True, null=True
    )
    retorna_casa = models.BooleanField(
        "Retorna do trabalho para casa 3 dias ou mais na semana?", default=False
    )
    tempo_casa_trabalho_horas = models.PositiveIntegerField(
        "Horas entre casa e trabalho", default=0, blank=True, null=True
    )
    tempo_casa_trabalho_minutos = models.PositiveIntegerField(
        "Minutos entre casa e trabalho", default=0, blank=True, null=True
    )
    principal_transporte = models.CharField(
        "Principal meio de transporte",
        max_length=2,
        choices=[
            ('1', 'A pé'),
            ('2', 'Bicicleta'),
            ('3', 'Motocicleta'),
            ('4', 'Mototáxi'),
            ('5', 'Automóvel'),
            ('6', 'Táxi ou assemelhados'),
            ('7', 'Van, perua ou assemelhados'),
            ('8', 'Ônibus'),
            ('11', 'Caminhonete ou caminhão adaptado'),
            ('12', 'Embarcação de médio e grande porte'),
            ('13', 'Embarcação de pequeno porte'),
            ('14', 'Outros'),
        ],
        blank=True, null=True
    )

    # Autismo
    autismo_diagnostico = models.BooleanField(
        "Já foi diagnosticado(a) com autismo por profissional de saúde?", default=False
    )

    # Dados de contato
    contato_nome = models.CharField(
        "Nome para contato", max_length=100, blank=True, null=True
    )
    contato_email = models.EmailField(
        "E-mail para contato", blank=True, null=True
    )
    contato_telefone = models.CharField(
        "Telefone para contato", max_length=20, blank=True, null=True
    )

    # Religião ou culto
    religiao_culto = models.CharField(
        "Qual é sua religião ou culto?", max_length=100, blank=True, null=True
    )


