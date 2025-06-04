from flask import Flask
from flasgger import Swagger
from app.config import Config

# Blueprints
from app.routes.producao import producao_bp
from app.routes.processamento import processamento_bp
from app.routes.comercializacao import comercializacao_bp
from app.routes.importacao import importacao_bp
from app.routes.exportacao import exportacao_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configuração correta do Swagger
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "swagger_ui": True,
        "specs_route": "/apidocs"
    }

    Swagger(app, config=swagger_config)

    # Blueprints
    app.register_blueprint(producao_bp)
    app.register_blueprint(processamento_bp)
    app.register_blueprint(comercializacao_bp)
    app.register_blueprint(importacao_bp)
    app.register_blueprint(exportacao_bp)

    # ✅ Rota raiz
    @app.route("/")
    def index():
        return {"message": "API Vitibrasil ativa. Acesse /apidocs para a documentação."}

    return app
