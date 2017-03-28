Aplicando as alteração de banco de dados
========================================

Essa aplicação utiliza o Flask-Migrate para gerenciar as migrações de banco de dados, junto ao script de gerencia (manage.py), implementado pelo Flask-Script.

O Flask-Migrate define uma pasta ``src/migrations`` com scripts de alterações de bancos de dados.

Se a conexão com o banco de dados estiver correta, e o schema estiver criado, basta rodar os comandos abaixo, para se criar as tabelas:

.. code-block:: python

    $ cd api-feiras-livres

    $ source venv/bin/activate

    $ cd src

    (venv) $ ./manage.py db upgrade
