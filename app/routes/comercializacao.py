from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.services.scraper import get_data_all_sections

comercializacao_bp = Blueprint('comercializacao', __name__)

@comercializacao_bp.route('/comercializacao', methods=['GET'])
@swag_from({
    'tags': ['Comercialização'],
    'parameters': [
        {'name': 'ano', 'in': 'query', 'type': 'string'},
        {'name': 'produto', 'in': 'query', 'type': 'string'},
        {'name': 'limit', 'in': 'query', 'type': 'integer'},
        {'name': 'offset', 'in': 'query', 'type': 'integer'}
    ],
    'responses': {200: {'description': 'Lista de comercialização'}}
})
def get_comercializacao():
    dados = get_data_all_sections("comercializacao")
    ano = request.args.get('ano')
    produto = request.args.get('produto')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    if ano:
        dados = [d for d in dados if str(d.get('ano')) == str(ano)]
    produto_param = request.args.get('produto')
    if produto_param:
        produto_param = produto_param.lower().strip()
        dados = [
            d for d in dados
            if any(
                produto_param in str(v).lower().strip()
                for k, v in d.items()
                if 'produto' in k.lower()
        )
    ]

    return jsonify(dados[offset:offset+limit])