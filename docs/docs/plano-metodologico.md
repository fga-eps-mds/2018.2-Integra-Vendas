---
id: plano-metodologico
title: Plano Metodológico
sidebar_label: Plano Metodológico
---

Esse documento descreve o plano metodológico que será seguido no desenvolvimento do projeto além de detalhar as técnicas e os rituais que serão aplicados.

# 1 Papéis
## 1.1 Scrum Master
O Scrum Master tem como responsabilidade:
* Definir, adaptar e aplicar a metodologia de desenvolvimento que será utilizada na construção do produto;
* Definir métricas para analisar e melhorar a produtividade da equipe com base nos dados coletados;
* Garantir a execução da metodologia definida nesse documento.

## 1.2 Product Owner (PO)
O PO tem como responsabilidade:
* Definir escopo do produto com base nas necessidades dos *stakeholders*;
* Definir proposta de valor do produto;
* Analisar custos e a rentabilidade do projeto;
* Definir critérios de aceitação para as histórias de usuário;
* Definir e analisar métricas para garantir a entrega de valor do produto aos stakeholders;

## 1.3 Arquiteto
O Arquiteto tem como responsabilidade:
* Modelar e planejar a arquitetura do sistema;
* Acompanhar o desenvolvimento do produto para garantir que a arquitetura está sendo seguida.

## 1.4 DevOps
O DevOps tem como responsabilidade:
* Definir a política de contribuição para o projeto;
* Garantir a disponibilidade dos ambientes de desenvolvimento, homologação e produção;
* Garantir a integração e o *deploy* contínuo;
* Garantir o *gitflow*.

## 1.5 Desenvolvedor
O Desenvolvedor tem como responsabilidade:
* Seguir a metodologia e os rituais definidos pelo Scrum Master;
* Desenvolver o produto;
* Testar as soluções implementadas durante o desenvolvimento do produto garantindo uma cobertura de testes de pelo menos 90% do código;
* Seguir padrões, técnicas e boas práticas de programação definidas pelo Scrum Master.

---
# 2 Rituais
## 2.1 Sprints
A *sprint* é um período de tempo definido durante o qual é produzida uma versão incremental do produto. Uma *sprint* inicia imediatamente após a conclusão da *sprint* anterior e tem o objetivo de entregar um incremento potencialmente utilizável do produto [[1]](#6-referencias). As *sprints* do atual projeto terá as seguintes características:
* Duração: 7 dias;
* Todas as *sprints* começarão às 14 horas do sábado e se encerrarão 9 horas do sábado seguinte dando início, respectivamente, aos rituais de Revisão da *sprint*, Retrospectiva da *sprint*, Planejamento da *sprint* e Definição de riscos.

## 2.2 Daily Meeting
As *daily meetings* são a documentação do trabalho diário dos membros da equipe que serão utilizados para registrar o progresso do desenvolvimento do produto e observar as dificuldades encontradas pelos membros. A daily meeting terá as seguintes características:
* Duração: Máximo 10 minutos;
* Ocorrerão todos os dias às 14 horas;
* Serão estruturadas em três tópicos a serem respondidos:
	* "O que foi feito?"
	* "O que será feito?"
	* "Quais foram as dificuldades?"
* Devido a dificuldade da equipe de se encontrar diariamente para fazer um reunião presencial, as *daily meetings* serão registradas em um canal de texto nomeado "#daily" no Discord.

## 2.3 Revisão da Sprint
Uma reunião informal para validar o incremento do produto produzido na *sprint* atual e adaptar o *backlog* do produto se necessário [[1]](#6-referencias). No caso do deste processo de desenvolvimento nem todos os *stakeholders* estarão presentes na revisão do incremento do produto, pois a parte interessada analisará o produto em outro momento. A Revisão da *Sprint* terá as seguintes características:
* Duração de 1 hora;
* Envolverá a equipe de desenvolvimento, o Scrum Master, o PO, o Arquiteto e o DevOps.


## 2.4 Retrospectiva da Sprint
Ocorrendo após a Revisão da *sprint*, a Retrospectiva da *sprint* será o momento da equipe inspecionar a si própria criando assim um plano para melhorias a serem aplicadas na próxima *sprint* [[1]](#6-referencias). A Retrospectiva da *sprint* terá as seguintes características:
* Duração: 30 minutos;
* Será documentada anonimamente seguindo os tópicos:
	* Pontos positivos: Cada membro da equipe apontará pontos positivos da equipe durante a *sprint* que ocorreu;
	* Pontos de melhoria: Cada membro da equipe apontará pontos melhoria da equipe durante a *sprint* que ocorreu;
	* Sugestões de melhoria: Cada membro apresentará sugestões para solucionar os pontos de melhoria observados na *sprint* e, após a sugestão ser discutida pela equipe, as sugestões serão colocadas em prática.

## 2.5 Planejamento da Sprint
Com a colaboração de todo os papéis, é planejado o trabalho a ser realizado na *sprint*. Tendo como tarefa principal do Scrum Master garantir a execução do ritual o entendimento dos participantes sobre o propósito do mesmo [[1]](#6-referencias). O Planejamento da *sprint* terá as seguintes características:
* Duração: 3 horas;
* Primeiramente o PO analisa os Temas de negócio e, se necessário, extrai seus Épicos. A partir disso, os Épicos são analisados e são criadas, se necessário, Histórias de Usuário (US) com seus critérios de aceitação;
* As US são pontuadas pela equipe de desenvolvimento usando o *planning poker*;
* Depois de pontuadas as US, o PO e o Scrum Master definem quais US serão produzidas na *sprint*;
* O Scrum Master divide a equipe de desenvolvimento em pares e define os responsáveis pelo desenvolvimento das US escolhidas.

## 2.6 Identificação de riscos
A etapa de identificação de riscos se encontra tanto no início do projeto quanto durante todo o desenvolvimento. Listar os riscos externos e internos em tabelas ou planilhas é o indicado para uma boa identificação de riscos [[2]](#6-referencias). Neste projeto, os riscos serão identificados e pontuados no ritual de Identificação de riscos a cada *sprint* que terá as seguintes características:
* Duração: 1 hora;
* Com a colaboração de todos os papéis, a equipe identifica e lista os riscos internos e externos da *sprint*.
* Usando o *planning poker* a equipe define pontuações para os riscos demonstrando quais são os maiores riscos para o projeto e a equipe na *sprint* em que eles foram pontuados.

---
# 3 Ferramentas de planejamento
## 3.1 Issues
As *issues* no Github serão utilizadas para representar todas as tarefas que a equipe realizará durante a produção do software. Para a melhor identificação dessas tarefas as *issues* devem ter os seguintes atributos:
* Nome
* Descrição
* *Label*
* Responsáveis

## 3.2 Épicos
Os Épico provê uma camada extra na hierarquia das Issues definindo um tema que agrupa tarefas que serão realizadas e se comportando como grandes US [[3]](#6-referencias)[[4]](#6-referencias). No desenvolvimento do produto os Épicos terão o objetivo de agrupar US e terão os seguintes atributos:
* Código: EP## (#: número da EP);
* Nome: <código> - Eu como <ator> gostaria de <funcionalidade de alto nível> para <valor atribuído para o stakeholder>;
* Lista de USs atreladas ao Épico.

## 3.3 Histórias de Usuário (US)
As USs são descrições de alto nível de funcionalidades que definem incrementos no produto pela perspectiva dos *stakeholders* [[4]](#6-referencias). As USs serão documentadas nao GitHub como *issues* (seguindo todas as regras definidas anteriormente para *issues*) que obrigatoriamente deverão estar atreladas a Épicos e seguirão um template definido:
* Código/Nome: US## (#: número da US);
* Descrição: Eu como <ator> gostaria de <funcionalidade> para <valor atribuído para o *stakeholder*>;
* Tarefas: Lista de atividades que levam a produção da funcionalidade;
* Requisitos: Critérios de aceitação.

## 3.4 Milestones
As *Milestones* no GitHub são análogas às *sprints* definindo um período de tempo e documentando no repositório quais atividades serão realizadas em um determinado período [[4]](#6-referencias).

## 3.5 Planning Poker
O *Planning Poker* é um método de estimar *Story Points* (medida relativa de de esforço, complexidade e risco) a partir de comparações de tamanho relativo entre as US [[5]](#6-referencias). No projeto o *planning poker* será usado para estimar tanto as US quanto os riscos em uma determinada *sprint* com o auxílio do aplicativo Scrum Poker Cards [[6]](#6-referencias) que simula as cartas escritas com a sequência de Fibonacci.

## 3.6 Kanban
Para monitorar o trabalho da equipe será utilizado dois quadros de Kanban no *Projects* do GitHub:
* Quadro de desenvolvimento para manter o controle da produção das US que será dividido em Product Backlog, Sprint Backlog, In Progress, Testing e Done;
* Quadro geral para manter o controle de todas as outras atividades relacionadas ao produto como produção de documentos, reuniões, treinamentos, estudos e etc. Este quadro será dividido em To do, In progress e Done.

---
# 4 Métricas de gerenciamento
## 4.1 Velocity
O *velocity* é uma medida de *story points* concluídos em um determinado período de tempo, no caso desse projeto o tempo seria as *sprints* semanais. Essa medida apresenta a taxa de entrega de trabalho pela equipe e isso possibilita estimativas mais acuradas de *story points* que podem ser atribuídos ao time por *sprint* [[4]](#6-referencias).

Inicialmente a estimativa feita pode não ser tão acurada, mas com o passar das *sprits* essa acurácia tende a aumentar.

## 4.2 Burndown
O *burndown* mostra o trabalho que está completo relacionado com o *velocity* do projeto. O gráfico de *burndown* mostra como as projeto está andando, o que apresenta uma boa noção de quantos *story points* podem ser realizados em uma determinada *sprint* [[4]](#6-referencias).

## 4.3 Quadro de conhecimento
O quadro de conhecimentos representa como está o conhecimento de cada indivíduo da equipe em tecnologias e métodos que serão chave para o desenvolvimento do projeto. Esse quadro auxilia na identificação dos possíveis riscos internos no projeto e na estimativa inicial de capacidade de trabalho da equipe. A medição dos dados de conhecimento terão as seguintes características:
* Quando: A medição do conhecimento da equipe será feita no começo do projeto e antes de cada *release*;
* Como: Entro de cada tópico o nível de conhecimento será pontuado em Baixo - 1, Médio - 3, Alto - 5.


## 4.4 Riscos
Os riscos do projeto serão divididos em riscos internos e externos e serão descritos em tabelas [[2]](#6-referencias). Os riscos serão elicitados e pontuados a cada *sprint*.

---
# 5 Técnicas de codificação

---
# 6 Referências
[[1]](#6-referencias) SCHWABER, Ken; SUTHERLAND, Jeff. **Um guia definitivo para o Scrum**: As regras do jogo. Scrum Inc, 2013. 19 p.

[[2]](#6-referencias) JUNCKES, Gabriel Dias; MORGADO, Paulo. **Gerência de riscos em desenvolvimento de software**. 2013. Universidade do Sul de Santa Catarina. Disponível em: <https://www.devmedia.com.br/gerencia-de-riscos-em-desenvolvimento-de-software/28506>. Acesso em: 5 set. 2018.

[[3]](#6-referencias) PAQUETTE, Paige. **Working with Epics inside GitHub**: Introducing ZenHub Epics. 2016. Disponível em: <https://www.zenhub.com/blog/working-with-epics-in-github/>. Acesso em: 06 set. 2018.

[[4]](#6-referencias) BUTLER, Matt; PAQUETTE, Paige. **Better So ware & Stronger Teams**: Project Management for GitHub. Zenhub, 2016. Disponível em: <https://www.zenhub.com/github-project-management.pdf>. Acesso em: 04 set. 2018.

[[5]](#6-referencias) BRASILEIRO, Roberto. **Planning Poker**: A melhor maneira de estimar qualquer atividade. 2017. Disponível em: <http://www.metodoagil.com/planning-poker/>. Acesso em: 07 set. 2018.

[[6]](#6-referencias) artArmin. **Scrum Poker Cards**. Disponível em: <https://play.google.com/store/apps/details?id=artarmin.android.scrum.poker>. Acesso em: 07 set. 2018.

[[7]](#6-referencias) MEDEIROS, Manoel Pimentel. **Implementando Pair Programming em sua equipe**: Conhecendo as dificuldades e as vantagens dessa prática XP. 2007. Disponível em: <https://www.devmedia.com.br/implementando-pair-programming-em-sua-equipe/1694>. Acesso em: 8 set. 2018.