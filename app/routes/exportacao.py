### vitibrasil_api/app/routes/exportacao.py
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.services.scraper import get_data_all_sections

exportacao_bp = Blueprint('exportacao', __name__, url_prefix='/exportacao')

@exportacao_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Exportação'],
    'parameters': [
        {
            'name': 'ano',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'Filtrar por ano (ex: 2021)'
        },
        {
            'name': 'pais',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'Filtrar por país (ex: Afeganistão)'
        },
        {
            'name': 'limit',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': 'Quantidade de registros a retornar'
        },
        {
            'name': 'offset',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': 'Quantidade de registros a pular'
        },
    ],
    'responses': {
        200: {
            'description': 'Lista de exportações',
            'examples': {
                'application/json': [
                    {
                        "ano": 2021,
                        "quantidade": 859169,
                        "valor": 2508140,
                        "país": "Afeganistão",
                        "id": 1,
                        "arquivo": "ExpVinho.csv"
                    }
                ]
            }
        }
    }
})
def get_exportacao():
    dados = get_data_all_sections("exportacao")
    ano = request.args.get('ano')
    pais = request.args.get('pais')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    if ano:
        dados = [d for d in dados if 'ano' in d and str(d['ano']).strip() == str(ano).strip()]

    if pais:
        dados = [d for d in dados if d.get('país', '').lower() == pais.lower()]

    return jsonify(dados[offset:offset+limit])
