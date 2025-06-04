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

    # Configuração do Swagger UI via CDN externo (funciona na Render)
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Vitibrasil API",
            "description": "API com dados da vitivinicultura brasileira",
            "version": "1.0.0"
        },
        "basePath": "/",
        "schemes": ["https"]
    }

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs",
        "swagger_ui_bundle_js": "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.15.5/swagger-ui-bundle.js",
        "swagger_ui_standalone_preset_js": "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.15.5/swagger-ui-standalone-preset.js",
        "swagger_ui_css": "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.15.5/swagger-ui.css"
    }

    Swagger(app, config=swagger_config, template=swagger_template)

    # Registrar os blueprints
    app.register_blueprint(producao_bp)
    app.register_blueprint(processamento_bp)
    app.register_blueprint(comercializacao_bp)
    app.register_blueprint(importacao_bp)
    app.register_blueprint(exportacao_bp)

    return app
