---
id: diagrama_de_classes
title: Diagrama de Classes
---

# Não precisa entregar para a AP1
## Introdução

<p align = "justify">
O diagrama de classes UML é um diagrama que mostra a estrutura do sistema desenhado no nível de classes e interfaces, ilustra as funcionalidades, dependências e relacionamentos de cada elemento. Pode ser vista como uma representação visual da arquitetura de um sistema. 
</p>

## Metodologia

<p align = "justify">
A equipe se reuniu por .... e realizou um brainstorm onde foram dicutidos os tópicos chaves e a arquitetura geral dos sistemas, e assim criamos...

Para a criação da primeira versão do diagrama de classes, a equipe utilizou o programa... Além disso, foi utilizado... para videoconferência e Visual Studio Code / Live Share para elaboração da documentação.
</p>

# ENTREGUE NO PRÓXIMO INCREMENTO
## Diagrama de Classes

### Versão 1.0


Este diagrama oferece uma visão clara e organizada da arquitetura de classes, tornando compreensível a interação entre diferentes componentes do sistema e suas responsabilidades.


![Diagrama de Classes](../assets/Diagrama_de_Classes/Diagrama_de_classes_01.png)


<strong>  - Pacote: Usuários  <strong>
Usuário: Classe base genérica da qual todas as outras classes de usuários herdam.
Recenseador: Especializado em trabalhar com formulários.
Administrador: Responsável pela gestão do editor de formulários.
Usuário Público: Limita-se a visualizações no dashboard.

   <strong>  - Formularios e Editor <strong>
Formulário: Onde os dados são coletados.
Editor de Formulário: Ferramenta de gerenciamento e edição dos formulários por parte dos administradores.


   <strong>  - Informações <strong>
Moradia e Informação Morador: Dados básicos de domicílios e seus ocupantes.
Características do Domicílio, Identificação Étnico-Racial, Registro Civil, Educação: Diferentes aspectos dos dados demográficos coletados.
Resultado do Formulário: Que armazena os dados processados e compilados.

   <strong> Dashboard> <strong>
Dashboard: Interface que permite visualizações e análises dos resultados compilados.


Usuários e suas funções: Cada tipo de usuário desempenha funções específicas no sistema, por exemplo:


   <strong> Relacionamentos <strong>
Recenseadores usam formulário para coleta de dados.
Administradores gerenciam o editor de formulários.
Usuários públicos têm acesso ao dashboard para visualização.
Coleta de Dados: Os formulários são essenciais para a coleta de diversos tipos de informações, como habitação e características dos moradores.

Dashboard e Resultados: Os resultados colhidos e processados alimentam o dashboard, que é onde as informações são centralizadas e visualizadas.
  
-------------------------------------------------NOVO DIAGRAMA DE CLASSES----------------------------------------------------------------------------------------------------------------------------------

![![Diagrama de Classes](../assets/diagrama_de_classes/diagrama_de_classes.png)](../assets/diagrama_de_classes/diagrama_de_classes.png)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






### Versão 1.1
![![Diagrama de Classes](../assets/diagrama_de_classes/diagrama_de_classes_1.1.png)](../assets/diagrama_de_classes/diagrama_de_classes_1.1.png)


### Versão 2.0

![![Diagrama de Classes](../assets/diagrama_de_classes/diagrama_de_classes_1.1.png)](../assets/diagrama_de_classes/diagrama_de_classes_2.0.png)


#### Rastreabilidade de Requisitos

| ID|Descrição|
|---|---|
|US17, US18, US19, US20|Torneio|
|US01, US06, US07, US08|Usuário|
|US45|Rodada|
|US35|Partida|






## Conclusão

<p align = "justify">
Através do diagrama de classes, foi possível representar a estrutura do sistema a nível de classes e auxiliar na modelagem da arquitetura geral, além do banco de dados. Ao longo do desenvolvimento da disciplina, iremos adaptar e evoluir o diagrama e sua documentação para refletir no estado atual do projeto.
</p>

## Referências

> UML Class and Object Diagrams Overview. Disponível em https://www.uml-diagrams.org/class-diagrams-overview.html. Acesso em 21/09/20

> UML Class Diagram Tutorial. Disponível em https://www.youtube.com/watch?v=UI6lqHOVHic. Acesso em 21/09/20

> UML Class Relationship Diagrams. Disponível em https://www.cs.odu.edu/~zeil/cs330/latest/Public/classDiagrams/index.html#other-class-diagram-elements Acesso em 19/10/20

## Autor(es)

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 21/09/20 | 1.0 | Criação do documento | João Pedro, Lucas Alexandre, Matheus Estanislau, Moacir Mascarenha e Renan Cristyan |
| 28/09/20 | 1.1 | Ajustes no documento | João Pedro e Renan Cristyan |
| 28/09/20 | 1.2 | Adicionado diagrama de classes 1.1 | João Pedro e Renan Cristyan |
| 26/10/20 | 2.0 | Adicionado diagrama de classes 2.0 | João Pedro, Lucas Alexandre, Matheus Estanislau, Moacir Mascarenha e Renan Cristyan |
