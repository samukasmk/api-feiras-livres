from flask import Blueprint, request, jsonify
from flask_restful import reqparse
from app.database import db
from .models import FeiraLivre

feira_livre_api = Blueprint('feiralivre_api', __name__)


@feira_livre_api.route('/api/v1/feiralivre/<string:registro>', methods=['GET'])
def get_feiralivre(registro):
    feira_obj = FeiraLivre.query.filter_by(registro=registro).first()
    if feira_obj:
        return jsonify(feira_obj.serialize())
    else:
        return '', 204


@feira_livre_api.route('/api/v1/feiralivre/<string:registro>', methods=['POST'])
def post_feiralivre(registro):
    json_args = request.get_json(force=True)
    required_params = FeiraLivre.__table__.columns.keys()

    # remove imutable params from actions
    for imutable_param in ["id", "registro", "date_modified", "date_created"]:
        json_args.pop(imutable_param, None)
        required_params.remove(imutable_param)

    # analize required params is missing
    passed_params = set(json_args.keys())
    required_params = set(required_params)
    missing_params = list(required_params.difference(passed_params))

    if len(missing_params) > 0:
        return jsonify(error=dict(
            message='Required params is missing for POST',
            required=missing_params)), 422

    json_args['registro'] = registro
    try:
        feira_obj = FeiraLivre(**json_args)
        db.session.add(feira_obj)
        db.session.commit()
    except Exception as e:
        return jsonify(error=dict(message=str(e))), 422
    else:
        return jsonify(feira_obj.serialize())


@feira_livre_api.route('/api/v1/feiralivre/<string:registro>', methods=['PUT'])
def put_feiralivre(registro):
    json_args = request.get_json(force=True)
    # remove imutable params from actions
    for imutable_param in ["id", "registro", "date_modified", "date_created"]:
        json_args.pop(imutable_param, None)

    feira_obj = FeiraLivre.query.filter_by(registro=registro).first()
    if feira_obj is None:
        return '', 204

    try:
        for arg in json_args.keys():
            setattr(feira_obj, arg, json_args[arg])
        db.session.commit()
    except Exception as e:
        return jsonify(error=dict(message=str(e))), 422
    else:
        return jsonify(feira_obj.serialize())


@feira_livre_api.route('/api/v1/feiralivre/<string:registro>', methods=['DELETE'])
def delete_feiralivre(registro):
    feira_obj = FeiraLivre.query.filter_by(registro=registro).first()
    if feira_obj:
        db.session.delete(feira_obj)
        db.session.commit()
        return jsonify(feira_obj.serialize())
    else:
        return '', 204


@feira_livre_api.route('/api/v1/feiraslivres/', methods=['GET'])
def get_feiraslivres():
    # Define
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, location='args', required=False)
    parser.add_argument('bairro', type=str, location='args', required=False)
    parser.add_argument('distrito', type=str, location='args', required=False)
    parser.add_argument('nome_feira', type=str, location='args', required=False)
    parser.add_argument('regiao5', type=str, location='args', required=False)
    args = parser.parse_args()

    # Build query object with params
    query = FeiraLivre.query
    if 'offset' in args.keys():
        query = query.offset(args.pop('offset'))
    if 'limit' in args.keys():
        query = query.limit(args.pop('limit'))
    query_params = {k: v for k, v in args.items() if v}

    feira_obj = query.filter_by(**query_params).all()

    if feira_obj:
        return jsonify(feiras=[e.serialize() for e in feira_obj])
    else:
        return jsonify(feiras=[]), 204
