---
id: devops-cicd
title: Integração contínua
sidebar_label: Integração contínua
---

Integração contínua

# TravisCI

O Travis basicamente é uma ferramenta de execução de scripts em ambientes controlados. Esses scripts são acionados a partir de um push ou pull request realizado no repositório. Travis é capaz de perceber isso a partir da integração com o github que emite webhooks baseado em eventos no repositório.

Tendo o poder de executar scripts de acordo com eventos, pode-se realizar a suite de testes no momento do pull request e garantir que todos os testes estão passando como esperado. Pode-se executar builds de executáveis, realizar deploy da aplicação, etc.

Como o travis também te permite controlar o ambiente em que são executados os scripts, adicionando dependências, selecionando sistema operacional que executará o script, defindo variáveis de ambiente. É possível realizar testes em diferentes plataformas, realizar o deploy em diferentes ambientes, etc.

## Etapas
O travis permite o controle dos jobs sendo executados em stages. Um job é um ambiente separado que executará um script, podem haver vários jobs sendo executados em paralelo, os jobs estão dentro de uma build, que é o controle geral do travis para quando o travis é acionado.

Stages tornam possível a execução ordenada dos jobs. Em um stage podem ocorrer jobs paralelos, porém só se passa para o próximo stage quando todos os scripts forem executados e tiverem passado.

## Atualmente em Integra-Vendas
Atualmente o CI está separado nas etapas:
* Teste
* Build e publicação da imagem docker versionada no docker hub
* Deploy

### Etapa de Teste
Na etapa de testes são executados:
* Testes unitários
* Checagem do container de desenvolvimento
* Checagem do container de produção
* Publicação do relatório de testes no codecov

Essa etapa é a mais importante quando se trata de integração contínua, é nela que se garante que o código que o desenvolvedor sobe para o repositório está estável, ou seja, não quebrou outras funcionalidades.

### Etapa de Build e Publish
Na etapa de build e publicação do docker é executado apenas um script que realiza todo o procedimento. Esse script é responsável por realizar a build da imagem e publicá-la com a versão correta no dockerhub. O padrão atual de versionamento da imagem é:
* prefixo: integravendas
* nome: nome do serviço
* versão
  * desenvolvimento: latest
  * produção: latest-stable
  * produção versionada: stable-1.0

Ex.: integravendas/product-microservice:stable-1.0

### Etapa de Deploy

