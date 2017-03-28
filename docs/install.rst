Instalação
==========

Clonando o projeto do github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ git clone git@github.com:samukasmk/api-feiras-livres.git

Criando um virtualenv para o projeto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ cd api-feiras-livres
    $ virtualenv --python=python3.5 --no-site-packages venv


Ativando o novo virtualenv ao seu path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Segue um exemplo para ativar o virtualenv ao seu path

.. code-block:: bash

    $ source venv/bin/activate

.. note:: Apesar de ter acabado de mencionar, vou prosseguir os exemplos como se não tivesse ativado, para ficar mais declarativo, exemplo quando menciono **(./venv/bin/python)**

Instalando as dependências (dentro do novo virtualenv)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Em produção
-------------------------------------

.. code-block:: bash

    $ ./venv/bin/pip install -r requirements/prod.txt


Em desenvolvimento (com as ferramentas de testes)
-------------------------------------

.. code-block:: bash

    $ ./venv/bin/pip install -r requirements/dev.txt
