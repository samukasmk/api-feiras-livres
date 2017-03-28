Documentações
=====================================

Build de arquivos html
-------------------------------------------------

Você pode gerar essa documentação locamente com o sphinx utilizando o comando:

.. code-block:: bash

    $ cd api-feiras-livres
    $ cd docs
    $ make html

E ao final desse comando será criado uma pasta com os arquivos html de documentação em ``docs/_build/html``


Buildando automaticamente
-------------------------
Se caso desejar desevolver e visualizar rapidamente execute o comando abaixo:

.. code-block:: bash

    $ cd api-feiras-livres
    $ sphinx-autobuild docs docs/_build/html

E acesse no navegador http://127.0.0.1:8000
