Executando os testes unitários
===============================

Os testes unitários dessa aplicação foram desenvolvidos com o framework `Py.test <http://doc.pytest.org/en/latest/>`_ e a biblioteca integradora: `pytest-flask <http://pytest-flask.readthedocs.io/>`_.


Como é executado os testes com o banco de dados
--------------------------------------------------

Como é muito complexo mockar objetos do banco (flask-sqlalchemy), segui uma pratica da própria documentação do flask, onde defini fixtures: localizado em: ``tests/conftest.py``

Antes de iniciar os testes:
  - é construido um objeto Flask app
    - forçando alterar a conexão com o banco dados (SQLITE Temporário) ``sqlite:///tests/db/testing.db``
      - Recriando o arquivo de banco de dados para testes ``tests/db/testing.db``
       - Executando os scripts de migração ``db upgrade``
        - Disponibilidando banco de dados SQLite APENAS para os testes


Executando os testes (com coverage simplificado)
--------------------------------------------------

Nesse exemplo abaixo vamos demonstrar a execução dos testes com o relatório de coberturar dos teste em **modo simplificado** imprimindo na telas

1. Acesse a pasta do projeto

.. code-block:: bash

    $ cd api-feiras-livres

2. Ative o virtualenv

.. code-block:: bash

    $ source venv/bin/activate

3. Acesse a pasta do projeto ``src``

.. code-block:: bash

    (venv) $ cd src

4. Chame o executavel do py.test

.. code-block:: bash

    (venv) $ py.test



Executando os testes (com coverage detalhado)
--------------------------------------------------

Nesse ultimo exemplo vamos demonstrar como executar os testes unitários, com o relatório de coberturar dos teste em **modo detalhado** gerando arquivos html


.. code-block:: bash

    $ cd api-feiras-livres

    $ source venv/bin/activate

    (venv) $ cd src

    (venv) $ py.test --cov-report=html


E ao final desse comando será criado uma pasta com os arquivos html dos relatórios de cobertura dos testes em ``src/html``



Analisando mais opções de testes
--------------------------------------------------

Caso queira deixar fixo um metódo de testes apenas, defina no arquivo de configuração:

``src/pytest.ini``

Como está o arquivo de configuração (``src/pytest.ini``) atualmente:

.. code-block:: ini

    [pytest]

    ; simplified coverage (just in screen)
    addopts = -ra -s -v --flakes --cov=.

    ; full coverage (at html files)
    ; addopts = -ra -s -v --flakes --cov-report=html --cov=.

    ; exclude unrelated folders and all old tests
    norecursedirs =
        .*
        env
        venv

    flakes-ignore =
      *.py UnusedImport
      *.py UnusedVariable
