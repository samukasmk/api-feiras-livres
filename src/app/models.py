from app.database import db


class FeiraLivre(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    # required fields
    registro = db.Column(db.String(10), nullable=False, default='', unique=True)
    nome_feira = db.Column(db.String(100), nullable=False, default='')
    bairro = db.Column(db.String(100), nullable=False, default='')
    logradouro = db.Column(db.String(255), nullable=False, default='')
    # optional fields
    numero = db.Column(db.String(10), nullable=True)
    referencia = db.Column(db.String(300), nullable=True)
    lat = db.Column(db.Integer, nullable=True)
    long = db.Column(db.Integer, nullable=True)
    setcens = db.Column(db.BigInteger, nullable=True)
    areap = db.Column(db.BigInteger, nullable=True)
    coddist = db.Column(db.Integer, nullable=True)
    distrito = db.Column(db.String(100), nullable=True)
    codsubpref = db.Column(db.Integer, nullable=True)
    subprefe = db.Column(db.String(100), nullable=True)
    regiao5 = db.Column(db.String(100), nullable=True)
    regiao8 = db.Column(db.String(100), nullable=True)
    # extra fields
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    def __init__(self, registro, nome_feira, bairro, logradouro, **kwargs):
        # required fields
        self.registro = registro
        self.nome_feira = nome_feira
        self.bairro = bairro
        self.logradouro = logradouro
        # optional fields
        self.numero = kwargs.get('numero', None)
        self.referencia = kwargs.get('referencia', None)
        self.lat = kwargs.get('lat', None)
        self.long = kwargs.get('long', None)
        self.setcens = kwargs.get('setcens', None)
        self.areap = kwargs.get('areap', None)
        self.coddist = kwargs.get('coddist', None)
        self.distrito = kwargs.get('distrito', None)
        self.codsubpref = kwargs.get('codsubpref', None)
        self.subprefe = kwargs.get('subprefe', None)
        self.regiao5 = kwargs.get('regiao5', None)
        self.regiao8 = kwargs.get('regiao8', None)

    def __repr__(self):
        return '<app.models.FeiraLivre {}>'.format(self.registro)

    def serialize(self):
        serialized_dict = {}
        for column in self.__table__.columns:
            serialized_dict[column.name] = str(getattr(self, column.name))
        return serialized_dict

### Why i used .serialize() method instead .__dict__
# In [1]: import time
# In [2]: from app.models import FeiraLivre
# In [3]: feira_obj = FeiraLivre.query.filter_by(registro='6005-4').first()
#
# In [4]: def mensure__dict__method():
#    ...:     global feira_obj
#    ...:     start = time.time()
#    ...:     feira_obj.__dict__
#    ...:     end = time.time()
#    ...:     print(end - start)
#
# In [5]: def mensure_serialize_method():
#    ...:     global feira_obj
#    ...:     start = time.time()
#    ...:     feira_obj.serialize()
#    ...:     end = time.time()
#    ...:     print(end - start)
#
# In [6]: mensure__dict__method()
# 1.9073486328125e-06
# In [7]: mensure__dict__method()
# 1.9073486328125e-06
# In [8]: mensure__dict__method()
# 1.9073486328125e-06
#
# In [9]: mensure_serialize_method()
# 0.00011992454528808594
# In [10]: mensure_serialize_method()
# 0.0001239776611328125
# In [11]: mensure_serialize_method()
# 0.0001468658447265625

### Example of Insert:
# In [12]: feira_angelica = FeiraLivre(
#     ...:     registro = '6005-4',
#     ...:     nome_feira = 'ANGELICA',
#     ...:     bairro = 'CONSOLACAO',
#     ...:     logradouro = 'RUA MATO GROSSO C/ PARA',
#     ...:     numero = 'S/N',
#     ...:     referencia = 'TV DA RUA SERGIPE',
#     ...:     lat = -23550464,
#     ...:     long = -46659253,
#     ...:     setcens = 355030826000014,
#     ...:     areap = 3550308005013,
#     ...:     coddist = 26,
#     ...:     distrito = 'CONSOLACAO',
#     ...:     codsubpref = 9,
#     ...:     subprefe = 'SE',
#     ...:     regiao5 = 'Centro',
#     ...:     regiao8 = 'Centro')
# In [13]: db.session.add(feira_angelica)
# In [14]: db.session.commit()

### Example of Query:
# In [15]: feira_angelica = FeiraLivre.query.filter_by(registro='6005-4').first()

### Example of Delete:
# In [16]: db.session.delete(feira_angelica)
# In [17]: db.session.commit()

### Example of Queries in Views:
# @app.route('/user/<username>')
# def get_feira(registro):
#     feira_obj = FeiraLivre.query.filter_by(registro='6005-4').first_or_404()
#     return render_template('get_feira.html', user=feira_obj)
