---
id: doc-arquitetura
title: Documento de Arquitetura
sidebar_label: Documento de Arquitetura
---

# 1 Introdução

## 1.1 Finalidade

O documento de arquitetura tem o objetivo de especificar decisões arquiteturais relevantes ao projeto iFood, descrevendo seus aspectos e funcionalidades do sistema de forma clara e objetiva, onde serão utilizadas as tecnologia Django REST Framework e React Native.

## 1.2 Escopo

Este documento se aplica à produção do aplicativo iFood, implementado para as plataformas IOS e Android, representando a arquitetura utilizada.

# 2 Representação da Arquitetura

## 2.1 Diagrama de relações

![relacoes](assets/relacoes.png)

O diagrama apresenta cada etapa que será seguido para que o aplicativo funcione, relacionando o front-end com o back-end.

## 2.2 Diagrama React/Redux/Microsserviços

imagem

### React-Native

O React-Native é um framework que utiliza o mesmo design que o React tendo aplicação na construção de aplicativos mobile utilizando apenas javascript e traz uma rica interface, a partir de componentes declarativos, para o ambiente mobile. O React-Native trás uma propósta rápida e prática para recarregar o aplicativo instantâneamente, sem precisar compilar, com o "Hot Recoading", que tem como objetivo trazer um feedback em menos de 1 segundo. Este framework combina os componentes escritos em Objective-C, Java, ou Swift, podendo ser escritas parte do aplicativo usando um código nativo.

### Redux

O Redux é um container de estado previsível para aplicativos JavaScript. Esse container ajuda a manter a consistência dos aplicativos em ambientes diferentes, sendo fácil de testar e proporcionando uma boa experiência ao desenvolvedor.

### Micro Serviços


## 2.2 Diagrama Django REST Framework

![rest](assets/rest.png)

### Model

A model é a representação dos, permitindo obter informações do banco de dados sem conhecer a complexidade de tal. Essa camada contém tudo sobre os dados: como acessar, validar, comprotamentos e relações entre dados.

### View

A view controla o fluxo de informações entre a model e o template. Essa camada utiliza lógica programada para decidir quais informações serão extraídas do banco de dados e quais serão transmitidas para exibição.

### Serializer

### URL

### Test


# 3 Metas e Restrições de Arquitetura

Para o desenvolvimento deste projeto serão ultilizadas as seguintes tecnologias:

- React-native: Utilizado para a construção do aplicativo em IOS e Android;
- Redux: Utilizado para armazenar e resgatar dados dentro da aplicação React;
- Python: Versão 3.6 como linguagem base das aplicações back-end
- Django: Framework para desenvolvimento de aplicações web em python
- Django REST Framework: Utilizado para construção de API's e micro serviços;
- RabbitMQ: Barramento de mensagens entre os micro serviços e o aplicativo;
- PostgreSQL: Banco de Dados relacional;

# 4 Visão de Implementação

## 4.1 Modelagem de dados

imagem

## 4.2 Diagrama de Pacotes

### Front-end

imagem

### Back-end


![diagrama_pacotes_back](assets/diagrama_pacotes_back.png)

# 5 Pipeline

## APP

imagem

## Micro serviços

imagem
