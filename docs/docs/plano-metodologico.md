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
# 3 Técnicas de planejamento

---
# 4 Métricas de gerenciamento

---
# 5 Técnicas de codificação

---
# 6 Referências