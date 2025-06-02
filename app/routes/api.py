from flask import Blueprint, request, jsonify, redirect
from app.services.scraper import get_data_all_sections

api_bp = Blueprint('api', __name__)

@api_bp.route('/', methods=['GET'])
def home():
    return {
        "mensagem": "Bem-vindo à API da Vitivinicultura Brasileira",
        "documentacao": "/apidocs",
        "exemplo": "/producao?ano=2021&limit=5",
        "rotas_disponiveis": [
            "/producao",
            "/processamento",
            "/comercializacao",
            "/importacao",
            "/exportacao"
        ]
    }

@api_bp.route('/producao', methods=['GET'])
def get_producao():
    """
    ---
    parameters:
      - name: ano
        in: query
        type: string
        required: false
        description: "Filtrar por ano, por exemplo: 2021"
      - name: produto
        in: query
        type: string
        required: false
        description: "Nome do produto (ex: Tinto, Branco)"
      - name: limit
        in: query
        type: integer
        required: false
        default: 10
      - name: offset
        in: query
        type: integer
        required: false
        default: 0
    responses:
      200:
        description: "Lista de registros de produção"
    """
    dados = get_data_all_sections("producao")
    ano = request.args.get('ano')
    produto = request.args.get('produto')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    if ano:
        dados = [d for d in dados if str(d.get('ano')) == str(ano)]
    if produto:
        dados = [d for d in dados if str(d.get('produto')).lower() == produto.lower()]

    return jsonify(dados[offset:offset+limit])

@api_bp.route('/processamento', methods=['GET'])
def get_processamento():
    """
    ---
    parameters:
      - name: ano
        in: query
        type: string
        required: false
      - name: cultivar
        in: query
        type: string
        required: false
        description: "Nome da cultivar (ex: Isabel, Bordo)"
      - name: limit
        in: query
        type: integer
        required: false
        default: 10
      - name: offset
        in: query
        type: integer
        required: false
        default: 0
    responses:
      200:
        description: "Lista de registros de processamento"
    """
    dados = get_data_all_sections("processamento")
    ano = request.args.get('ano')
    cultivar = request.args.get('cultivar')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    if ano:
        dados = [d for d in dados if str(d.get('ano')) == str(ano)]
    if cultivar:
        dados = [d for d in dados if str(d.get('cultivar')).lower() == cultivar.lower()]

    return jsonify(dados[offset:offset+limit])

@api_bp.route('/comercializacao', methods=['GET'])
def get_comercializacao():
    """
    ---
    parameters:
      - name: ano
        in: query
        type: string
        required: false
      - name: produto
        in: query
        type: string
        required: false
      - name: limit
        in: query
        type: integer
        required: false
        default: 10
      - name: offset
        in: query
        type: integer
        required: false
        default: 0
    responses:
      200:
        description: "Lista de registros de comercialização"
    """
    dados = get_data_all_sections("comercializacao")
    ano = request.args.get('ano')
    produto = request.args.get('produto')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    if ano:
        dados = [d for d in dados if str(d.get('ano')) == str(ano)]
    if produto:
      dados = [
        d for d in dados
        if d.get('produto') and produto.lower().strip() in d.get('produto').lower().strip()
      ]


    return jsonify(dados[offset:offset+limit])

@api_bp.route('/importacao', methods=['GET'])
def get_importacao():
    """
    ---
    parameters:
      - name: ano
        in: query
        type: string
        required: false
      - name: produto
        in: query
        type: string
        required: false
      - name: pais
        in: query
        type: string
        required: false
      - name: limit
        in: query
        type: integer
        required: false
        default: 10
      - name: offset
        in: query
        type: integer
        required: false
        default: 0
    responses:
      200:
        description: "Lista de registros de importação"
    """
    dados = get_data_all_sections("importacao")
    ano = request.args.get('ano')
    produto = request.args.get('produto')
    pais = request.args.get('pais')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    if ano:
        dados = [d for d in dados if str(d.get('ano')) == str(ano)]
    if produto:
        dados = [d for d in dados if str(d.get('produto')).lower() == produto.lower()]
    if pais:
        dados = [d for d in dados if str(d.get('pais')).lower() == pais.lower()]

    return jsonify(dados[offset:offset+limit])

@api_bp.route('/exportacao', methods=['GET'])
def get_exportacao():
    """
    ---
    parameters:
      - name: ano
        in: query
        type: string
        required: false
      - name: produto
        in: query
        type: string
        required: false
      - name: pais
        in: query
        type: string
        required: false
      - name: limit
        in: query
        type: integer
        required: false
        default: 10
      - name: offset
        in: query
        type: integer
        required: false
        default: 0
    responses:
      200:
        description: "Lista de registros de exportação"
    """
    dados = get_data_all_sections("exportacao")
    ano = request.args.get('ano')
    produto = request.args.get('produto')
    pais = request.args.get('pais')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    if ano:
        dados = [d for d in dados if str(d.get('ano')) == str(ano)]
    if produto:
        dados = [d for d in dados if str(d.get('produto')).lower() == produto.lower()]
    if pais:
        dados = [d for d in dados if str(d.get('pais')).lower() == pais.lower()]

    return jsonify(dados[offset:offset+limit])
