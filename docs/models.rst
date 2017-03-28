Trabalhando com Models
======================

Para se gerenciar os dados atravéz de ORM, essa aplicação utiliza-se do Flask-SQLAlchemy, segue alguns exemplos de uso:


Inserindo dados das feiras (via models)
----------------------------------------

.. code-block:: python

      feira_angelica = FeiraLivre(
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
      db.session.add(feira_angelica)
      db.session.commit()


Pesquisando feiras pelo código de registro (via models)
--------------------------------------------------------------

.. code-block:: python

    feira_angelica = FeiraLivre.query.filter_by(registro='6005-4').first()
    feira_angelica.nome_feira
    'ANGELICA'



Apagando um registo do banco de dados (via models)
--------------------------------------------------------------

.. code-block:: python

    db.session.delete(feira_angelica)
    db.session.commit()
