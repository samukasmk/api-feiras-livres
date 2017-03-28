import os
import json
import tempfile
import pytest
from flask import url_for


class TestApiFeiraLivre:
    def setup_class(self):
        self.registro_id = 'FEIRA-TESTE'
        self.post_data = dict(
            nome_feira='ANGELICA',
            bairro='CONSOLACAO',
            logradouro='RUA MATO GROSSO C/ PARA',
            numero='S/N',
            referencia='TV DA RUA SERGIPE',
            lat=-23550464,
            long=-46659253,
            setcens=355030826000014,
            areap=3550308005013,
            coddist=26,
            distrito='CONSOLACAO',
            codsubpref=9,
            subprefe='SE',
            regiao5='Centro',
            regiao8='Centro')
        self.put_data = dict(
            nome_feira='NOVO NOME',
            bairro='PENHA',
            logradouro='NOVA RUA',
            numero='42')

    def test_1_post_feiralivre_creation(self, client):
        creation_post = client.post(
            url_for('feiralivre_api.post_feiralivre',
                    registro=self.registro_id),
            data=json.dumps(self.post_data))

        assert creation_post.content_type.split('; ')[0] == 'application/json', \
            "Content Type of creation POST is not JSON: {}".format(
                creation_post.content_type)
        assert creation_post.status_code == 200, \
            "HTTP Status of creation POST is not 200: {}".format(
                creation_post.json)
        assert 'registro' in creation_post.json.keys(), \
            "Key 'registro' is missing: {}".format(creation_post.json)
        assert 'id' in creation_post.json.keys(), \
            "Key 'id' is missing: {}".format(creation_post.json)
        assert self.post_data['bairro'] == creation_post.json['bairro'], \
            "Value for 'bairro' is not equal: {}".format(creation_post.json)

    def test_1_post_feiralivre_validation(self, client):
        invalid_post = client.post(
            url_for('feiralivre_api.post_feiralivre',
                    registro=self.registro_id),
            data=json.dumps({'invalid': 'post'}))

        assert invalid_post.content_type.split('; ')[0] == 'application/json', \
            "Content Type of invalid POST is not JSON: {}".format(
                invalid_post.content_type)
        assert invalid_post.status_code == 422, \
            "HTTP Status of invalid POST is not 422: {}".format(
                invalid_post.json)

        post_keys = list(self.post_data.keys())
        post_keys = set(post_keys)
        resp_keys = set(invalid_post.json['error']['required'])
        missing_req_keys = resp_keys.difference(post_keys)
        assert missing_req_keys == set(), \
            'Missing keys of validation: {}'.format(missing_req_keys)

    def test_2_get_feiralivre_value(self, client):
        get_value = client.get(
            url_for('feiralivre_api.get_feiralivre',
                    registro=self.registro_id))

        assert get_value.content_type.split('; ')[0] == 'application/json', \
            "Content Type of GET value is not JSON: {}".format(
                get_value.content_type)
        assert get_value.status_code == 200, \
            "HTTP Status of GET value is not 200: {}".format(
                get_value.json)
        assert 'registro' in get_value.json.keys(), \
            "Key 'registro' is missing: {}".format(get_value.json)
        assert 'id' in get_value.json.keys(), \
            "Key 'id' is missing: {}".format(get_value.json)
        assert self.post_data['bairro'] == get_value.json['bairro'], \
            "Value for 'bairro' is not equal: {}".format(get_value.json)

    def test_2_get_feiralivre_validate(self, client):
        get_validate = client.get(
            url_for('feiralivre_api.get_feiralivre',
                    registro='INVALID-KEY'))

        assert get_validate.content_type.split('; ')[0] == 'text/html', \
            "Content Type of GET value is not JSON: {}".format(
                get_validate.content_type)
        assert get_validate.status_code == 204, \
            "HTTP Status of GET value is not 204"

    def test_3_valid_search_feiraslivres_by_distrito(self, client):
        search_by_distrito = client.get(
            '{}?distrito={}'.format(
                url_for('feiralivre_api.get_feiraslivres'),
                self.post_data['distrito']))
        assert search_by_distrito.content_type.split('; ')[0] == 'application/json', \
            "Content Type of GET search_by_distrito is not JSON: {}".format(
                search_by_distrito.content_type)
        assert search_by_distrito.status_code == 200, \
            "HTTP Status of GET valid_search_by_distrito is not 200"

    def test_3_unknown_search_feiraslivres_by_distrito(self, client):
        search_by_distrito = client.get(
            '{}?distrito={}'.format(
                url_for('feiralivre_api.get_feiraslivres'),
                'unknown'))
        assert search_by_distrito.content_type.split('; ')[0] == 'application/json', \
            "Content Type of GET search_by_distrito is not JSON: {}".format(
                search_by_distrito.content_type)
        assert search_by_distrito.status_code == 204, \
            "HTTP Status of GET unknown_search_by_distrito is not 204"

    def test_3_valid_search_feiraslivres_by_regiao5(self, client):
        search_by_regiao5 = client.get(
            '{}?regiao5={}'.format(
                url_for('feiralivre_api.get_feiraslivres'),
                self.post_data['regiao5']))
        assert search_by_regiao5.content_type.split('; ')[0] == 'application/json', \
            "Content Type of GET search_by_regiao5 is not JSON: {}".format(
                search_by_regiao5.content_type)
        assert search_by_regiao5.status_code == 200, \
            "HTTP Status of GET valid_search_by_regiao5 is not 200"

    def test_3_unknown_search_feiraslivres_by_regiao5(self, client):
        search_by_regiao5 = client.get(
            '{}?regiao5={}'.format(
                url_for('feiralivre_api.get_feiraslivres'),
                'unknown'))
        assert search_by_regiao5.content_type.split('; ')[0] == 'application/json', \
            "Content Type of GET search_by_regiao5 is not JSON: {}".format(
                search_by_regiao5.content_type)
        assert search_by_regiao5.status_code == 204, \
            "HTTP Status of GET unknown_search_by_regiao5 is not 204"

    def test_3_valid_search_feiraslivres_by_nome_feira(self, client):
        search_by_nome_feira = client.get(
            '{}?nome_feira={}'.format(
                url_for('feiralivre_api.get_feiraslivres'),
                self.post_data['nome_feira']))
        assert search_by_nome_feira.content_type.split('; ')[0] == 'application/json', \
            "Content Type of GET search_by_nome_feira is not JSON: {}".format(
                search_by_nome_feira.content_type)
        assert search_by_nome_feira.status_code == 200, \
            "HTTP Status of GET valid_search_by_nome_feira is not 200"

    def test_3_unknown_search_feiraslivres_by_nome_feira(self, client):
        search_by_nome_feira = client.get(
            '{}?nome_feira={}'.format(
                url_for('feiralivre_api.get_feiraslivres'),
                'unknown'))
        assert search_by_nome_feira.content_type.split('; ')[0] == 'application/json', \
            "Content Type of GET search_by_nome_feira is not JSON: {}".format(
                search_by_nome_feira.content_type)
        assert search_by_nome_feira.status_code == 204, \
            "HTTP Status of GET unknown_search_by_nome_feira is not 204"

    def test_3_valid_search_feiraslivres_by_bairro(self, client):
        search_by_bairro = client.get(
            '{}?bairro={}'.format(
                url_for('feiralivre_api.get_feiraslivres'),
                self.post_data['bairro']))
        assert search_by_bairro.content_type.split('; ')[0] == 'application/json', \
            "Content Type of GET search_by_bairro is not JSON: {}".format(
                search_by_bairro.content_type)
        assert search_by_bairro.status_code == 200, \
            "HTTP Status of GET valid_search_by_bairro is not 200"

    def test_3_unknown_search_feiraslivres_by_bairro(self, client):
        search_by_bairro = client.get(
            '{}?bairro={}'.format(
                url_for('feiralivre_api.get_feiraslivres'),
                'unknown'))
        assert search_by_bairro.content_type.split('; ')[0] == 'application/json', \
            "Content Type of GET search_by_bairro is not JSON: {}".format(
                search_by_bairro.content_type)
        assert search_by_bairro.status_code == 204, \
            "HTTP Status of GET unknown_search_by_bairro is not 204"

    def test_4_put_feiralivre_value(self, client):
        changing_put = client.put(
            url_for('feiralivre_api.put_feiralivre',
                    registro=self.registro_id),
            data=json.dumps(self.put_data))

        assert changing_put.content_type.split('; ')[0] == 'application/json', \
            "Content Type of changing PUT is not JSON: {}".format(
                changing_put.content_type)
        assert changing_put.status_code == 200, \
            "HTTP Status of changing PUT is not 200: {}".format(
                changing_put.json)
        assert 'registro' in changing_put.json.keys(), \
            "Key 'registro' is missing: {}".format(changing_put.json)
        assert 'id' in changing_put.json.keys(), \
            "Key 'id' is missing: {}".format(changing_put.json)
        assert self.put_data['bairro'] == changing_put.json['bairro'], \
            "Value for 'bairro' is not equal: {}".format(changing_put.json)

    def test_4_put_feiralivre_validate(self, client):
        put_validate = client.put(
            url_for('feiralivre_api.put_feiralivre',
                    registro='INVALID-KEY'),
            data=json.dumps(self.put_data))

        assert put_validate.content_type.split('; ')[0] == 'text/html', \
            "Content Type of put value is not JSON: {}".format(
                put_validate.content_type)
        assert put_validate.status_code == 204, \
            "HTTP Status of put value is not 204: {}".format(
                put_validate.data)

    def test_5_delete_feiralivre(self, client):
        resp_put = client.delete(
            url_for('feiralivre_api.delete_feiralivre',
                    registro=self.registro_id),
            data=json.dumps(self.put_data))

        assert resp_put.status_code == 200, \
            "PUT Response is not 200: {}".format(resp_put.json)
        assert 'registro' in resp_put.json.keys(), \
            "JSON returned without 'registro' key {}".format(resp_put.json)
        assert 'id' in resp_put.json.keys(), \
            "JSON returned without 'id' key {}".format(resp_put.json)
        assert self.put_data['bairro'] == resp_put.json['bairro'], \
            "New value for 'bairro' is not equal: {}".format(resp_put.json)

    def test_5_delete_feiralivre_validate(self, client):
        delete_validate = client.delete(
            url_for('feiralivre_api.delete_feiralivre',
                    registro='INVALID-KEY'))

        assert delete_validate.content_type.split('; ')[0] == 'text/html', \
            "Content Type of delete value is not JSON: {}".format(
                delete_validate.content_type)
        assert delete_validate.status_code == 204, \
            "HTTP Status of delete value is not 204"
