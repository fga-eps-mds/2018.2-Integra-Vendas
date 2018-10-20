---
id: devops-ambiente
title: Configuração de Ambiente
sidebar_label: Configuração de ambiente
---

O projeto integra-vendas é separado em um backend com microserviços desenvolvidos em django e um frontend mobile, desenvolvido em react-native. Este documento é direcionado ao backend do projeto.

## Ambientes
* Desenvolvimento (Docker + Docker-Compose)
* Homologação (Heroku)
* Produção (Docker + DockerHub + Kubernetes)

### Ambiente de Desenvolvimento
No desenvolvimento é utilizado Docker para isolar o ambiente. O [Docker](https://www.docker.com) é uma tecnologia que possibilita isolar um ambiente. Diferente das Máquinas virtuais que tendem a criar um SO completo em cima de outro, o docker propõe um isolamento com foco em dependências e processos, isso diminui a carga sobre o host.

A definição da imagem a ser utilizada pelo container é feita em um Dockerfile, um arquivo de configuração para criação de imagens do docker. Em nosso projeto existem dois Dockerfiles, um para desenvolvimento e outro para produção. Basicamente a diferença entre eles esta nas dependências adicionadas à imagem e no comando que é executado quando se entra no container.

### Ambiente de Homologação
O ambiente de homologação é no [Heroku](https://www.heroku.com/) pois é uma plataforma Free com recursos limitados, que possibilita verificar já com a configuração de produção como estaria o sistema.

### Ambiente de Produção
O ambiente de produção ocorre em kubernetes, antes utilizamos o rancher 2.0 no Digital Ocean, porém quando acabou o saldo inicial concedido, migramos para a Google Cloud Platform, que possui o Kubernetes Engine.

As imagens utilizadas em produção são publicadas no DockerHub, um repositórios de imagens docker.

## Docker-compose
É utilizado o [docker-compose](https://docs.docker.com/compose/) a fim de facilitar a configuração de portas, volumes e rede do container.

## Shell scripts
A fim de executar um conjunto de comandos, tanto em desenvolvimento quanto a fim de otimizar os arquivos de CI, são utilizados scripts.

## Makefile
A fim de facilitar a utilização de comandos padrões para realizar as atividades de iniciar o sistema, entrar no container, rodar testes, etc. É utilizado o Makefile.

## Variáveis de Ambiente
De acordo com [Os 12 Fatores](https://12factor.net/pt_br/), que uma de suas propostas é a utilização de variáveis de ambiente. É utilizado um arquivo .env para guardar as configurações necessárias para se executar o sistema. O arquivo .env não é adicionado ao repositório, a fim de manter secreta as informações de configuração. Ainda sim são definidos valores padrões para desenvolvimento que permitem o levantamento do sistema sem que seja necessário definir tais variáveis, facilitando a vida dos desenvolvedores.

## Dependências separadas por ambiente
É utilizado arquivos de dependências distintos para os diferentes ambientes, sendo desenvolvimento, produção e heroku. Heroku utiliza as dependências de produção porém é adicionado também o gunicorn.

As dependências se localizam dentro da pasta requirements/ e se dividem entre, base.txt, dev.txt e prod.txt. Onde base.txt se localizam as dependências essenciais para o projeto funcionar. O arquivo dev.txt guarda dependências de profile, tests etc... E prod.txt, por enquanto vazio, guarda configurações de produção.
