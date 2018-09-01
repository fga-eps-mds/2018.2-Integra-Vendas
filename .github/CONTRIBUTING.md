# Guia de Contribuição  

## Como contribuir?

Para contribuir com o projeto é muito fácil e cada pouquinho conta! Basta seguir os seguintes passos:

* *Fork* do repositório (apenas para usuários externos)
* Criar [*issues*](CONTRIBUTING.md#política-de-issues)
* Criar [*branchs*](CONTRIBUTING.md#política-de-branches)
* Seguir a política de [*commits*](CONTRIBUTING.md#política-de-commits)
* Submeter [*Pull Request*](CONTRIBUTING.md#política-de-merges-e-pull-requests)


### Política de Issues
Para criação de issue o [template Issue](docs/issue_template.md) deve ser seguido.

### Gitflow
Gitflow é o fluxo planejado para criação de branches. Afim de organizar e poder gerenciar melhor o projeto.

#### Nova funcionalidade
Novas funcionalidades sempre saem da branch **dev**, nunca da master.
```
git checkout origin dev
git pull origin dev --rebase
git checkout -b login/gmail-integration-#7
git push origin login/gmail-integration-#7

... coding ...

git merge origin dev
git push origin login/gmail-integration-#7

... Pull request to dev ...
```
#### HotFix
HotFix são atualizações esporádicas pequenas mas importantantes, de funcionalidades que já estão na branch de desenvolvimento ou produção.
```
git checkout origin dev
git pull origin dev --rebase
git checkout -b hotfix/gmail-integration-#7

... hot fix ...

git merge origin dev
git push origin hotfix/gmail-integration-#7

... Pull Request to dev ...
```

### Política de Branches  
#### *master*
Master é a branch de produção. Nela se encontra a versão que estará disponível para utilização no mercado.

#### *dev*
Dev é a branch de homologação. Nela se encontra a versão mais atualizada e estável do projeto.

#### Nome das Branches
As branches seguirão o nome de contexto/artefato
* tema/funcionalidade-issue
* doc/documento

```
git checkout -b docs/EAP
```
```
git checkout -b login/gmail-integration-#7
```

### Política de Commits
Os commits serão feitos em inglês, tanto título quanto descrição
```
git commit -m "#1 Finishing login"
```

A issue pode ser referenciada no commit basta adicionar `#<numero da issue>`.

#### Pareamento
```
#1 Adding autolayout to signup window


Co-authored-by: Nome do individuo <email@email.com>
Co-authored-by: Nome de outro individuo <outroemail@email.com>
```

*Obs.: Atentar-se ao duplo espaçamento entre a descrição do commit e a definição dos autores

#### Exemplo de descrição do commit:
```
Fix #1 Finishing login
```
```
Fix #1 Fixing bug - missing labels
```
```
#1 Creating basic layout
```
```
#1 Creating unit tests for login
```

### Política de Merges e Pull Requests

#### Pull Requests

Pull requests serão realizados para controle de estabilidade das branches:
* master
* dev

Deve ser seguido o [template Pull Request](docs/pull_request_template.md).

##### Code Review
Ao menos um membro deve realizar a revisão das mudanças realizadas no pull request.
O revisor deve clonar a branch do pull request e verificar se o pull request é coerente.
Em caso de aceitação, deve-se fazer a aprovação e realizar o merge.
Caso o pull request esteja faltando algum requisito, deve-se propor as mudanças necessárias.
Caso o pull request não faça sentido ou já tenha sido resolvido, ou seja duplicado, deve ser fechado e feito um comentário coerente.
