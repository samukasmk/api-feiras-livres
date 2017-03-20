from flask import url_for

class MockedModelFeiraLivre:
    def __init__(self, **kwargs):
        self.registro = '6005-4'
        self.nome_feira = 'ANGELICA'
        self.bairro = 'CONSOLACAO'
        self.logradouro = 'RUA MATO GROSSO C/ PARA'
        self.numero = 'S/N'
        self.referencia = 'TV DA RUA SERGIPE'
        self.lat = -23550464
        self.long = -46659253
        self.setcens = 355030826000014
        self.areap = 3550308005013
        self.coddist = 26
        self.distrito = 'CONSOLACAO'
        self.codsubpref = 9
        self.subprefe = 'SE'
        self.regiao5 = 'Centro'
        self.regiao8 = 'Centro'

    def first(self):
        return self

    def serialize(self):
        return {'a':'b'}


class TestApp:
    def test_get_feiralivre(self, mocker, client):

        mocker.patch(
            'app.models.FeiraLivre.query',
            return_value=MockedModelFeiraLivre())

        res = client.get(url_for('feiralivre_api.get_feiralivre', registro='aa'))
        assert res.status_code == 200, 'Ensure respose 200 of endpoint get_feiralivre'
        assert 'registro' in res.json.keys(), 'Ensure json return with registro key'
