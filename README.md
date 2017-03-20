api-feiras-livres
===
**Desenvolvido por:** Samuel Sampaio (@samukasmk)

**Descrição:** Esse projeto consiste em uma API, desenvolvido com o framework Flask, para expor os dados das feiras livres da cidade de São Paulo.

Os dados podem ser baixados através do link:
- http://www.prefeitura.sp.gov.br/cidade/secretarias/upload/chamadas/feiras_livres_1429113213.zip

Essa API foi construida, baseada na estrutura de dados do arquivo (DEINFO_AB_FEIRASLIVRES_2014.csv), contida no zip acima.

Como os dados da feiras são abertos, também construi uma API sem autenticação com dados abertos.

# 1. Requisitos
- **Python:** 3.5.2
- **Pip:** 9.0.1 (ou superior)
- **Flask:** 0.12
- **Flask-SQLAlchemy:** 2.2
- **SQLAlchemy:** 1.1.6
- **Flask-RESTful:** 10.3.5
- **Flask-Migrate:** 12.0.3
- **Flask-Script:** 12.0.5
- **uWSGI:** 2.0.14 (para produção apenas)
- **mysqlclient:** 1.3.10 (se caso optar por banco de dados Mysql)

# 2. Instalação

### 2.1. Clonando este projeto

```bash
$ git clone git@github.com:samukasmk/api-feiras-livres.git
```

### 2.2. Criando um virtualenv para o projeto
```bash
$ cd api-feiras-livres
$ virtualenv --python=python3.5 --no-site-packages venv
```

### 2.3. Ativando o novo virtualenv ao seu path
Segue um exemplo para ativar o virtualenv ao seu path

```bash
source venv/bin/activate
```

> Obs: Apesar de ter acabado de mencionar, vou prosseguir os exemplos como se não tivesse ativado, para ficar mais declarativo, exemplo quando menciono **(./venv/bin/python)**

### 2.4. Instalando as dependências (dentro do novo virtualenv)

### 2.4.1. Em produção

```bash
$ ./venv/bin/pip install -r requirements/prod.txt
```

### 2.4.3. Em desenvolvimento (com as ferramentas de testes)

```bash
$ ./venv/bin/pip install -r requirements/dev.txt
```

### 2.5. Criando um banco de dados

Caso você opte por usar o Mysql ou PostgreSQL, crie um novo schema de banco de dados chamado: **api_feira_livre**, exemplo:

```sql
CREATE DATABASE api_feira_livre;
```

Se você optar por SQLite, desconsidere esse passo, pois a aplicação irá criar um arquivo, exemplo: 'api_feira_livre.db'

### 2.6. Definindo o dados de conexão com banco de dados
Edite o arquivo **(src/config.py)**, alterando os dados de conexão com o banco de dados no atributo **(SQLALCHEMY_DATABASE_URI)**

#### 2.6.1. Exemplo de utilização do banco de dados SQLite (Modo desenvolvedor, não utilize em produção)

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'api_feira_livre.db')
```

#### 2.6.2. Exemplo de utilização do banco de dados MySQL

```python
SQLALCHEMY_DATABASE_URI = 'mysql://usuario:senha@host/api_feira_livre'
```

#### 2.6.3. Exemplo de utilização do banco de dados PostgreSQL

```python
SQLALCHEMY_DATABASE_URI = 'postgres://usuario:senha@host/api_feira_livre'
```


### 2.7. Aplicando as alteração de banco de dados (via scripts de migrations)

Essa aplicação utiliza o Flask-Migrate para gerenciar as migrações de banco de dados, junto ao script de gerencia (manage.py), implementado pelo Flask-Script.

O Flask-Migrate define uma pasta **(src/migrations)** com scripts de alterações de bancos de dados.

Se a conexão com o banco de dados estiver correta, e o schema estiver criado, basta rodar os comandos abaixo, para se criar as tabelas:

```bash
$ cd src
$ ../venv/bin/python manage.py db upgrade
```

### 2.7. Executando a aplicação

#### 2.7.1. Em modo desenvolvedor (runserver)
Para executar a aplicação em sua maquina local, utilize o script (manage.py) com a opção de runserver, exemplo:

```bash
$ cd src
$ ../venv/bin/python manage.py runserver
```

#### 2.7.1. Em modo desenvolvedor (uwsgi)
Para ambientes de produção recomendo o uwsgi, porem não irei me extender por agora com os exemplos de nginx servindo como proxy reverso, por este ser um projeto de exemplo, caso haja interesse, posso adicionar futuramente os arquivos de configuração de vhost, exemplo de execução do uwsgi:

```bash
$ cd src
$ ../venv/bin/uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi
```

# 3. Utilizando a API

A API é implementada pela pacote Flask-RESTful, onde existem 2 principais endpoints:

-  **/api/v1/feiralivre/{registro}:** Manipulação de cada feira, é orientado pelo código de registro das feiras.

-  **/api/v1/feiraslivres/:** Consulta de varias feiras, podendo ser por filtro.

### 3.1. Cadastrando de uma nova feira:

**Endpoint:**
> POST /api/v1/feiralivre/{registro}

**Exemplo:**
```bash
$ curl -X POST http://127.0.0.1:8080/api/v1/feiralivre/6005-4 \
    -H "Content-Type: application/json" \
    -d '{
          "nome_feira": "ANGELICA",
          "bairro": "CONSOLACAO",
          "logradouro": "RUA MATO GROSSO C/ PARA",
          "numero": "S/N",
          "referencia": "TV DA RUA SERGIPE",
          "lat": -23550464,
          "long": -46659253,
          "setcens": 355030826000014,
          "areap": 3550308005013,
          "coddist": 26,
          "distrito": "CONSOLACAO",
          "codsubpref": 9,
          "subprefe": "SE",
          "regiao5": "Centro",
          "regiao8": "Centro"
        }'
```

### 3.2. Obtendo dados de uma feira pelo código de registro

**Endpoint:**
> GET /api/v1/feiralivre/{registro}

**Exemplo:**
```bash
$ curl -X GET http://127.0.0.1:8080/api/v1/feiralivre/6005-4 \
    -H "Content-Type: application/json"
```

### 3.3. Alterando dos campos cadastrados de uma feira, exceto seu código de registro:
**Endpoint:**
> PUT /api/v1/feiralivre/{registro}

**Exemplo:**
```bash
$ curl -X PUT http://127.0.0.1:8080/api/v1/feiralivre/6005-4 \
    -H "Content-Type: application/json" \
    -d '{
          "nome_feira": "NOVO VALOR",
          "bairro": "NOVO VALOR",
          "logradouro": "NOVO VALOR",
          "numero": "NOVO VALOR",
          "referencia": "NOVO VALOR",
          "lat": 0,
          "long": 0,
          "setcens": 0,
          "areap": 0,
          "coddist": 0,
          "distrito": "NOVO VALOR",
          "codsubpref": 0,
          "subprefe": "NOVO VALOR",
          "regiao5": "NOVO VALOR",
          "regiao8": "NOVO VALOR"
        }'
```

### 3.4. Excluindo de uma feira através de seu código de registro:
**Endpoint:**
> DELETE /api/v1/feiralivre/{registro}

**Exemplo:**
```bash
$ curl -X DELETE http://127.0.0.1:8080/api/v1/feiralivre/6005-4 \
    -H "Content-Type: application/json"
```

### 3.5. Buscando de feiras utilizando ao menos um dos parâmetros abaixo:

**Endpoint:**
> GET /api/v1/feiraslivres/
- distrito=CONSOLACAO
- regiao5=Centro
- nome_feira=ANGELICA
- bairro=CONSOLACAO
- id=13

**Exemplo:**
```bash
$ curl -X GET \
    http://127.0.0.1:8080/api/v1/feiraslivres/?distrito=CONSOLACAO&regiao5=Centro&nome_feira=ANGELICA&bairro=CONSOLACAO \
    -H "Content-Type: application/json"
```

### 3.6. Buscando por todas feiras

**Endpoint:**
> GET /api/v1/feiraslivres/

**Exemplo:**
```bash
$ curl -X GET \
    http://127.0.0.1:8080/api/v1/feiraslivres/ \
    -H "Content-Type: application/json"
```


# 4. Trabalhando com Models

Para se gerenciar os dados atravéz de ORM, essa aplicação utiliza-se do Flask-SQLAlchemy, segue alguns exemplos de uso:


### 4.1. Inserindo dados das feiras (via models)

```python
>>> feira_angelica = FeiraLivre(
        registro = '6005-4',
        nome_feira = 'ANGELICA',
        bairro = 'CONSOLACAO',
        logradouro = 'RUA MATO GROSSO C/ PARA',
        numero = 'S/N',
        referencia = 'TV DA RUA SERGIPE',
        lat = -23550464,
        long = -46659253,
        setcens = 355030826000014,
        areap = 3550308005013,
        coddist = 26,
        distrito = 'CONSOLACAO',
        codsubpref = 9,
        subprefe = 'SE',
        regiao5 = 'Centro',
        regiao8 = 'Centro')
>>> db.session.add(feira_angelica)
>>> db.session.commit()
```

### 4.2. Pesquisando feiras pelo código de registro (via models)

```python
>>> feira_angelica = FeiraLivre.query.filter_by(registro='6005-4').first()
>>> feira_angelica.nome_feira
'ANGELICA'
```

### 4.3. Apagando um registo do banco de dados (via models)

```python
>>> db.session.delete(feira_angelica)
>>> db.session.commit()
```
