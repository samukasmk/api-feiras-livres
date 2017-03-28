Populando o banco de dados com o CSV
=====================================

Para facilitar o manuseio da aplicação, criei um script para importação dos dados do CSV (via manage.py)

Para importar os dados do CSV ao banco de dados (lembrando que o banco já tenha que estar com os migrations executado) utilize o comando:


.. code-block:: bash

    $ cd api-feiras-livres
    $ source venv/bin/activate
    $ cd src
    $ ./manage populate_from_csv <PATH do Arquivo CSV>


Esse arquivo pode ser baixado diretamente do site da prefeitura, pelo link:

http://www.prefeitura.sp.gov.br/cidade/secretarias/upload/chamadas/feiras_livres_1429113213.zip
