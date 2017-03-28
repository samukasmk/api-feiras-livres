Executando a aplicação
=======================


Em modo desenvolvedor (runserver)
------------------------------------------

Para executar a aplicação em sua maquina local, utilize o script (manage.py) com a opção de runserver, exemplo:

.. code-block:: python

    cd src
    ../venv/bin/python manage.py runserver


Em ambientes de produção (uwsgi)
------------------------------------------

Para ambientes de produção recomendo o uwsgi, porem não irei me extender por agora com os exemplos de nginx servindo como proxy reverso, por este ser um projeto de exemplo, caso haja interesse, posso adicionar futuramente os arquivos de configuração de vhost com uwsgi:

.. code-block:: python

    cd src
    ../venv/bin/uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi
