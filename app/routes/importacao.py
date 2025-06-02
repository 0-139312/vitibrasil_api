from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.services.scraper import get_data_all_sections

importacao_bp = Blueprint('importacao', __name__)

@importacao_bp.route('/importacao', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'ano',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'Ano de interesse (ex: 2021)'
        },
        {
            'name': 'pais',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'Filtrar por nome do país'
        },
        {
            'name': 'limit',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': 'Limite de registros'
        },
        {
            'name': 'offset',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': 'Deslocamento inicial dos registros'
        },
    ],
    'responses': {
        200: {
            'description': 'Lista de dados de importação'
        }
    }
})
def get_importacao():
    ano = request.args.get('ano')
    pais = request.args.get('pais')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    dados = get_data_all_sections("importacao")

    print(f"[DEBUG] Total bruto: {len(dados)}")

    if ano:
        ano = str(ano).strip()
        dados = [d for d in dados if 'ano' in d and str(d['ano']) == ano]
        print(f"[DEBUG] Filtrado por ano={ano}, total: {len(dados)}")

    if pais:
        pais = pais.lower().strip()
        dados = [d for d in dados if 'país' in d and pais in d['país'].lower().strip()]
        print(f"[DEBUG] Filtrado por pais={pais}, total: {len(dados)}")

    return jsonify(dados[offset:offset + limit])
