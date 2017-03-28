api-feiras-livres
========================================

O **api-feiras-livres** é um projeto, desenvolvido com o framework `Flask <http://flask.pocoo.org>`_,
para prover uma **API REST**, sobre os dados abertos de feiras livres que
acontecem na cidade de São Paulo.

A prefeitura de São Paulo fornece esses dados abertos, por meio de arquivos CSV
compactados (segue o link para download):

http://www.prefeitura.sp.gov.br/cidade/secretarias/upload/chamadas/feiras_livres_1429113213.zip

Essa API foi construida, baseada na estrutura de dados do arquivo (DEINFO_AB_FEIRASLIVRES_2014.csv), contida no zip acima.

Esse projeto foi desenvolvido por: **Samuel Sampaio**



Guia do usuário
------------

Esta parte da documentação irá demonstrar como instalar e utilizar a
aplicação **api-feiras-livres**.

.. toctree::
   :maxdepth: 4

   dependencies
   install
   database
   migrations
   run
   api
   unittests
   models
   populate
   docs
