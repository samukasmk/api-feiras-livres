Criando um banco de dados
=========================

Crie um novo schema em seu banco de dados chamado: **api_feira_livre**, exemplo:

.. code-block:: sql

    CREATE DATABASE api_feira_livre;



Definindo o dados de conexão com banco de dados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Edite o arquivo ``src/config.py``
- Altere o atributo de conexão com o banco de dados **(SQLALCHEMY_DATABASE_URI)**


.. note:: Seguem abaixo, exemplos de conexão com o banco de dados

Exemplo de conexão com o PostgreSQL
----------------------------
.. code-block:: python

    SQLALCHEMY_DATABASE_URI = 'postgresql://usuario:senha@host/api_feira_livre'


Exemplo de conexão com o MySQL
----------------------------
.. code-block:: python

    SQLALCHEMY_DATABASE_URI = 'mysql://usuario:senha@host/api_feira_livre'


Exemplo de conexão com o SQLite
--------------

.. code-block:: python

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'api_feira_livre.db')


.. warning:: ATENÇÃO: Não UTILIZE o banco de dados **SQLite** em modo de PRODUÇÃO,
             pois o mesmo possui recursos limitados de uso, que oneram
             consideravelmente a performance.
