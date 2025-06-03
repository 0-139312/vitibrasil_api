from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.services.scraper import get_data_all_sections

processamento_bp = Blueprint('processamento', __name__, url_prefix='/processamento')

@processamento_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Processamento'],
    'parameters': [
        {'name': 'ano', 'in': 'query', 'type': 'string', 'required': False},
        {'name': 'cultivar', 'in': 'query', 'type': 'string', 'required': False},
        {'name': 'limit', 'in': 'query', 'type': 'integer', 'required': False},
        {'name': 'offset', 'in': 'query', 'type': 'integer', 'required': False}
    ],
    'responses': {200: {'description': 'Lista de processamento'}}
})
def get_processamento():
    dados = get_data_all_sections("processamento")
    ano = request.args.get('ano')
    cultivar = request.args.get('cultivar')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    if ano:
        dados = [d for d in dados if str(d.get('ano')) == str(ano)]
    if cultivar:
        dados = [d for d in dados if cultivar.lower() in d.get('cultivar', '').lower()]

    return jsonify(dados[offset:offset+limit])