# SECOM IX

## Introdução sobre cultura DevOps
#### [Apresentação em slides](https://drive.google.com/file/d/15HDbwvaCPA27Pj15yc_mGai5uRdVmP-M/view?usp=sharing)

## Criar uma aplicação Flask
#### Uma aplicação básica
Instalar dependências para formulário:
```
flask-wtf
email-validator
```
#### Validar uma entrada de dados - nome e idade
#### Criar uma forma de validação de entrada
#### Criar testes unitários para as rotas criadas
#### Criar testes utilizando mock
Módulo `a.py`:
```python
import requests


def wget_google():
    print(requests.get(url='http://www.google.com').text)


class A:

    def metodo_a(self):
        print('executando metodo_a')

    def metodo_b(self):
        print('executando metodo_b')
```
Módulo test_exemplos.py
```python
from a import A
from unittest import mock, TestCase

class TestExamplesCase(TestCase):

    @mock.patch("app.tests.a.A.metodo_a")
    def test_a(self, metodo_a):
        metodo_a.side_effect = print('executando metodo mockado')
        a_instance = A()
        a_instance.metodo_a()
        a_instance.metodo_b()

    @mock.patch("app.tests.a.wget_google", return_value="Site não encontrado")
    @mock.patch("app.tests.a.requests.get", side_effect=print('Não encontrou o site'))
    def test_requests(self, get, wget_google):
        print(wget_google())
        wget_google()

```

## Conteinerização da aplicação
#### Docker
É uma plataforma aberta, criada com o objetivo de facilitar o desenvolvimento, a implantação e a execução de aplicações em ambientes isolados. 

> Isolamento

O modelo de isolamento utilizado no Docker é a virtualização a nível do sistema operacional, um método de virtualização 
onde o kernel do sistema operacional permite que múltiplos processos sejam executados isoladamente no mesmo host.
O container tem visão apenas do processo e não da máquina física.

![Virtualization vs Containers](./images/virtualization-vs-containers.png "Virtualization vs Containers")

Para criar o isolamento necessário do processo, o Docker usa a funcionalidade do kernel, denominada de namespaces, 
que cria ambientes isolados entre containers: os processos de uma aplicação em execução não terão acesso aos recursos de outra.
A menos que seja expressamente liberado na configuração de cada ambiente.

> Imagem

A imagem é a abstração da infraestrutura em estado somente leitura, de onde será instanciado o container.

> Container

Todo container é iniciado a partir de uma imagem, dessa forma podemos concluir que nunca teremos uma imagem em execução.
Traçando um paralelo com o conceito de orientação a objeto, a imagem é a classe e o container o objeto.
Vale ressaltar que a ideia dos containers é a de serem descartáveis. Caso você use o mesmo container por 
muito tempo sem descartá-lo, provavelmente está usando o Docker incorretamente. O Docker não é uma máquina, 
é um processo em execução. E, como todo processo, deve ser descartado para que outro possa tomar seu lugar na reinicialização do mesmo.
Não é uma boa escolhe utilizar containers para executarem SGBDs em produção.

> Docker Engine

É o software base de toda solução. É tanto o daemon responsável pelos containers como o cliente usado para enviar comandos para o daemon.

> Docker Compose

É a ferramenta responsável pela definição e execução de múltiplos contêineres com base em arquivo de definição.
Docker compose é uma ferramenta para definição e execução de múltiplos containers Docker.
Com ela é possível configurar todos os parâmetros necessários para executar cada container a partir de um arquivo de definição.
Geralmente utiliza-se variáveis de ambiente.


> Exemplo Docker

- Hello World em Docker

```shell script
$ docker container run hello-world
```

- Dockerfile Exemplo

Criar arquivo `soma.py`:
```python
num1 = int(input("Informe Numero 1:"))
num2 = int(input("Informe Numero 2:"))

print(num1 + num2)
```
E outro arquivo `Dockerfile`:
```dockerfile
FROM python:3.7.3
COPY soma.py /app/
CMD python /app/soma.py
```

- Criar imagem

```shell script
$ docker build -t my-app-demo:1.0 .
```

- Criar container
```shell script
$ docker container run -it my-app-demo:1.0
```

- Exemplo docker-compose

Criar arquivo `docker-compose.yml`:
```yaml
version: '3.7'

services:
  app_1:
    image: python:3.7.3
    container_name: app1
    command: |
      echo "Hello from app1"

  app_2:
    image: python:3.7.3
    container_name: app2
    command: |
      echo "Hello from app2"

```
E executar com:
```shell script
$ docker-compose up
```
> Docker Registry - [Docker Hub](https://hub.docker.com)


#### Criar Dockerfile
#### Criar Docker-compose

## Deploy do app no Heroku
#### O que é o Heroku
Heroku é uma _Plataform as a Service_ - __PaaS__, que permite desenvolvedores construir, executar e operar aplicações inteiras 
em cloud. PaaS é um tipo de computação em nuvem que permite aos desenvolvedores não se preocuparem com aspectos
da infra estrutura como provisionar instâncias, criar redes privadas e públicas e vários outros detalhes. 
Visa facilitar o processo de desenvolvimento colocando toda infra disponível e o desenvolvedor focar apenas na evolução da software.
Heroku permite o deploy de aplicações em várias linguagens:
- Java
- Node.js
- Scala
- Clojure
- Python
- PHP
- Go

#### Criar conta quem não tem
Para criar uma conta basta acessar o seguinte link: https://signup.heroku.com

#### Criar um app na plataforma
#### Fazer a publicação diretamente
##### Instalar Heroku CLI
Link para download e passos para instalação: https://devcenter.heroku.com/articles/heroku-cli#download-and-install

##### Login
```shell script
$ heroku login
```

##### Push Apps
```shell script
$ heroku container:push web --app <app_name>
$ heroku container:release web -a <app_name>
```

##### Visualizar Logs
```shell script
$ heroku logs --tail -a <app_name>
```

## Construir um CI/CD no GitHub Actions
#### Definir um flow para executar os testes - CI
#### Incrementar o flow para realizar o deploy
#### Definir um workflow para fazer deploy apenas na branch master

## Code Review
#### Separar projeto em branchs master e dev
#### Criar regras para aprovação de merge
#### Criar pull request e marcar alguém para realizar o review
