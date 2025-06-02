from flask import Flask
from flasgger import Swagger
from app.config import Config

from app.routes.producao import producao_bp
from app.routes.processamento import processamento_bp
from app.routes.comercializacao import comercializacao_bp
from app.routes.importacao import importacao_bp
from app.routes.exportacao import exportacao_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Swagger(app, config={
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # todas as rotas
                "model_filter": lambda tag: True,  # todos os modelos
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs" 
    })


    app.register_blueprint(producao_bp)
    app.register_blueprint(processamento_bp)
    app.register_blueprint(comercializacao_bp)
    app.register_blueprint(importacao_bp)
    app.register_blueprint(exportacao_bp)

    return app
