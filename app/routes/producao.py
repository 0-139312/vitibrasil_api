from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.services.scraper import get_data_all_sections

producao_bp = Blueprint('producao', __name__, url_prefix='/producao')

@producao_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Produção'],
    'parameters': [
        {'name': 'ano', 'in': 'query', 'type': 'string', 'required': False, 'description': 'Filtrar por ano'},
        {'name': 'produto', 'in': 'query', 'type': 'string', 'required': False, 'description': 'Filtrar por nome do produto'},
        {'name': 'limit', 'in': 'query', 'type': 'integer', 'required': False, 'description': 'Qtd de registros'},
        {'name': 'offset', 'in': 'query', 'type': 'integer', 'required': False, 'description': 'Qtd a pular'}
    ],
    'responses': {
        200: {
            'description': 'Lista de produção',
            'examples': {
                'application/json': [{'ano': 2021, 'produto': 'Vinho de Mesa', 'quantidade': 173899995}]
            }
        }
    }
})
def get_producao():
    dados = get_data_all_sections("producao")
    ano = request.args.get('ano')
    produto = request.args.get('produto')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    if ano:
        dados = [d for d in dados if str(d.get('ano')) == str(ano)]
    if produto:
        dados = [d for d in dados if produto.lower() in d.get('produto', '').lower()]

    return jsonify(dados[offset:offset+limit])